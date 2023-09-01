let botao = document.querySelector("#botao");
botao.style.background = "yellow";
let estaQuebrado = false;
let contaCliques = 0;

botao.addEventListener("mouseover", e => {
    if(!estaQuebrado); {
        botao.style.background = "green";
        botao.style.color = "white";
    }
});

botao.addEventListener("mouseout", e => {
    if(!estaQuebrado);
        botao.style.background = "yellow";
});

botao.addEventListener("click", e => {

    contaCliques++; //contaCliques = contaCliques + 1;
    
    if(contaCliques >= 10) {
        botao.style.background = "red";
        botao.innerHTML = "quebrei";
        estaQuebrado = true;
    }
});
