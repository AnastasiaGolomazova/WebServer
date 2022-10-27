import logging
from aiohttp import web
import json
from string import ascii_letters

from decorators import decorator_logging_factory_async

logger = logging.getLogger(__name__)

routes = web.RouteTableDef()


# TODO add data validation (pydantic for example)


@routes.get("/ping")
@decorator_logging_factory_async(logger)
async def check_connection(request: web.Request):
    raise web.HTTPOk(
        text='{"message": "connected"}',
        headers={"content-type": "application/json"},
    )


@routes.get("/v1/oils/all")
@decorator_logging_factory_async(logger)
async def get_v1_oils_all(request: web.Request):
    limit = int(request.query.get("limit"))
    offset = int(request.query.get("offset", 0))
    raise web.HTTPOk(
        text='{"oils": [{"id": 1, "name": "some_name"}]}',
        headers={"content-type": "application/json"},
    )


@routes.get("/v1/oils/id")
@decorator_logging_factory_async(logger)
async def get_v1_oils_id(request: web.Request):
    limit = int(request.query.get("limit"))
    offset = int(request.query.get("offset", 0))
    id = int(request.query.get("id"))
    if id == 500:
        raise web.HTTPNotFound(
            text='{"message": "oil not found"}',
            headers={"content-type": "application/json"},
        )
    raise web.HTTPOk(
        text='{"oils": [{"id": 1, "name": "some_name", "volatility": "some volatility", \
            "aroma_group": "some aroma_group"}]}',
        headers={"content-type": "application/json"},
    )


@routes.get("/v1/oils/effect")
@decorator_logging_factory_async(logger)
async def get_v1_oils_effect(request: web.Request):
    limit = int(request.query.get("limit"))
    offset = int(request.query.get("offset", 0))
    effect = request.query.get("effect")
    raise web.HTTPOk(
        text='{"oils": [{"id": 1, "name": "some_name", "volatility": "some volatility", \
            "aroma_group": "some aroma_group"}]}',
        headers={"content-type": "application/json"},
    )


@routes.get("/v1/effects")
@decorator_logging_factory_async(logger)
async def get_v1_effects(request: web.Request):
    limit = int(request.query.get("limit"))
    offset = int(request.query.get("offset", 0))
    raise web.HTTPOk(
        text='{"effects": ["id": 1, "name": "some_effect"]}',
        headers={"content-type": "application/json"},
    )



@routes.get("/test")
@decorator_logging_factory_async(logger)
async def get_test(request: web.Request):
    print(request.query)
    limit = int(request.query.get("limit"), 0)
    offset = int(request.query.get("offset", 0))

    data = {
        'limit': limit,
        'offset': offset, 
        'value': ascii_letters[offset: limit + offset]
    }
    return web.json_response(data)


@routes.get("/test_json")
@decorator_logging_factory_async(logger)
async def get_test_json(request: web.Request):
    data_json = await request.json()
    print(data_json)
    limit = int(data_json.get("limit"))
    offset = int(data_json.get("offset"))

    data = {
        'limit': limit,
        'offset': offset, 
        'value': ascii_letters[offset: limit + offset]
    }
    return web.json_response(data)


