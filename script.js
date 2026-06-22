let estado = [1,2,3,4,5,6,7,8,0];

const tabuleiro = document.getElementById("tabuleiro");


function render() {
    tabuleiro.innerHTML = "";

    estado.forEach((v, i) => {

        const btn = document.createElement("button");

        btn.innerText = v === 0 ? "" : v;

        btn.className = v === 0 ? "vazio" : "tile";

        btn.onclick = () => mover(i);

        tabuleiro.appendChild(btn);
    });
}


function mover(i) {

    const vazio = estado.indexOf(0);

    const adj = {
        0:[1,3],1:[0,2,4],2:[1,5],
        3:[0,4,6],4:[1,3,5,7],5:[2,4,8],
        6:[3,7],7:[4,6,8],8:[5,7]
    };

    if (adj[i].includes(vazio)) {
        [estado[i], estado[vazio]] = [estado[vazio], estado[i]];
        render();
    }
}


function embaralhar() {
    estado = estado.sort(() => Math.random() - 0.5);
    render();
}


function customState() {

    let input = prompt("Digite 123456780");

    if (!input || input.length !== 9) return;

    estado = input.split("").map(Number);

    render();
}


async function resolver() {

    const algoritmo = document.getElementById("algoritmo").value;

    const res = await fetch("/resolver", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({
            estado,
            algoritmo
        })
    });

    const data = await res.json();

    document.getElementById("resultado").innerText =
        JSON.stringify(data.solucao, null, 2);

    document.getElementById("tempo").innerText = data.tempo;
    document.getElementById("custo").innerText = data.custo;
    document.getElementById("visitados").innerText = data.visitados;
}


render();