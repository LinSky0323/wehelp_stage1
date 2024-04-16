"""W3作業"""
# #第一題

# #引入request、json
from urllib import request
import json
import bs4
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

# 第二題
with open("./article.csv","w",encoding="utf-8") as file2:
    def get_data(url3):
        """連線取得DATA"""
    #建立request物件，附加request header屬性
        req=request.Request(url3,headers={
            "User-Agent":"""Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36""",
            "cookie":"over18=1"})
        with request.urlopen(req) as response3:
            data3=response3.read().decode("utf-8")
        #喝湯
        root=bs4.BeautifulSoup(data3,"html.parser")
        #找到class=title的div 裡面的string是要找的標題
        titles=root.find_all("div",class_="title")
        #在頁面裡點進每個標題
        for j in titles:
            if j.a is not None:
                file2.write(j.a.string+",")
                #對點進的內容網頁在建立一個Request
                req_content=request.Request("https://www.ptt.cc"+j.a["href"],headers={"User-Agent":
                """Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36""",
                "cookie":"over18=1"})
                with request.urlopen(req_content) as response:
                    data=response.read().decode("utf-8")
                root2=bs4.BeautifulSoup(data,"html.parser")
                #算like的數量
                like=len(root2.find_all("span",string="推 "))
                #算dislike的數量
                dislike=len(root2.find_all("span",string="噓 "))
                file2.write(str(like)+",")
                file2.write(str(dislike)+",")
                #找到內文為時間的span
                times=root2.find("span",string="時間")
                if times is None:
                    file2.write(" "+"\n")
                else:
                    #用函數找到下一個span(就是顯示時間的)
                    file2.write(times.find_next_sibling().string+"\n")
        change_page=root.find("a",string="‹ 上頁")
        return change_page["href"]
    URLPTT="https://www.ptt.cc/bbs/Lottery/index.html"
    COUNT=0
    #跑三頁
    while COUNT<3 :
        URLPTT="https://www.ptt.cc"+get_data(URLPTT)
        COUNT+=1
