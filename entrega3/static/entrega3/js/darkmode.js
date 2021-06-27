$(document).ready(function(){
    $("#night-mode").click(function (){
        var element = document.body;         
        element.classList.toggle("dark"); 
        $('.card').toggleClass("dark");
        $('.modal-content').toggleClass("darkmodal");
    });
});