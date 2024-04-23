function check_agree(){
    const check=document.querySelector("#check_agree");
    const form=document.querySelector("#formlist");
    form.addEventListener("submit",(e)=>{
        if(!check.checked){
            e.preventDefault();
            alert("Please check the checkbox first")
        }
    })
}
function check_number(){
    const snumber=document.querySelector("#snumber");
    const btn=document.querySelector("#nbtn");
    btn.addEventListener("click",()=>{
        let number=parseInt(snumber.value)
        if(isNaN(number) || number<=0){
            alert("Please enter a positive number")
        }
        else{
            window.location.href=`/square/${number}`
        }
    })
    snumber.addEventListener("keydown",(e)=>{
        if(e.key==="Enter"){
            btn.click()
        }
    })
}
function AddEventListener(){
    check_agree();
    check_number();
}

function main(){
    AddEventListener();
}

main()