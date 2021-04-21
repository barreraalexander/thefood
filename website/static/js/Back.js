var back_div = document.querySelector("#back_div")
if (back_div){
    back_div.addEventListener("click", function(){
        window.history.back();
    })
}