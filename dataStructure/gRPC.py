gRPC_status_creator = {'SUCCESS': 1, 'ERROR': 0}


class RequestCounter:
    id = 0

    @staticmethod
    def give_id():
        RequestCounter.id += 1
        return RequestCounter.id
