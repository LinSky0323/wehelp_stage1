async function get_data(){
    fetch("/get_message").then((res)=>res.json()).then((data)=>{
        const message=document.querySelector("#mes");
        const res_name=window.sessionStorage.getItem("username")   //利用sessionStorage紀錄當前登入者的username
        for(let i=1;i<=data.length;i++){
            console.log(data);
            const container=document.createElement("div");
            container.className="message";
            const name=document.createElement("span");
            name.className="message_name";
            name.innerText=data[data.length-i].name+"：";
            const content=document.createElement("span");
            content.className="message_content";
            content.innerText=data[data.length-i].content;
            message.appendChild(container);
            container.appendChild(name);
            container.appendChild(content);
            if(res_name===data[data.length-i].username){         //確認當前使用者的username是否跟message的username一樣
                const form=document.createElement("form");
                form.action="/delete_message";
                form.method="post";
                const input=document.createElement("input");
                input.type="hidden";
                input.name="message_id";
                input.value=data[data.length-i].id;
                const input_user=document.createElement("input");
                input_user.type="hidden";
                input_user.name="message_username";
                input_user.value=data[data.length-i].username;
                const input_btn=document.createElement("input");
                input_btn.type="submit";
                input_btn.value="x";
                container.appendChild(form);
                form.appendChild(input);
                form.appendChild(input_user);
                form.appendChild(input_btn);
            }
        }
    })
}

function check_empty(){
    const response=document.querySelector("#response");
    const form=document.querySelector("#res_form");
    form.addEventListener("submit",(e)=>{
        if(!response.value){
            e.preventDefault()
        }
    })
}

function main(){
    get_data();
    check_empty();
}

main();