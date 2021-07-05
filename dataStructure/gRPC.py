gRPC_status_creator = {'SUCCESS': 0, 'ERROR': 1}


class RequestCounter:
    id = 0

    @staticmethod
    def give_id():
        RequestCounter.id += 1
        return RequestCounter.id
