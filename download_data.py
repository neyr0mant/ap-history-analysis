import os
import requests
import shutil
from bs4 import BeautifulSoup
from start_analysis import StartАnalysis
from progress.bar import IncrementalBar
import tarfile

class DownloadАrh(StartАnalysis):

    def __init__(self, year_min: int = 1620, year_max: int = 2023, download_scr: bool = True, unpack_scr: bool = True):
        self.num_for_month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
                             8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
        self.year_min = year_min
        self.year_max = year_max
        self.list_year = range(self.year_min, self.year_max + 1)
        self.path_data_download = "download_src_data"
        self.path_data_unpack = "unpack_src_data"
        if not os.path.exists(self.path_data_download):
            os.mkdir(self.path_data_download)
        if not os.path.exists(self.path_data_unpack):
            os.mkdir(self.path_data_unpack)
        # if download_scr:
        #     self.download_data()
        #     print(f"Download {self.year_min} - {self.year_max} complete")
        if unpack_scr:
            self.unpack_data()
            print(f"Unpack {self.year_min} - {self.year_max} complete")

    @staticmethod
    def get_soup_data(link):
        response = requests.get(link).content
        if BeautifulSoup(response, "lxml").title:
            return BeautifulSoup(response, "lxml").title.text
        else:
            return response

    def download_data(self):
        err_download = {}
        count_err = 0
        for year in self.list_year:
            path_year = os.path.join(self.path_data_download, str(year))
            if os.path.exists(path_year):
                shutil.rmtree(path_year)
            os.mkdir(path_year)
            bar_month = IncrementalBar(f'Year {year}', max=len(self.num_for_month.keys()))
            for month_int, month_name in self.num_for_month.items():
                if month_int <= 9:
                    year_month_arh = f"{year}0{month_int}.tar.gz"
                else:
                    year_month_arh = f"{year}{month_int}.tar.gz"
                link_data = f"https://www.ncei.noaa.gov/data/global-marine/archive/{year_month_arh}"
                data = self.get_soup_data(link_data)
                bar_month.next()
                if isinstance(data, str):
                    count_err += 1
                    err_download.update({year_month_arh: data})
                else:
                    with open(os.path.join(path_year, f"{month_int}_{month_name}.tar.gz"), 'wb') as file:
                        file.write(data)
            bar_month.finish()
            print(f"Year {year} uploaded, errors: {count_err}")
            if count_err == 12:
                os.rmdir(path_year)
            count_err = 0
        if err_download:
            with open("log_err_download.txt", "w+") as file:
                file.write(f"###########    Download errors {self.year_min} - {self.year_max}    ###########\n")
                for name_arh, err in err_download.items():
                    file.write(f"{name_arh}: {err}\n")

    def unpack_data(self):
        unpack_err = {}
        for year in self.list_year:
            year = str(year)
            path_year = os.path.join(self.path_data_unpack, year)
            if os.path.exists(path_year):
                shutil.rmtree(path_year)
            path_data_src_year = os.path.join(self.path_data_download, year)
            if not os.path.exists(path_data_src_year):
                unpack_err.update({"Path": path_data_src_year})
            else:
                os.mkdir(path_year)
                for arh_months in os.listdir(path_data_src_year):
                    month = arh_months.split(".")[0]
                    path_data_unpack_month = os.path.join(self.path_data_unpack, year, month)
                    os.mkdir(path_data_unpack_month)
                    path_data_scr_month = os.path.join(path_data_src_year, arh_months)
                    with tarfile.open(path_data_scr_month) as tar:
                        tar.extractall(path=path_data_unpack_month)
        if unpack_err:
            with open("log_err_unpack.txt", "w+") as file:
                file.write(f"###########    Unpack errors {self.year_min} - {self.year_max}    ###########\n")
                for name_arh, err in unpack_err.items():
                    file.write(f"{name_arh}: {err}\n")



    # def get_list_link_arh(self, year_min, year_max):
    #     html_data_title = "https://www.ncei.noaa.gov/data/global-marine/archive/"
    #     html = requests.get(html_data_title).content
    #     list_name_arh = []
    #     soup_obj = BeautifulSoup(html, "lxml")
    #     for tr in soup_obj.table.findAll("tr"):
    #         if tr.td:
    #             href = tr.td.a.get("href")
    #             if href:
    #                 name_arh_int = self.get_int_for_str(href.split(".")[0])
    #                 if name_arh_int:
    #                     cur_year = int(str(name_arh_int)[:4])
    #                     if year_min <= cur_year <= year_max:
    #                         list_name_arh.append(href)
    #     return [f"https://www.ncei.noaa.gov/data/global-marine/archive/{name_arh}" for name_arh in list_name_arh]


# import tarfile
# for name_arh in list_name_arh:
#     path_dir = os.path.join("data_pressure", name_arh)
#     if not os.path.exists(path_dir):
#         data = requests.get(get_link(name_arh)).content
#         with open(path_dir, 'wb') as file_:
#                 file_.write(data)
#         path_tar = os.path.join("data_pressure", name_arh)
#         year = name_arh.split(".")[0]
#         path_cvs = os.path.join("data_cvs", year)
#         os.mkdir(os.path.join("data_cvs", year))
#         with tarfile.open(path_tar) as tar:
#             tar.extractall(path=path_cvs)

DownloadАrh(1700, 1800)