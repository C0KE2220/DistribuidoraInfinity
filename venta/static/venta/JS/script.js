function descuento(){
    let porc,valor,desc,total;

    valor = document.getElementById("total").innerHTML;
    desc = document.getElementById("desc").innerHTML;
    porc = 0.85;
    
    
    valor = parseInt(valor);

    total = (valor*porc);
    desc = (valor-total);
    document.getElementById("total").innerHTML = ("$"+total);
    document.getElementById("desc").innerHTML = ("$"+desc);
    
}
function valCupon(){

    let cup,text;
    cup = "PRIMERACOMPRA";
    text = document.getElementById("cupon").value;
    text = text.toUpperCase();
    

    if(text == cup){
        document.getElementById("cupon").value = "";
        document.getElementById("mensaje").innerHTML = "Tienes un descuento activo del 15%";
        descuento();

    }else{
        document.getElementById("mensaje").innerHTML = "El cupón ingresado no es válido";
    }
}