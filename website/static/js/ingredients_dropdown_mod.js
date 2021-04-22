var ingredient_ctnrs = document.querySelectorAll('.ingredients_ctnr')
if (ingredient_ctnrs){
    for (let ctnr of ingredient_ctnrs){
        let list_items =  ctnr.querySelectorAll('.ingredients_list')
        for (let item of list_items){
            console.log(item)
            item.classList.add('dissolver')
            // item.style = "opacity:0;position:absolute;"
        }
    }
}