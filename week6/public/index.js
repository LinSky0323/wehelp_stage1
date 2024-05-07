function check_signup_empty(){
    const form=document.querySelector("#signup_form");
    const name=document.querySelector("#signup_name");
    const acount=document.querySelector("#signup_acount");
    const password=document.querySelector("#signup_password");
    form.addEventListener("submit",(e)=>{
        if(!name.value || !acount.value || !password.value){
            e.preventDefault();
        }
    })
}
function check_signin_empty(){
    const form=document.querySelector("#signin_form");
    const acount=document.querySelector("#signin_acount");
    const password=document.querySelector("#signin_password");
    form.addEventListener("submit",(e)=>{
        if(!acount.value || !password.value){
            e.preventDefault();
        }
    })
}

function main(){
    check_signin_empty();
    check_signup_empty();
}

main();