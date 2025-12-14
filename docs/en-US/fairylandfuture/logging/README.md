# fairylandfuture.logging 使用文档

## 快速开始

### 基础用法

```python
from fairylandfuture.logging import LogManager, Config

# 1. 配置日志（应用启动时执行一次）
LogManager.configure(Config(
    level='INFO',
    console=True,
    file=False
))

# 2. 获取 logger（每个模块/类获取自己的 logger）
logger = LogManager.get_logger(__name__)

# 3. 记录日志
logger.info('这是一条信息日志')
logger.debug('这是一条调试日志')
logger.warning('这是一条警告日志')
logger.error('这是一条错误日志')
```

---

## 配置选项

### Config 参数说明

```python
from fairylandfuture.logging import Config

config = Config(
    level='INFO',           # 日志级别：TRACE/DEBUG/INFO/WARNING/ERROR/CRITICAL
    console=True,           # 是否输出到控制台
    file=False,             # 是否输出到文件
    dirname='logs',         # 日志文件目录
    filename='service.log', # 日志文件名
    rotation='5 MB',        # 日志文件轮转大小（5 MB / 10 MB / 100 MB）
    retention='180 days',   # 日志保留时间（7 days / 30 days / 180 days）
    pattern='...',          # 日志格式模板
    json=False,             # 是否使用 JSON 格式（结构化日志）
    encoding='utf-8'        # 文件编码
)
```

### 从 YAML 加载配置

```yaml
# conf/logging.yaml
level: INFO
console: true
file: true
dirname: logs
filename: service.log
rotation: 10 MB
retention: 30 days
json: false
encoding: utf-8
```

```python
from fairylandfuture.logging import LogManager, Config

config = Config.from_yaml('conf/logging.yaml')
LogManager.configure(config)
```

### 从环境变量加载配置

```bash
# 设置环境变量
export FAIRY_LOG_LEVEL=DEBUG
export FAIRY_LOG_ENABLE_CONSOLE=true
export FAIRY_LOG_ENABLE_FILE=true
export FAIRY_LOG_DIR=logs
export FAIRY_LOG_FILE=app.log
export FAIRY_LOG_JSON=false
```

```python
from fairylandfuture.logging import LogManager, Config

config = Config.from_env(prefix='FAIRY_LOG_')
LogManager.configure(config)
```

---

## 实际使用场景

### 1. 开发环境配置

```python
from fairylandfuture.logging import LogManager, Config

# 开发环境：控制台输出 + DEBUG 级别
LogManager.configure(Config(
    level='DEBUG',
    console=True,
    file=False
))
```

### 2. 生产环境配置

```python
from fairylandfuture.logging import LogManager, Config

# 生产环境：文件输出 + INFO 级别
LogManager.configure(Config(
    level='INFO',
    console=False,
    file=True,
    dirname='/var/log/myapp',
    filename='app.log',
    rotation='50 MB',
    retention='30 days'
))
```

### 3. JSON 结构化日志（用于日志分析平台）

```python
LogManager.configure(Config(
    level='INFO',
    console=False,
    file=True,
    dirname='logs',
    filename='app.json',
    json=True,  # 启用 JSON 格式
    rotation='10 MB',
    retention='30 days'
))
```

### 4. 在类中使用

```python
from fairylandfuture.logging import LogManager

class UserService:
    def __init__(self):
        # 每个类获取自己的命名 logger
        self.logger = LogManager.get_logger('myapp.service.user')
    
    def create_user(self, username: str):
        self.logger.info(f'创建用户: username={username}')
        try:
            # 业务逻辑
            self.logger.debug(f'插入数据库: {username}')
            # ...
            self.logger.info(f'用户创建成功: {username}')
        except Exception as e:
            self.logger.error(f'创建用户失败: {str(e)}')
            raise
```

### 5. 层级日志级别（不同模块不同级别）

