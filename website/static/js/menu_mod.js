var menu_open = false;
heading_div = document.querySelector('#heading_div');
if (heading_div){
    heading_div.addEventListener('click', function (){

        let nav_elem = document.querySelector('#nav_ctnr');
        let dwn_arw = document.querySelector('#aside_down_arrow')
    
        if (menu_open==false){
            nav_elem.classList.toggle("invisible");
            dwn_arw.style.transform = "initial";
            menu_open = true;
        } else if(menu_open==true) {
            nav_elem.classList.toggle("invisible");        
            dwn_arw.style.transform = "rotate(180deg)";
            menu_open = false;
        }
    })
}