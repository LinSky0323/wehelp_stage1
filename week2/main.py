"""week2作業"""
    #第一題

def find_and_print(messages1, current_station):
    """找出離輸入的站點最近的人"""
    #列出捷運線
    mrt=["Songshan",
         "Nanjing Sanmin",
         "Taipei Arena",
         "Nanjing Fuxing",
         "Songjiang Nanjin",
         "Zhongshan",
         "Beimen",
         "Ximen",
         "Xiaonanmen",
         "Chiang Kai-Shek Memorial Hall",
         "Guting",
         "Taipower Building",
         "Gongguan",
         "Wanlong",
         "Jingmei",
         "Dapinglin",
         "Qizhang",
         "Xindian City Hall",
         "Xindian"]
    #列出所有人在哪個站(用數字表示)
    local={}
    for key,value in messages1.items():
        if value.find("Xiaobitan")!=-1:
            local[key]=999
        for j in mrt:
            if value.find(j)!=-1:
                local[key]=mrt.index(j)
    #算距離
    dis=float('inf')
    sta=mrt.index(current_station)
    ans=""
    for key,value in local.items():
        if value==999:
            dist=abs(sta-16)+1
        else:
            dist=abs(sta-value)
        if dist<dis:
            ans=key
            dis=dist
    print(ans)
# your code here
messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian



    #第二題
# your code here, maybe

#可訂人 已訂時間
AlreadyBook={}
def book(consultants1, hour, duration, criteria):
    """找出可預約的人"""
    for i in consultants1:
        if  i["name"] not in AlreadyBook:
            AlreadyBook[i["name"]]=[]
    #排出需求
    require=[]
    for i in consultants1:
        require.append(i[criteria])
    #挑人
    while True:
        th=0
        if criteria=="price":
            th=require.index(min(require))
            require[th]=float("inf")
        elif criteria=="rate":
            th=require.index(max(require))
            require[th]=0
        #看人該時段有沒有預約
        check=True
        for i in range(duration):
            if hour+i in AlreadyBook[consultants1[th]["name"]]:
                check=False
                break
        #沒預約 把時間塞進AlreadyBook 印出可預約人
        if check:
            for i in range(duration):
                AlreadyBook[consultants1[th]["name"]].append(hour+i)
            print(consultants1[th]["name"])
            break
       # 全滿了
        if max(require)==0 or min(require)==float("inf"):
            print("No Service")
            break

# your code here
consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]
book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John

    #第三題
def func(*data):
    """找出middle最少的人名"""
    #把大家的middle排出來
    middle=[]
    for i in data:
        if len(i)<=2:
            middle.append(i[1])
            continue
        middle.append(i[len(i)-2])
    #看誰最少
    count={}
    for i in middle:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    #存最小數
    min_v=float("inf")
    #最小有沒有重複
    repeat=False
    #存最小的key
    min_k=""
    for key,value in count.items():
        if value<min_v:
            min_v=value
            min_k=key
            repeat=False
        elif value==min_v:
            repeat=True
    if repeat:
        print("沒有")
    else:
        print(data[middle.index(min_k)])

# your code here
func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安

    #第四題
def get_number(index):
    """找出數字"""
    print(index*4-index//3*5)
# your code here
get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70


    #第五題
def find(spaces, stat, n):
    """將人塞進有載客且最不浪費空間的車廂"""
    #列出能坐的車廂
    can_drive=[]
    for i in enumerate(stat):
        if stat[i]==1:
            can_drive.append(i)
    #看哪節車廂最適合
    empty=float("inf")
    ans=-1
    for i in can_drive:
        if spaces[i]-n>=0 and spaces[i]-n<empty:
            empty=spaces[i]-n
            ans=i
    print(ans)


# your code here
find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2
