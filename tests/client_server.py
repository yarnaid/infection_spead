import unittest
from backend import server
from collections import namedtuple

backend_building = namedtuple('Building', ['id', 'type', 'x', 'y', 'width', 'length', 'angle'])
backend_human = namedtuple('Human', ['id', 'type', 'x', 'y'])
Meta = namedtuple('meta', ['status', 'request_id'])


class ServerModelingServicer(unittest.TestCase):
    @staticmethod
    def create_null_request():  # creating request with meta(state = SUCCESS, request_id = 10)
        Request = namedtuple('request', ['meta'])
        meta = Meta(0, 10)
        request = Request(meta)
        return request

    def test_getting_map(self):
        # setting up Servicer
        build_1 = backend_building(1, 1, 1, 1, 1, 1, 1)
        build_2 = backend_building(10, 10, 10, 10, 10, 10, 10)
        map_items = [build_1, build_2]
        servicer = server.ModelingServicer(map_items, None)
        # setting up request
        request = ServerModelingServicer.create_null_request()

        # work with server function
        resp = servicer.GetMap(request, context=None)
        result = []
        for _, elem in enumerate(resp):
            result.append(elem)
        msg = "Wrong id while yielding map object"
        self.assertEqual(result[0].building.id, 1, msg=msg)
        self.assertEqual(result[1].building.id, 10, msg=msg)
        msg = "Wrong returned request id while yielding map object"
        self.assertEqual(result[1].meta.request_id, request.meta.request_id, msg=msg)

    def test_update_request(self):
        # setting up servicer
        human_1 = backend_human(1, 1, 1, 1)
        human_2 = backend_human(3, 3, 3, 3)
        humans = [human_2, human_1]
        servicer = server.ModelingServicer(None, humans)
        # send request
        request = ServerModelingServicer.create_null_request()
        resp = servicer.GetUpdate(request, context=None)
        result = []
        # study result
        for _, elem in enumerate(resp):
            result.append(elem)
        msg = "Wrong id while yielding human object"
        self.assertEqual(result[0].state.coord_x, 3, msg=msg)
        self.assertEqual(result[1].state.id, 1, msg=msg)
        msg = "Wrong returned request id while yielding human object"
        self.assertEqual(result[1].meta.request_id, request.meta.request_id, msg=msg)
