element.attribute="new value"
document.getElementById("example").src="otherPicture.jpg";
myButton = document.getElementById("myButton"); //searches for and detects the input element from the 'myButton' id
myButton.value = "I'm a changed button"; //changes the value
myButton.type = "text"; //changes the input type from 'button' to 'text'.
var e = document.getElementById("div2"); //Get the element
e.setAttribute("id", "div3"); //Change id to div3
//var e = document.createElement('div'); //Make a div element (we also could have made it with HTML)
//e.createAttribute("id", "myDiv"); //Set the id to "myDiv"