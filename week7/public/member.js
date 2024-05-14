// 不使用JS取得資料做渲染，改用樣板引擎的迴圈控制渲染HTML

// async function get_data(){
//     fetch("/get_message").then((res)=>res.json()).then((data)=>{
//         const message=document.querySelector("#mes");
//         const res_name=window.sessionStorage.getItem("username")   //利用sessionStorage紀錄當前登入者的username
//         for(let i=1;i<=data.length;i++){
//             console.log(data);
//             const container=document.createElement("div");
//             container.className="message";
//             const name=document.createElement("span");
//             name.className="message_name";
//             name.innerText=data[data.length-i].name+"：";
//             const content=document.createElement("span");
//             content.className="message_content";
//             content.innerText=data[data.length-i].content;
//             message.appendChild(container);
//             container.appendChild(name);
//             container.appendChild(content);
//             if(res_name===data[data.length-i].username){         //確認當前使用者的username是否跟message的username一樣
//                 const form=document.createElement("form");
//                 form.action="/delete_message";
//                 form.method="post";
//                 const input=document.createElement("input");
//                 input.type="hidden";
//                 input.name="message_id";
//                 input.value=data[data.length-i].id;
//                 const input_user=document.createElement("input");
//                 input_user.type="hidden";
//                 input_user.name="message_username";
//                 input_user.value=data[data.length-i].username;
//                 const input_btn=document.createElement("input");
//                 input_btn.type="submit";
//                 input_btn.value="x";
//                 container.appendChild(form);
//                 form.appendChild(input);
//                 form.appendChild(input_user);
//                 form.appendChild(input_btn);
//             }
//         }
//     })
// }

function check_empty(){
    const response=document.querySelector("#response");
    const form=document.querySelector("#res_form");
    form.addEventListener("submit",(e)=>{
        if(!response.value){
            e.preventDefault()
        }
    })
}
function get_member_name(){
    const container=document.querySelector("#name_container")
    const check_member_form=document.querySelector("#check_member_form");
    const input=document.querySelector("#check_member");
    check_member_form.addEventListener("submit",(e)=>{
        e.preventDefault();
        fetch("/api/member?username="+input.value).then((e)=>e.json()).then((data)=>{
            const name=document.querySelector("#member_name");
            if(data["data"]){
                name.innerText=data["data"]["name"]+"("+data["data"]["username"]+")";}
            else{name.innerText="No Data"}
        })
    })
}

function update_name(){
    const form=document.querySelector("#updata_name_form");
    const input=document.querySelector("#update_name");
    const nname=document.querySelector("#new_name");
    form.addEventListener("submit",(e)=>{
        e.preventDefault();
        const data={"name":input.value}
        fetch("/api/member",{
            method:"PATCH",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(data)
        }).then((e)=>e.json()).then((e)=>{
            if(e.OK){nname.innerText="更新成功"}
            else{nname.innerText="更新失敗"}
        })
    })
}

function main(){
    get_member_name()
    check_empty();
    update_name();
}

main();