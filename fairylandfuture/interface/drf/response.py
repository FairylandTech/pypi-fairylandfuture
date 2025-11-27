# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2025-05-27 15:51:45 UTC+08:00
"""

import typing as t

from rest_framework.response import Response

from fairylandfuture.structures.http.response import ResponseFrozenStructure, ResponseStructure


class DRFResponseMixin:

    def _response(
        self,
        data: ResponseStructure | ResponseFrozenStructure,
        headers: dict[str, t.Any] | None = None,
        content_type: str | None = None,
        exception: bool = False,
    ):
        if not isinstance(data, (ResponseStructure, ResponseFrozenStructure)):
            raise TypeError("data must be an instance of ResponseStructure or ResponseFrozenStructure")

        if not content_type:
            content_type = "application/json"

        return Response(data=data.asdict, status=data.code, headers=headers, content_type=content_type, exception=exception)
