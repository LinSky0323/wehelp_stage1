let N=0;

async function getData(url){
    return fetch(url).then((e)=>e.json()).then((e)=>e["data"]["results"]);
}

function render_small_box(mes,pic){
    const container=document.querySelector("#small_container");
    const box=document.createElement("div");
    box.className="small_box";
    const img=document.createElement("img");
    img.className="simg";
    img.src=`https${pic}`;
    const text=document.createElement("p");
    text.className="stext";
    text.innerText=mes;
    container.appendChild(box);
    box.appendChild(img);
    box.appendChild(text);

}

function render_big_box(mes,pic){
    const container=document.querySelector("#big_container");
    const box=document.createElement("div");
    box.className="big_box";
    const img=document.createElement("img");
    img.className="bimg";
    img.src=`https${pic}`;
    const star_img=document.createElement("img");
    star_img.className="star";
    star_img.src="star.png";
    const text=document.createElement("p");
    text.className="btext";
    text.innerText=mes;
    container.appendChild(box);
    box.appendChild(img);
    box.appendChild(text);
    box.appendChild(star_img);

}

async function create_small_box(URL){
    const data=await getData(URL);
    for(let i=0;i<3;i++){
        const img=data[i+N]["filelist"].split("https")[1];
        const text=data[i+N]["stitle"];
        render_small_box(text,img);
    }
    N+=3;
}

async function create_big_box(URL){
    const data=await getData(URL);
    for(let i=0;i<10;i++){
        if(data[i+N]===undefined){
            const button = document.querySelector("#load_more");
            button.disabled=true;
            break;
        }
        const img=data[i+N]["filelist"].split("https")[1];
        const text=data[i+N]["stitle"];
        render_big_box(text,img);
    }
    N+=10;
}

function load_more(){
    const button = document.querySelector("#load_more");
    button.addEventListener("click",(e)=>{
        create_big_box(URL);
    })
}
function click_list(){
    const btn=document.querySelector("#btn");
    const list=document.querySelector("#list");
    const cross=document.querySelector("#cross");
    btn.addEventListener("click",()=>{
        list.classList.toggle("cli");
    })
    cross.addEventListener("click",()=>{
        list.classList.toggle("cli");
    })
}
async function main(URL){
    create_small_box(URL);
    create_big_box(URL);
    load_more(URL);
    click_list();
}

const URL="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
main(URL);

