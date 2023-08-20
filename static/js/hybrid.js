

function movie_system() {

    let s = document.getElementById("system").value;

    if(s == "1, Avatar") {
        document.getElementById("p1").style.display = "block"; 
        document.getElementById("p2").style.display = "none";
        document.getElementById("p3").style.display = "none";
        document.getElementById("p4").style.display = "none";

    } else if(s == "500, Avatar") {
        document.getElementById("p1").style.display = "none"; 
        document.getElementById("p2").style.display = "block";
        document.getElementById("p3").style.display = "none";
        document.getElementById("p4").style.display = "none";

    } else if(s == "500, Avatar") {
        document.getElementById("p1").style.display = "none"; 
        document.getElementById("p2").style.display = "none";
        document.getElementById("p3").style.display = "block";
        document.getElementById("p4").style.display = "none";
        
    } else if(s == "500, Avatar") {
        document.getElementById("p1").style.display = "none"; 
        document.getElementById("p2").style.display = "none";
        document.getElementById("p3").style.display = "none";
        document.getElementById("p4").style.display = "block";

    } else {
        document.getElementById("p1").style.display = "none"; 
        document.getElementById("p2").style.display = "none";
        document.getElementById("p3").style.display = "none";
        document.getElementById("p4").style.display = "none";
    }

    

}



function logout(event) {
    let val = confirm('Do you want to logout?');

    if (val == true) {
        return true;
    } else {
        event.stopImmediatePropagation();
        event.preventDefault();
        return false;
    }
}