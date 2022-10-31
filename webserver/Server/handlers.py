import logging
import string
from aiohttp import web
import json
from string import ascii_letters
from datastorage import DataStorage
import json
import dataBase.remoteDataBaseAdapter as db
import jsonpickle
from http.server import BaseHTTPRequestHandler, HTTPServer
from types import SimpleNamespace
from decorators import decorator_logging_factory_async

logger = logging.getLogger(__name__)

routes = web.RouteTableDef()
dataStorage = DataStorage()

@routes.get("/getRecipe")
@decorator_logging_factory_async(logger)
async def get_recipe(request: web.Request):
    return web.json_response(json.dump(dataStorage.Recipe))



@routes.get("/getEffect")
@decorator_logging_factory_async(logger)
async def get_effect(request: web.Request):
    return web.json_response(json.dump(dataStorage.Effect))


@routes.get("/getPage")
@decorator_logging_factory_async(logger)
async def get_page(request: web.Request):
    id = int(request.query.get("id"))
    res = db.getRequestPage()
    for item in res:
        if item.Id == id:
            raise web.HTTPOk(
            text=item.toJsonText(),
            headers={"Access-Control-Allow-Origin": "*"},
            )         
    raise web.HTTPOk(
            text={},
            headers={"Access-Control-Allow-Origin": "*"},
            ) 


@routes.get("/getPages")
@decorator_logging_factory_async(logger)
async def get_pages(request: web.Request):
    res = db.getRequestPage()
    resJson2 = []
    for item in res:
        resJson = {}
        resJson["id"] = item.Id
        resJson["name"] = item.Name
        resJson2.append(resJson)
    raise web.HTTPOk(
            text=json.dumps(resJson2, ensure_ascii=False),
            headers={"Access-Control-Allow-Origin": "*"},
            )

@routes.get("/getEffectById")
@decorator_logging_factory_async(logger)
async def get_effect_by_id(request: web.Request):
    id = int(request.query.get("id"))
    rez = dataStorage.getEffect(id)
    return web.json_response(json.dump((rez)))




@routes.get("/createRecipe")
@decorator_logging_factory_async(logger)
async def get_test_json(request: web.Request):
    name= request.query.get("name")
    idProfile= int(request.query.get("idProfile"))
    chbx = int(request.query.get("chbx"))
    count= int(request.query.get("count"))
    res = []
    for number in range(count):
        resJson = {}
        oil = request.query.get(f'oil{number+1}')
        oilN = int(request.query.get(f'oilN{number+1}'))
        resJson[oil] = oilN
        res.append(resJson)

    raise web.HTTPOk(
            headers={"Access-Control-Allow-Origin": "*"},
            )





@routes.get("/getOrder")
@decorator_logging_factory_async(logger)
async def get_test_json(request: web.Request):
    name= request.query.get("name")
    surname= request.query.get("surname")
    patronymic= request.query.get("patronymic")
    mail= request.query.get("mail")
    comment = request.query.get("comment")

    raise web.HTTPOk(
            headers={"Access-Control-Allow-Origin": "*"},
            )

@routes.get("/getRecipeById")
@decorator_logging_factory_async(logger)
async def get_test_json(request: web.Request):
    id= int(request.query.get("id"))
    recipe = db.getRecipe(id)
    list = dataStorage.getCombinationEssenseByRecipe(id)
    res = []
    resJson = {}
    resJson["nameRecipe"] = recipe.Name
    res.append(resJson)
    for number in list:
        resJson = {}
        resJson["id"] = number.Id
        resJson["name"] = number.Name
        resJson["quantity"] = number.Quantity
        res.append(resJson)

    raise web.HTTPOk(
            text = json.dumps(res, ensure_ascii=False),
            headers={"Access-Control-Allow-Origin": "*"},
            )


