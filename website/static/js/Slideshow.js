var slideshow_tab_picker = document.querySelector('#slideshow_tab_picker')
var selected_tab_id = "tab1"
if (slideshow_tab_picker){
    let tab1 = slideshow_tab_picker.querySelector("#tab1")
    let tab2 = slideshow_tab_picker.querySelector("#tab2")
    let tab3 = slideshow_tab_picker.querySelector("#tab3")
    let tab4 = slideshow_tab_picker.querySelector("#tab4")

    let tabs = [tab1, tab2, tab3, tab4]

    for (let tab of tabs){
        tab.addEventListener('click', function(){            
            
            if (tab.id != selected_tab_id){
                unselected_tab = document.querySelector(`#${selected_tab_id}`)
                unselected_tab.classList.remove('white_bg')
                tab.classList.add('white_bg')

                let selected_slide_id = tab.getAttribute('data-slide_id')
                let unselected_slide_id = unselected_tab.getAttribute('data-slide_id')

                let selected_slide = document.querySelector(`#${selected_slide_id}`)
                let unselected_slide = document.querySelector(`#${unselected_slide_id}`)

                unselected_slide.classList.add('invisible')
                selected_slide.classList.remove('invisible')

                selected_tab_id = tab.id
            }
        })
    }
}


var category_picker = document.querySelector('#category_picker')
var selected_cat_id = "category1"
if (category_picker){
    let category1 = category_picker.querySelector('#category1')
    let category2 = category_picker.querySelector('#category2')
    let category3 = category_picker.querySelector('#category3')
    let category4 = category_picker.querySelector('#category4')

    let cat_elems = [category1, category2, category3, category4]
    for (let cat_elem of cat_elems){
        cat_elem.addEventListener('click', function(){
            if (cat_elem.id != selected_cat_id){
                let unselected_cat = document.querySelector(`#${selected_cat_id}`)
                unselected_cat.classList.remove('selected_btn');
                cat_elem.classList.add('selected_btn')

                let selected_img_elem = cat_elem.querySelector('img');
                let new_selected_img = selected_img_elem.getAttribute('data-inverse_img');
                selected_img_elem.setAttribute('data-inverse_img', selected_img_elem.getAttribute('src')) 
                selected_img_elem.setAttribute('src', new_selected_img)
                
                let unselected_img_elem = unselected_cat.querySelector('img');
                let new_unselected_img = unselected_img_elem.getAttribute('data-inverse_img');
                unselected_img_elem.setAttribute('data-inverse_img', unselected_img_elem.getAttribute('src')) 
                unselected_img_elem.setAttribute('src', new_unselected_img)

                selected_cat_id = cat_elem.id
            }
        })
    }
}