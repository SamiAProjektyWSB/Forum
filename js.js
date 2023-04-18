// Pasek nawigacyjny

function HideDaNavbar(){
    var akon = document.getElementById("akon");
    var navbar = document.getElementById("navbar");
    akon.setAttribute("style","display:none;");
    navbar.classList.remove("hide");
}

function ShowDaNavbar(){
    var akon = document.getElementById("akon");
    var navbar = document.getElementById("navbar");
    akon.setAttribute("style","display:block;");
    navbar.classList.add("hide");
}