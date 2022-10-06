function szamol() {

var indulo = document.getElementById("select1").value;
var erkezo = document.getElementById("select2").value;

var eredmeny= indulo-erkezo;
    console.log(typeof(eredmeny));

    if(erkezo=indulo){
        alert("buta geci vagy");
    }
    
    else{
        alert(Math.abs(eredmeny));
    }
}