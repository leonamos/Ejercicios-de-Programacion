
console.log("Hola mundo")

function sus(numero){
    let nutotal = 0
    let total = 0
    for (let i = 0; i < numero; i++){
        
        nutotal = 0
        total = total + i
        console.log(i + "+" + nutotal + "=" + total)

        
    }
    console.log("El total es " + total)
}

sus(10)


function numeroAleatorio(numero){
    let aleatorio = Math.random() * numero 
    console.log("numero aleatorio" + aleatorio)

    let aleatorio2 = Math.random() * numero 
    console.log("numero aleatorio" + aleatorio2)
    aleatorio2 = Math.floor(aleatorio2)
    aleatorio2 = Math.round(aleatorio2)
    console.log("numero aleatorio con floor" + aleatorio2)
    console.log(aleatorio2)
}

numeroAleatorio(10)


function tablaMultiplicar(){


}