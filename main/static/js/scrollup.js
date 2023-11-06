var mybutton = document.getElementById("id_scroll_up");
mybutton.classList.add("bi" ,"bi-arrow-up-circle-fill","text-black" ,"fs-1");
window.onscroll = function () { scrollFunction() };
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}
document.getElementById("id_scroll_up").addEventListener("click", function(){
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
})

