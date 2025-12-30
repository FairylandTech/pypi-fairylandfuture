# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-12-29 19:46:12 UTC+08:00
"""

import contextlib
import datetime
import typing as t

import psycopg
import psycopg.sql
from psycopg.rows import dict_row, tuple_row

from fairylandfuture import logger
from fairylandfuture.models import BaseModelPostgreSQL
from fairylandfuture.structures.database import PostgreSQLExecuteStructure
from fairylandfuture.utils.strings import StringUtils

MODEL_ORM_TYPE = t.TypeVar("MODEL_ORM_TYPE", bound="BaseModelPostgreSQL")


class PostgreSQLConnector:

    def __init__(
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        database: str,
        timezone: str = "Asia/Shanghai",
        keepalive_idle: int = 60,
        keepalive_interval: int = 10,
        keepalive_count: int = 5,
        connect_timeout: int = 10,
        autocommit: bool = False,
        **kwargs,
    ):
        self.autocommit = autocommit
        self.__connection_params = {
            "host": host,
            "port": port,
            "user": username,
            "password": password,
            "dbname": database,
            "connect_timeout": connect_timeout,
            "keepalives_idle": keepalive_idle,
            "keepalives_interval": keepalive_interval,
            "keepalives_count": keepalive_count,
            "options": f"-c timezone={timezone}",
            **kwargs,
        }
        self.__connection: t.Optional[psycopg.Connection] = None

        self.__connection_id: int = 0
        self.__last_activity_timestamp: float = 0.0

    def __enter__(self):
        self.ensure_connection()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        if self.__connection is None or self.__connection.closed:
            self.__connect()
        else:
            if not self.__is_connection_alive():
                logger.warning("PostgreSQL connection lost, reconnecting...")
                self.__reconnect()

        self.__last_activity_timestamp = datetime.datetime.now().timestamp()
        return self.__connection

    def __connect(self):
        try:
            self.__connection = psycopg.connect(**self.__connection_params, autocommit=self.autocommit)
            self.__connection_id += 1
            self.__last_activity_timestamp = datetime.datetime.now().timestamp()
            logger.info(f"PostgreSQL connected successfully, connection id: {self.__connection_id}")
        except Exception as err:
            logger.error(f"PostgreSQL connection error: {err}")
            raise

    def __is_connection_alive(self) -> bool:
        try:
            if self.__connection is None or self.__connection.closed:
                return False
            with self.__connection.cursor() as cursor:
                cursor.execute("SELECT 1;")
                cursor.fetchall()
            return True
        except Exception as err:
            logger.error(f"PostgreSQL connection id {self.__connection_id} is not alive: {err}")
            return False

    def __reconnect(self):
        self.close()
        self.__connect()

    def ensure_connection(self):
        _ = self.connection

    def close(self):
        if self.__connection and not self.__connection.closed:
            try:
                self.__connection.close()
                logger.info(f"PostgreSQL connection id {self.__connection_id} closed.")
            except Exception as err:
                logger.error(f"Error closing PostgreSQL connection id {self.__connection_id}: {err}")
            finally:
                self.__connection = None

    def get_cursor(self, /, *, row_factory: t.Optional[psycopg.rows.RowFactory] = None) -> psycopg.Cursor:
        if row_factory:
            return self.connection.cursor(row_factory=row_factory)
        return self.connection.cursor()

    def commit(self):
        try:
            self.connection.commit()
            logger.debug(f"Transaction committed.")
        except Exception as err:
            logger.error(f"Error committing PostgreSQL connection id {self.__connection_id}: {err}")
            raise err

    def rollback(self):
        try:
            self.connection.rollback()
            logger.debug(f"Transaction rolled back.")
        except Exception as err:
            logger.error(f"Error rolling back PostgreSQL connection id {self.__connection_id}: {err}")
            raise

    @contextlib.contextmanager
    def transaction(self):
        connection = self.connection
        try:
            with connection.transaction():
                yield connection
        except Exception as err:
            logger.error(f"Transaction error on PostgreSQL connection id {self.__connection_id}: {err}")
            raise


class PostgreSQLRepository:

    def __init__(self, connector: PostgreSQLConnector):
        self.connector = connector

    def __insert_of_model(self, model: "MODEL_ORM_TYPE") -> "PostgreSQLExecuteStructure":
        table_identifier = psycopg.sql.Identifier(model.__table__.schema, model.__tablename__) if model.__table__.schema else psycopg.sql.Identifier(model.__tablename__)
        columns = [column.key for column in model.__mapper__.columns if getattr(model, column.key, None) is not None]
        query = psycopg.sql.SQL("insert into {table} ({fields}) values ({values})").format(
            table=table_identifier,
            fields=psycopg.sql.SQL(", ").join(map(psycopg.sql.Identifier, columns)),
            values=psycopg.sql.SQL(", ").join(map(lambda column: psycopg.sql.Placeholder(column), columns)),
        )
        vars = {column: getattr(model, column, None) for column in columns}
        return PostgreSQLExecuteStructure(query, vars)

    def __insert_of_args(self):
        pass

    def execute(self, exec: PostgreSQLExecuteStructure, commit: bool = False):
        cursor = self.connector.get_cursor()
        try:
            logger.debug(f"Executing PostgreSQL query: {exec.query.as_string()} with vars: {exec.vars}")
            cursor.execute(exec.query, exec.vars)
            if commit:
                self.connector.commit()
            return cursor
        except Exception as error:
            logger.error(f"Error executing PostgreSQL query: {error}")
            raise

    def executemany(self, exec: PostgreSQLExecuteStructure, batch_size: int = 1000, commit_interval: int = 10000, show_progress: bool = True):
        total_rows: int = len(exec.vars) if exec.vars else 0
        processed_rows: int = 0
        start_time: float = datetime.datetime.now().timestamp()

        cursor = self.connector.get_cursor()
        try:
            for i in range(0, total_rows, batch_size):
                batch = exec.vars[i : i + batch_size]

                self.connector.ensure_connection()

                logger.debug(f"Executing batch of size {len(batch)} for PostgreSQL query: {StringUtils.format(exec.query.as_string(), "SQL")}")
                cursor.executemany(exec.query, batch)
                processed_rows += len(batch)

                if processed_rows % commit_interval == 0 or processed_rows == total_rows:
                    self.connector.commit()

                    if show_progress:
                        elapsed = datetime.datetime.now().timestamp() - start_time
                        logger.info(f"Executed {processed_rows}/{total_rows} rows in {elapsed:.2f} seconds.")

            total_elapsed = datetime.datetime.now().timestamp() - start_time
            logger.info(f"Completed executing {total_rows} rows in {total_elapsed:.2f} seconds, average {total_rows / total_elapsed:.2f} rows/second.")
            return processed_rows
        except Exception as error:
            logger.error(f"Error executing PostgreSQL batch query: {error}")
            raise

    @t.overload
    def fetchone(self, exec: PostgreSQLExecuteStructure, /, *, as_dict: t.Literal[True] = True) -> t.Optional[t.Dict[str, t.Any]]: ...

    @t.overload
    def fetchone(self, exec: PostgreSQLExecuteStructure, /, *, as_dict: t.Literal[False] = False) -> t.Optional[t.Tuple[t.Any, ...]]: ...

    @t.overload
    def fetchone(self, exec: PostgreSQLExecuteStructure, /, *, clazz: t.Type[MODEL_ORM_TYPE]) -> t.Optional[MODEL_ORM_TYPE]: ...

    def fetchone(
        self,
        exec: PostgreSQLExecuteStructure,
        /,
        *,
        as_dict: bool = True,
        clazz: t.Optional[t.Type[MODEL_ORM_TYPE]] = None,
    ) -> t.Dict[str, t.Any] | t.Tuple[t.Any, ...] | MODEL_ORM_TYPE | None:
        row_factory = dict_row if (as_dict or clazz) else tuple_row
        cursor = self.connector.get_cursor(row_factory=row_factory)

        logger.debug(f"Fetching one row for PostgreSQL query: {StringUtils.format(exec.query.as_string(), "SQL")} with vars: {exec.vars}")

        cursor.execute(exec.query, exec.vars)
        row = cursor.fetchone()

        logger.debug(f"Fetched one row: {row}")

        if clazz:
            return clazz(**row)
        return row

    @t.overload
    def fetchmany(
        self,
        exec: PostgreSQLExecuteStructure,
        /,
        *,
        size: int = 100,
        as_dict: t.Literal[True] = True,
    ) -> t.Generator[t.List[t.Dict[str, t.Any]], None, None]: ...

    @t.overload
    def fetchmany(
        self,
        exec: PostgreSQLExecuteStructure,
        /,
        *,
        size: int = 100,
        as_dict: t.Literal[False] = False,
    ) -> t.Generator[t.List[t.Tuple[t.Any, ...]], None, None]: ...

    @t.overload
    def fetchmany(
        self,
        exec: PostgreSQLExecuteStructure,
        /,
        *,
        size: int = 100,
        clazz: t.Type[MODEL_ORM_TYPE],
    ) -> t.Generator[t.List[MODEL_ORM_TYPE], None, None]: ...

    def fetchmany(
        self,
        exec: PostgreSQLExecuteStructure,
        /,
        *,
        size: int = 100,
        as_dict: bool = True,
        clazz: t.Optional[t.Type[MODEL_ORM_TYPE]] = None,
    ) -> t.Generator[t.List[t.Dict[str, t.Any]] | t.List[t.Tuple[t.Any, ...] | t.List[MODEL_ORM_TYPE]], None, None]:
        row_factory = dict_row if (as_dict or clazz) else tuple_row
        cursor = self.connector.get_cursor(row_factory=row_factory)
        cursor.execute(exec.query, exec.vars)

        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            if clazz:
                yield [clazz(**row) for row in rows]
            else:
                yield rows

    def insert(
        self,
        data: t.Mapping[str, t.Any] | MODEL_ORM_TYPE,
        table: str,
        schema: t.Optional[str] = None,
        returning: str = "id",
        commit: bool = False,
    ) -> int | t.Literal[True]:
        if not data:
            logger.warning("No data provided for insert operation.")
            raise ValueError("Data for insert operation cannot be empty.")

        if isinstance(data, BaseModelPostgreSQL):
            exec_query_lang = self.__insert_of_model(data)

        table_identifier = psycopg.sql.Identifier(schema, table) if schema else psycopg.sql.Identifier(table)

        columns = tuple(data.keys())

        query = psycopg.sql.SQL("insert into {table} ({fields}) values ({values})").format(
            table=table_identifier,
            fields=psycopg.sql.SQL(", ").join(map(psycopg.sql.Identifier, columns)),
            values=psycopg.sql.SQL(", ").join(map(lambda column: psycopg.sql.Placeholder(column), columns)),
        )

        if returning:
            query += psycopg.sql.SQL(" returning {}").format(psycopg.sql.Identifier(returning))

        cursor = self.execute(PostgreSQLExecuteStructure(query, data), commit=commit)

        if returning:
            row = cursor.fetchone()
            if row is None:
                logger.error("Insert operation did not return any value.")
                raise RuntimeError("Insert operation failed to return the expected value.")
            return row[0]

        return True
