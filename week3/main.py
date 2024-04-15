"""W3作業"""
#第一題

#引入request、json
from urllib import request
import json
URL1="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
URL2="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
#建立兩個連結的request
with request.urlopen(URL1) as response1:
    data1=json.load(response1)
with request.urlopen(URL2) as response2:
    data2=json.load(response2)
#把兩個request依照"SERIAL_NO"排序成整齊的LIST
s_list=sorted(data1["data"]["results"],key=lambda k: k["SERIAL_NO"] )
m_list=sorted(data2["data"],key=lambda k:k["SERIAL_NO"])
#寫入第一個spot.csv檔
with open ("./spot.csv","w",encoding="utf-8") as file:
    for i in range(data1["data"]["count"]):
        add=m_list[i]["address"].split()[1][0:3]
        jpg=s_list[i]["filelist"].split("https")[1]
        file.write(s_list[i]["stitle"]+","+add+","+s_list[i]["longitude"]+
                   ","+s_list[i]["latitude"]+",https"+jpg+"\n")
#建立物件，key為捷運站，value為景點推到一起
j_list={}
for i in range(data1["data"]["count"]):
    if m_list[i]["MRT"] not in j_list :
        j_list[m_list[i]["MRT"]]=""
    j_list[m_list[i]["MRT"]]+=","+s_list[i]["stitle"]
#寫入第二個mrt.csv檔
with open ("./mrt.csv","w",encoding="utf-8") as file1:
    for key,value in j_list.items():
        file1.write(key+value+"\n")