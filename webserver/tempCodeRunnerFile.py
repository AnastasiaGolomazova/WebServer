def get_application():
    app = web.Application(middlewares=[middleware])
    app.add_routes(routes)
    return app


def main():
    logger.info("Program started")
    app = get_application()
    web.run_app(app, port=8080)


if __name__ 