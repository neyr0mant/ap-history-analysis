import configparser
import time
import os
from base_methods import BaseMethods
from settings import config_dict as config

class StartАnalysis(BaseMethods):
    def __init__(self):
        self.config = config
        print("Analysis type:")
        for num, type_analysis in config.items():
            print(f"{num}   {list(type_analysis.keys())[0]}")
        print("Enter number analysis type")
        num_analysis_enter = self.get_int_for_str(input())
        if not num_analysis_enter:
            self.wait_err_time("Entered not a number!!!")
        if num_analysis_enter not in config:
            self.wait_err_time("Wrong number analysis type!!!")
        self.analysis_type = list(config[num_analysis_enter])[0]
        dict_options = config[num_analysis_enter][self.analysis_type]["options"]
        print("Options:")
        type_analysis_options = {num: params for num, params in enumerate(dict_options, start=1)}
        for num, options in type_analysis_options.items():
            print(f"{num}  {options}")
        print("Enter number options")
        num_params_enter = self.get_int_for_str(input())
        if not num_params_enter:
            self.wait_err_time("Entered not a number!!!")
        if num_params_enter not in type_analysis_options:
            self.wait_err_time("Wrong number options type!!!")
        self.params = dict_options[type_analysis_options[num_params_enter]]
        self.name_options = type_analysis_options[num_params_enter]
        self.start_script()



    def start_script(self):
        if self.analysis_type == "TypeAnalysisDataAPHistory":
            if self.name_options == "download":
                from download_data import DownloadАrh
                year_min_config, year_max_config = self.params["year_min"], self.params["year_max"]
                print(f"Enter the year start with which the archive will be downloaded"
                      f"({year_min_config}-{year_max_config})\n")
                year_min_input = input()
                if year_min_input:
                    year_min_input_int = self.get_int_for_str(year_min_input)
                    if year_min_input_int:
                        if year_min_input_int < year_min_config:
                            self.wait_err_time(f"Download start year cannot be less than {year_min_config}")
                    else:
                        self.wait_err_time("A non-number is entered as the year of the start of the "
                                           "archive download!!!")
                    year_min_config = year_min_input_int
                print( f"Enter the year finish download archive ({year_min_config}-{year_max_config})\n")
                year_max_input = input()
                if year_max_input:
                    year_max_input_int = self.get_int_for_str(year_max_input)
                    if year_max_input_int:
                        if year_max_input_int > year_max_config:
                            self.wait_err_time(f"Download end year cannot be greater than {year_max_config}")
                    else:
                        self.wait_err_time("Not a number is entered as the end year of archive loading!!!")
                    year_max_config = year_max_input_int
                print(f"Start script: analysis type: {self.analysis_type} options: {self.name_options}\n "
                      f"Start download archive {year_max_input} - {year_max_config}")
                DownloadАrh(year_min=year_min_config, year_max=year_max_config)



if __name__ == "__main__":
    StartАnalysis()