const numbers = [1];

let txt = "";
let txts = ("t\n"); //it gos
let txtss = (""+1); //it gos 11111111111...
let txtsss = (0); //it gos 1 then 2 then 3 then 4 you get the point

function times(no) {
	for(var i = 0; i<no; i++) {
    	document.getElementById("demos").innerHTML = (txts += (txtsss += 1)+"\n")
    }
}

setInterval(function () {
	numbers.forEach(myFunction);
    //document.getElementById("demos").innerHTML = (txts += (txtsss += 1)+"\n")
    times(1)
}, 1000);


function myFunction(value) {
  txt += value +"h"+ "<br>"; 
}