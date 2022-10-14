from http import HTTPStatus


async def test_ping(cli):
    handler = "/ping"
    assert (await cli.get(handler)).status == HTTPStatus.OK


async def test_get_v1_oils_all(cli):
    handler = "/v1/oils/all"
    assert (
        await cli.get(
            handler,
            params={"limit": 10},
        )
    ).status == HTTPStatus.OK


async def test_get_v1_oils_id(cli):
    handler = "/v1/oils/id"
    assert (
        await cli.get(
            handler,
            params={"limit": 10, "id": 57},
        )
    ).status == HTTPStatus.OK

    assert (
        await cli.get(
            handler,
            params={"limit": 10, "id": 500},
        )
    ).status == HTTPStatus.NOT_FOUND


async def test_get_v1_oils_effect(cli):
    handler = "/v1/oils/effect"
    assert (
        await cli.get(handler, params={"limit": 10, "effect": "some effect"})
    ).status == HTTPStatus.OK


async def test_get_v1_effects(cli):
    handler = "/v1/effects"
    assert (await cli.get(handler, params={"limit": 10})).status == HTTPStatus.OK
