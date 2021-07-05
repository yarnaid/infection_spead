gRPC_status_creator = {'SUCCESS': 0, 'ERROR': 1}  # Dont know how to do it better


class RequestCounter:  # counter of unique request id
    id = 0

    @staticmethod
    def give_id():
        RequestCounter.id += 1
        return RequestCounter.id
