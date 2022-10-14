import logging
import json
from aiohttp import web
from decorators import decorator_logging_factory_async

logger = logging.getLogger(__name__)


@web.middleware
@decorator_logging_factory_async(logger)
async def middleware(request, handler):
    try:
        return await handler(request)
    except json.JSONDecodeError:
        raise web.HTTPBadRequest(
            text='{"message": "bad-parameters"}',
            headers={"content-type": "application/json"},
        )
    except web.HTTPException as ex:
        raise ex
    # TODO add database error
    except Exception as exc:
        raise web.HTTPException(
            text=f'{{"message": {exc}}}',
            headers={"content-type": "application/json"},
        )
