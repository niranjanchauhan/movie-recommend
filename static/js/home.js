

function movie_system() {

    let s = document.getElementById("system").value;

    if(s == "Top Movies") {
        document.getElementById("top_movies").style.display = "block"; 
        document.getElementById("romantic_movies").style.display = "none";

    } else if(s == "Top Romantic Movies") {
        document.getElementById("top_movies").style.display = "none";
        document.getElementById("romantic_movies").style.display = "block";

    } else {
        document.getElementById("top_movies").style.display = "none";
        document.getElementById("romantic_movies").style.display = "none"; 
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