import pytest
from backend import server
from collections import namedtuple
backend_building = namedtuple('Building', ['id', 'type', 'x', 'y', 'width', 'length', 'angle'])
backend_human = namedtuple('Human', ['id', 'type', 'x', 'y'])
Meta = namedtuple('meta', ['status', 'request_id'])


def create_null_request():  # creating request with meta(state = SUCCESS, request_id = 10)
    Request = namedtuple('request', ['meta'])
    meta = Meta(0, 10)
    request = Request(meta)
    return request


def test_getting_map():
    # setting up Servicer
    build_1 = backend_building(1, 1, 1, 1, 1, 1, 1)
    build_2 = backend_building(10, 0, 10, 10, 10, 10, 10)
    map_items = [build_1, build_2]
    servicer = server.ModelingServicer(map_items, None)
    # setting up request
    request = create_null_request()

    # work with server function
    resp = servicer.GetMap(request, context=None)
    result = []
    for elem in resp:
        result.append(elem)
    assert result[0].building.base.id == 1  # Wrong id while yielding map object
    assert result[1].building.base.id == 10
    assert result[1].meta.request_id == request.meta.request_id  # Wrong returned request id while yielding map object


def test_update_request():
    # setting up servicer
    human_1 = backend_human(1, 1, 1, 1)
    human_2 = backend_human(3, 3, 3, 3)
    humans = [human_2, human_1]
    servicer = server.ModelingServicer(None, humans)
    # send request
    request = create_null_request()
    resp = servicer.GetUpdate(request, context=None)
    result = []
    # study result
    for elem in resp:
        result.append(elem)
    assert result[0].state.base.coord_x == 3  # Wrong id while yielding human object
    assert result[1].state.base.id == 1
    assert result[1].meta.request_id == request.meta.request_id  # Wrong returned request id while yielding human object"
