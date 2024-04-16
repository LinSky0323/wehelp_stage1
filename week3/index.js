let N=0;

async function getData(url){
    return fetch(url).then((e)=>e.json()).then((e)=>e["data"]["results"])
}

function render_small_box(mes,pic){
    const container=document.querySelector("#small_container")
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
    const container=document.querySelector("#big_container")
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

async function main(URL){
    const data=await getData(URL);
    for(let i=0;i<3;i++){
        const img=data[i+N]["filelist"].split("https")[1];
        const text=data[i+N]["stitle"];
        render_small_box(text,img)
        N++;
    }
    for (let i=0;i<10;i++){
        const img=data[i+N]["filelist"].split("https")[1];
        const text=data[i+N]["stitle"];
        render_big_box(text,img);
        N++
    }
}

const URL="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
main(URL)

