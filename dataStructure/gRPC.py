gRPC_status_creator = {'UNDEFINED': 0, 'SUCCESS': 1, 'ERROR': 2}  # Dont know how to do it better
gRPC_human_types = {'NORMAL': 0, 'ILL': 1, 'RECOVERED': 2, 'DEAD': 3}
gRPC_building_types = {'HOUSE':0, 'ROAD':1}


class RequestCounter:  # counter of unique request id
    id = 0

    @staticmethod
    def give_id():
        RequestCounter.id += 1
        return RequestCounter.id
