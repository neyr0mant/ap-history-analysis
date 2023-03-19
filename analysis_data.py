from download_data import DownloadAndUnpackАrh
import os
import json

class AnalysisAP(DownloadAndUnpackАrh):
    print()

    def __init__(self, path_data_unpack = "unpack_src_data"):
        if not os.path.exists(path_data_unpack):
            self.wait_err_time(f"Not found folder {path_data_unpack}")
        self.path_data_unpack = path_data_unpack
        self.assert_dir(self.path_data_unpack, create=False)
        self.list_year_analysis = os.listdir(path_data_unpack)
        for year in os.listdir(self.path_data_unpack):
            self.path_dir_months = os.path.join(self.path_data_unpack, year)
            for months in os.listdir(self.path_dir_months):
                path_year_months = os.path.join(self.path_dir_months, months)
                self.list_files_path = [os.path.join(path_year_months, i) for i in
                                   os.listdir(path_year_months) if ".csv" in i]
                print()
            for csv in self.list_files_path:
                res = self.parser_cvs(csv)
                if res.get('SEA_LVL_PRES'):
                    print()


    def parser_cvs(self, path):
        dict_out = {}
        with open(path, 'r') as file:
            list_line = [i.replace('"', '').replace("\n", "").split(",") for i in file]
            if not list_line:
                self.wait_err_time(f"Not data in file {path}")
            len_desc_line, list_key = len(list_line[0]), list_line[0]
            for line_data in list_line[1:]:
                if len(line_data) != len_desc_line:
                    self.wait_err_time(f"Cannot be parsed len(line_data) != len_desc_line!!!")
                idx = 0
                while idx < len_desc_line:
                    cur_key = list_key[idx]
                    cur_data = dict_out.get(cur_key)
                    if cur_data:
                        dict_out[cur_key].append(line_data[idx])
                    else:
                        dict_out[cur_key] = [line_data[idx]]
                    idx += 1
        return dict_out




    def get_distance(self, lat1, lon1, lat2, lon2):
        import math
        def to_radians(degrees):
            return degrees * math.pi / 180
        r = 6371  # Earth radius in kilometers
        # Converting degrees to radians
        lat1 = to_radians(lat1)
        lon1 = to_radians(lon1)
        lat2 = to_radians(lat2)
        lon2 = to_radians(lon2)
        # Calculate the difference between latitudes and longitudes
        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1
        # Calculate the distance using the haversine formula
        a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return r * c

AnalysisAP()