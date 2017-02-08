$(document).ready(function(){
    $.get("#Navigation.html", funciton(data) {
        $("#header").html(data);
    });
});