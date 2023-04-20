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

//Pojawianie się okna komentowania postów

function ShowMeCommentPlace(){
    var comment = document.getElementById("kom")
    comment.setAttribute("style", "display:block;");
}

function ShowMeReplyPlace(){
    var comment = document.getElementById("odp")
    comment.setAttribute("style", "display:block;");
}