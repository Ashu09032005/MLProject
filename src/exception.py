import sys
import logging

def error_message_detail(error, error_detail: sys):
    #error_detail.exc_info() returns a tuple (exc_type, exc_value, exc_traceback)
    _, _, exc_tb = error_detail.exc_info()
    #exc_tb.tb_frame gives the current stack frame at the error point.
    #f_code.co_filename is the filename of the Python script for that frame.
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

# ✅ Example usage
if __name__ == "__main__":
    try:
        # Trigger an error for testing
        result = 1 / 0
    except Exception as e:
        raise CustomException(e, sys)
