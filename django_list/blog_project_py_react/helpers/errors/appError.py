class AppError(Exception):
    def __init__(self,status,message='',data=None,errors=None):
        self.status = status
        self.message = message
        self.data = data
        self.errors = errors if errors is not None else {}

    def to_response(self):
        return {
        "isSuccess": False,
        "message": self.message,
        "data": self.data,
        "errors": self.errors,
    }, self.status