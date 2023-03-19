# coding=utf-8
import requests
import openpyxl
import os
import pylab
import json
# html_data_title = "https://www.ncei.noaa.gov/data/global-marine/archive/"
#
# list_name_arh = []
# for line in open(r"C:\Projects Python\задачи с code_forces\1.txt"):
#     list_name_arh.append(line.split("href=")[1].split(">")[0])
#
# list_name_arh = [i.replace('"', '') for i in list_name_arh]
# list_name_arh = [i for i in list_name_arh if int(i.split(".")[0][:4]) >= 1800]
#
# def get_link(name_arh):
#     return f"https://www.ncei.noaa.gov/data/global-marine/archive/{name_arh}"
#
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
#
# import tarfile
#
# for arh in os.listdir("data_pressure"):
#     path_tar = os.path.join("data_pressure", arh)
#     year = arh.split(".")[0]
#     path = os.path.join("data_cvs", year)
#     path_dir = os.path.join("data_cvs", year)
#     if not os.path.exists(path_dir):
#         os.mkdir(os.path.join("data_cvs", year))
#         with tarfile.open(path_tar) as tar:
#             tar.extractall(path=path)
#
# data_parse = {}
# if os.path.exists("data_parse.txt"):
#     with open("data_parse.txt", "r")as file:
#         read = file.read()
#         data_parse = json.loads(read)
#
# def get_float_data(data):
#     try:
#         data_float = float(data)
#         return data_float
#     except:
#         return False
#
# def get_distance(lat1, lon1, lat2, lon2):
#     import math
#
#     def to_radians(degrees):
#         return degrees * math.pi / 180
#     r = 6371  # Радиус Земли в километрах
#
#     # Переводим градусы в радианы
#     lat1 = to_radians(lat1)
#     lon1 = to_radians(lon1)
#     lat2 = to_radians(lat2)
#     lon2 = to_radians(lon2)
#
#     # Вычисляем разницу широт и долгот
#     delta_lat = lat2 - lat1
#     delta_lon = lon2 - lon1
#
#     # Вычисляем расстояние по формуле гаверсинуса
#     a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
#     return r * c
#
# for name_dir in os.listdir("data_cvs_test"):
#     year = name_dir[:4]
#     if year in data_parse.keys():
#         continue
#     else:
#         for name_file in os.listdir(os.path.join("data_cvs_test", name_dir)):
#             path = os.path.join("data_cvs_test", name_dir, name_file)
#             with open(path) as file:
#                 for idx, line in enumerate(file):
#                      for idx, val in enumerate(line.split(",")):
#                          val = val.replace('"', "")
#                          val = get_float_data(val)
#                          if val:
#                              if 600 < val < 1300:
#                                  if data_parse.get(year):
#                                      data_parse[year] = (data_parse.get(year) + val)/2
#                                  else:
#                                      data_parse[year] = val
#
#
# def get_grapths(data_parse):
#     pylab.plt.figure(figsize=(70, 35))
#     pylab.suptitle(f" Зависимость давления по годам", fontweight="bold", fontsize=50)
#     pylab.plt.rcParams['font.size'] = 28
#     bbox_properties = dict(
#         boxstyle="square, pad=0.1",
#         ec="k",
#         fc="w",
#         ls="-",
#         lw=2
#     )
#     x = [int(i) for i in data_parse.keys()]
#     y = [float(i) for i in data_parse.values()]
#     pylab.plot(x, y)
#     pylab.grid(True)
#     pylab.xlabel("Годы", fontsize=28)
#     pylab.ylabel(f"Давление, Па")
#     pylab.savefig("График.jpg")
#
# with open("data_parse.txt", "w")as file:
#     file.write(json.dumps(data_parse, ensure_ascii=False))

year_for_num = {}
str_y = "January, February, March, April, May, June, July, August, September, October, November, December"
for idx, name in enumerate(str_y.split(","), start=1):
    print(name.replace(" ", ""))
    manths = int()
    year_for_num.update({name.replace(" ", ""):idx})
print(year_for_num)
