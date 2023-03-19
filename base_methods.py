import time

class BaseMethods:

    def get_int_for_str(self, str_in):
        try:
            return int(str_in)
        except:
            return False

    def wait_err_time(self, err_text, wait_time_err=10):
        print(err_text)
        time.sleep(wait_time_err)
        raise Exception(err_text)