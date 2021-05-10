import inspect

from exceptions import RequestFormatError

class RequestManager:

    def __init__(self, request):
        self.request = request
    
    def is_valid(self, comparable, secure=False):
        """
        Validate the data request
        :param comparable: dict_keys object
        :param secure: check if attribute request is secure
        :return: True if is valid, if it doesn't raise RequestFormatError
        """

        assert type(comparable) == list, "comparable must be a dict"

        for item in self.request.get_json():
            if item not in comparable:
                raise RequestFormatError("{} not allowed".format(item))
        return True
        
            

