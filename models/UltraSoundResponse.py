class UltraSoundResponse:
    def __init__(self, success:bool, mode:int, error_message:str, error_code:int):
        self.success = success
        self.mode = mode
        self.error_message = error_message
        self.error_code = error_code
        