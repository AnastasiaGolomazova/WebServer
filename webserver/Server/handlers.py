import logging
from aiohttp import web
import json
from string import ascii_letters
from datastorage import DataStorage
import json
import dataBase.remoteDataBaseAdapter as db
from decorators import decorator_logging_factory_async

logger = logging.getLogger(__name__)

routes = web.RouteTableDef()
dataStorage = DataStorage()

@routes.get("/getRecipe")
@decorator_logging_factory_async(logger)
async def get_recipe(request: web.Request):
    return web.json_response(json.dump(dataStorage.Recipe))

@routes.get("/getRecipeById")
@decorator_logging_factory_async(logger)
async def get_recipe_by_id(request: web.Request):
    id = int(request.query.get("id"))
    return web.json_response(json.dump(dataStorage.getRecipe(id)))


@routes.get("/getEffect")
@decorator_logging_factory_async(logger)
async def get_effect(request: web.Request):
    return web.json_response(json.dump(dataStorage.Effect))

@routes.get("/getEffectById")
@decorator_logging_factory_async(logger)
async def get_effect_by_id(request: web.Request):
    id = int(request.query.get("id"))
    rez = dataStorage.getEffect(id)
    return web.json_response(json.dump((rez))

@routes.get("/getPages")
@decorator_logging_factory_async(logger)
async def get_pages(request: web.Request):
    res = db.getRequestPage()
    return web.json_response(json.dump(res))









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


