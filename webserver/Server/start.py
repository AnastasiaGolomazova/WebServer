import os
import logging
from aiohttp import web
from handlers import routes
from middleware import middleware

import dataBase.remoteDataBaseAdapter as db

from decorators import decorator_logging_factory


log_filename = os.path.join(os.path.dirname(__file__), "debug.log")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s:%(message)s",
    handlers=[
        logging.FileHandler(log_filename, mode="w"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


@decorator_logging_factory(logger)
def get_application():
    app = web.Application(middlewares=[middleware])
    app.add_routes(routes)
    return app


def main():
    logger.info("Program started")
    db.getRequest()
    app = get_application()
    web.run_app(app, port=8080)


if __name__ == "__main__":
    main()