```python
from fairylandfuture.logging import LogManager, Config

# 全局默认 INFO
LogManager.configure(Config(console=True, level='INFO'))

# API 层需要详细日志
LogManager.set_level('myapp.api', 'DEBUG')

# 数据库层只记录警告及以上
LogManager.set_level('myapp.db', 'WARNING')

# 支付模块记录所有
LogManager.set_level('myapp.payment', 'TRACE')
```

### 6. Django 项目中使用

```python
# settings.py
from fairylandfuture.logging import LogManager, Config

# 在 Django 启动时配置
LogManager.configure(Config(
    level='DEBUG' if DEBUG else 'INFO',
    console=DEBUG,
    file=True,
    dirname=str(BASE_DIR / 'logs'),
    filename='django.log'
))

# views.py
from fairylandfuture.logging import LogManager

class UserViewSet(ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logger = LogManager.get_logger('myapp.views.user')
    
    def list(self, request):
        self.logger.info(f'查询用户列表: user={request.user}')
        # ...
```

### 7. 异常处理与日志

```python
from fairylandfuture.logging import LogManager

logger = LogManager.get_logger(__name__)

try:
    # 业务逻辑
    result = some_operation()
    logger.info(f'操作成功: {result}')
except ValueError as e:
    # 业务异常
    logger.warning(f'参数错误: {str(e)}')
except Exception as e:
    # 系统异常
    logger.error(f'系统错误: {str(e)}')
    raise
```

---

## 最佳实践

### 1. 命名规范

```python
# 推荐使用模块路径作为 logger 名称
logger = LogManager.get_logger(__name__)

# 或使用业务模块名
logger = LogManager.get_logger('myapp.api.user')
logger = LogManager.get_logger('myapp.service.order')
logger = LogManager.get_logger('myapp.db.repository')
```

### 2. 日志级别使用指南

- **TRACE**：非常详细的调试信息（SQL 语句、请求详情）
- **DEBUG**：调试信息（函数调用、变量值）
- **INFO**：重要业务流程（用户登录、订单创建）
- **WARNING**：警告信息（参数校验失败、降级处理）
- **ERROR**：错误信息（异常捕获、失败重试）
- **CRITICAL**：严重错误（系统崩溃、数据丢失）

### 3. 应用启动流程

```python
# main.py
from fairylandfuture.logging import LogManager, Config

def init_app():
    # 1. 首先初始化日志
    LogManager.configure(Config.from_env())
    
    # 2. 获取应用 logger
    logger = LogManager.get_logger('myapp')
    logger.info('应用启动中...')
    
    # 3. 初始化其他组件
    # ...
    
    logger.info('应用启动完成')

if __name__ == '__main__':
    init_app()
```

### 4. 容器化部署

```yaml
# docker-compose.yml
version: '3'
services:
  app:
    image: myapp:latest
    environment:
      - FAIRY_LOG_LEVEL=INFO
      - FAIRY_LOG_ENABLE_CONSOLE=true
      - FAIRY_LOG_ENABLE_FILE=false  # 容器环境推荐输出到 stdout
    volumes:
      - ./logs:/app/logs  # 如果需要持久化日志
```

---

## 常见问题

### Q1: 为什么看不到 DEBUG 日志？
确保配置的 level 是 DEBUG，并且模块的层级级别没有被覆盖。

### Q2: 如何同时输出到控制台和文件？
设置 `console=True` 和 `file=True`。

### Q3: 如何避免日志文件过大？
使用 `rotation` 和 `retention` 参数控制轮转和保留。

### Q4: 日志中出现重复记录怎么办？
确保只调用一次 `LogManager.configure()`，不要在多个地方重复配置。

### Q5: 如何在包内部使用？
直接使用 `LogManager.get_logger(__name__)`，包内外统一使用同一套日志系统。

---

## 完整示例

见 `scripts/real_world_example.py` 和 `scripts/django_example.py`

