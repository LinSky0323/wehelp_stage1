//第一題
function findAndPrint(messages, currentStation){
    const mrt=["Songshan","Nanjing Sanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjin","Zhongshan","Beimen","Ximen","Xiaonanmen","Chiang Kai-Shek Memorial Hall","Guting","Taipower Building","Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xindian City Hall","Xindian"]
    //找出每個人的位置
    const where={};            
    for(let key in messages){   
        if(messages[key].includes("Xiaobitan"))where[key]=999;
        for(let i=0;i<mrt.length;i++){
            if(messages[key].includes(mrt[i])){
                where[key]=i
            }
        }
    }
    //找出傳入的位置
    const station=mrt.indexOf(currentStation);
    //比較遠近
    let min=Infinity;
    let ans="";
    for(let key in where){
        let dis=0;
        if(where[key]===999){
            dis=(Math.abs(16-station)+1);
        }
        else{
            dis=Math.abs(where[key]-station);
        }
        if(dis<min){
            min=dis;
            ans=key;
        }
    }
    console.log(ans)
    // your code here
    }
 const messages={
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Leslie":"I'm at home near Xiaobitan station.",
    "Vivian":"I'm at Xindian station waiting for you."
    };
findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian


//第二題

//看誰幾點已有預約
const table={};

function book(consultants, hour, duration, criteria){
    //把有誰加進可預約table
    for(let i of consultants){
        if(!table.hasOwnProperty(i.name))table[i.name]=[]
    }
  
    //排列要判斷的條件
    let th=[];
    for(let i=0;i<consultants.length;i++){
        th.push(consultants[i][criteria])
    }
    
    //開始找
    while(true){
        //先用第幾個人(want)去找
        let like=0;
        if(criteria=="price"){
            like=Math.min(...th);
        }
        else if(criteria=="rate"){
            like=Math.max(...th);
        }
        let want=th.findIndex((i)=>i==like);
        if(criteria=="price"){
            th[want]=Infinity;
        }
        else if(criteria=="rate"){
            th[want]=0;
        }
        
        //看看want的人那個時間點有沒有已經預約
        let check=true;
        for(let i=0;i<duration;i++){
            if(table[consultants[want].name].find((e)=>e==hour+i)!=undefined){
                check=false;
            }
            
        }
        if(check==true){
            for(let i=0;i<duration;i++){
                table[consultants[want].name].push(hour+i)
            }
            console.log(consultants[want].name);
            break;
        }
        //全找完都沒空
        if(th.find((e)=>e<Infinity)==undefined || th.find((e)=>e>0)==undefined){
            console.log("No Service");
            break;}
    
    // your code here
    }
    }
  
    const consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
    ];
    book(consultants, 15, 1, "price"); // Jenny
    book(consultants, 11, 2, "price"); // Jenny
    book(consultants, 10, 2, "price"); // John
    book(consultants, 20, 2, "rate"); // John
    book(consultants, 11, 1, "rate"); // Bob
    book(consultants, 11, 2, "rate"); // No Service
    book(consultants, 14, 3, "price"); // John


//第三題

function func(...data){
    //把大家的middle name按順序排出
    let middle=[];
    for(let i of data){
        if(i.length==2)middle.push(i[1]);
        else{middle.push(i[i.length-2])};
    }
    //數出現次數放進object
    const count={};
    for(let i of middle){
        if(!count.hasOwnProperty(i)){
            count[i]=1;
        }
        else{count[i]+=1}
    }
    //最小數字
    const min=Math.min(...Object.values(count));
    const keys=[];
    for (let key in count){
        if(count[key]==min){
            keys.push(key)
        }
    }
    //最小不只一個就回沒有
    if(keys.length>1){
        console.log("沒有");
        return 0;
    }
    console.log(data[middle.findIndex((e)=>e==keys[0])])
    
    
    
    
    // your code here
    }
    func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
    func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
    func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
    func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安

//第四題

function getNumber(index){
    let ans=(index*4)-(Math.floor(index/3)*5);
    console.log(ans)
    }
    getNumber(1); // print 4
    getNumber(5); // print 15
    getNumber(10); // print 25
    getNumber(30); // print 70


//第五題

function find(spaces, stat, n){
    //找出所有能做的車廂的index
    const canDrive=[];
    for(let i=0;i<stat.length;i++){
        if(stat[i]==1)canDrive.push(i);
    }
    //確認車廂做的下，而且浪費最少空間
    let ans=-1;
    let min=Infinity;
    for(let i of canDrive){
        let A=spaces[i]-n;
        if(A>=0&&A<min){
            min=A;
            ans=i;
        }
    }
    console.log(ans)
    // your code here
    }
    find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5
    find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
    find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2