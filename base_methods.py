import time

class BaseMethods:


    def __init__(self):
        self.num_for_month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
                              8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

    def get_int_for_str(self, str_in):
        try:
            return int(str_in)
        except:
            return False

    def wait_err_time(self, err_text, wait_time_err=10):
        print(err_text)
        time.sleep(wait_time_err)
        raise Exception(err_text)