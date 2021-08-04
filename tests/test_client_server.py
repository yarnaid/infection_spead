from backend import server
from collections import namedtuple
from backend.server import ModelingSerializer

backend_building = namedtuple('Building', ['id', 'type', 'x', 'y', 'width', 'length', 'angle'])
backend_human = namedtuple('Human', ['id', 'type', 'x', 'y'])
Meta = namedtuple('meta', ['status', 'request_id'])


def create_null_request():  # creating request with meta(state = SUCCESS, request_id = 10)
    Request = namedtuple('request', ['meta'])
    meta = Meta(0, 10)
    request = Request(meta)
    return request


class mock_map:
    def __init__(self, *args):
        self.obj = args
        self.count = 0
        self.map_width = 20
        self.map_length = 20

    def iter_buildings(self):
        return self.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == len(self.obj):
            raise StopIteration
        res = self.obj[self.count]
        self.count += 1
        return res


def test_getting_map():
    # setting up Servicer
    build_1 = backend_building(1, 1, 1, 1, 1, 1, 1)
    build_2 = backend_building(10, 0, 10, 10, 10, 10, 10)
    map_items = mock_map(build_1, build_2)
    servicer = server.ModelingServicer(map_items, None, ModelingSerializer)
    # setting up request
    request = create_null_request()

    # work with server function
    resp = servicer.GetMap(request, context=None)
    assert resp.building[0].id == 1  # Wrong id while yielding map object
    assert resp.building[1].id == 10
    assert resp.meta.request_id == request.meta.request_id  # Wrong returned request id while yielding map object


def test_update_request():
    # setting up servicer
    human_1 = backend_human(1, 1, 1, 1)
    human_2 = backend_human(3, 3, 3, 3)
    humans = [human_2, human_1]
    servicer = server.ModelingServicer(None, humans, ModelingSerializer)
    # send request
    request = create_null_request()
    resp = servicer.GetUpdate(request, context=None)
    assert resp.state[0].coord_x == 3  # Wrong id while yielding human object
    assert resp.state[1].id == 1
    assert resp.meta.request_id == request.meta.request_id  # Wrong returned request id while yielding human
    # object"
