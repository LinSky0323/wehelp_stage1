function main(){
    const btn=document.querySelector("#btn");
    const list=document.querySelector("#list");
    const cross=document.querySelector("#cross");
    btn.addEventListener("click",()=>{
        list.classList.toggle("cli")
    })
    cross.addEventListener("click",()=>{
        list.classList.toggle("cli")
    })}
    main();