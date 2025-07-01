import sys
from src.logger import logging
from typing import Any

def error_message_details(error,error_detail:Any):
    _,_,exc_tb = error_detail.exc_info()
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
    else:
        file_name="Unknown"
    
    error_message="Error Occurred in python Script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:Any):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

# if __name__=="__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.error("Divide by Zero Error")
#         raise CustomException(e,sys)