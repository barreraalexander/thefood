// var ingredient_ctnrs = document.querySelectorAll('.ingredients_ctnr')
// if (ingredient_ctnrs){
//     for (let ctnr of ingredient_ctnrs){
//         let list_items =  ctnr.querySelectorAll('.ingredients_list')
//         for (let item of list_items){
//             console.log(item)
//             item.classList.add('dissolver')
//             // item.style = "position:absolute;"
//             // item.style = "opacity:0;position:absolute;"
//         }
//     }
// }


var ing_triangle = document.querySelectorAll('.ing_triangle')
if (ing_triangle){
    for (let tri of ing_triangle){
        tri.addEventListener('click', function(){
            let ingredients_list_id = "ingredients"+tri.getAttribute("data-loop_index")
            let ing_list_elem = document.querySelector(`#${ingredients_list_id}`)
            console.log(ing_list_elem)
            if (tri.getAttribute("data-is_open")==0){
                tri.style = "transform:rotate(0deg)"
                tri.setAttribute("data-is_open", 1)
                ing_list_elem.classList.remove('invisible')
            } else {
                tri.style = "transform:rotate(270deg)"
                tri.setAttribute("data-is_open", 0)
                ing_list_elem.classList.add('invisible')
            }
        })
    }
}