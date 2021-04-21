// ADD TO VIEW FORM
function submitView ( model_id ){
    let viewed_recipe_id = document.getElementById('view_recipe_id');
    viewed_recipe_id.setAttribute("value", model_id);

    let submit_btn = document.getElementById('view_submit');
    submit_btn.click();
    return true
}


// ADD TO 
like_form = document.querySelector('#like_form')
if (like_form){
    like_form.addEventListener('submit', async function(event){
        event.preventDefault()
        let liked_recipe_id = document.querySelector("#liked_recipe_id").getAttribute("value")
        
        const res = await fetch
        (`/api/add_to_likes`, {
            method:'POST',
            body: JSON.stringify(liked_recipe_id),
            headers: {"Content-type": "application/json; charset=UTF-8"}
        })

        .then(res => res.json)
        .then(json => console.log(json))
        .catch(err => console.log(err))

    })
}

like_button = document.querySelector('#heart_icon')
if (like_button){
    like_button.addEventListener('click', function(){
        like_submit = document.querySelector("#like_submit")
        like_submit.click()
    })
}


// ADD TO CART FORM
atc_form = document.querySelector('#atc_form')
if (atc_form){ 
    atc_form.addEventListener('submit', async function(event){
        event.preventDefault()
        let chosen_recipe_id = document.querySelector("#chosen_recipe_id").getAttribute("value")
        
        const res = await fetch
        (`/api/add_to_cart`, {
            method:'POST',
            body: JSON.stringify(chosen_recipe_id),
            headers: {"Content-type": "application/json; charset=UTF-8"}
        })

        .then(res => res.json)
        .then(json => console.log(json))
        .catch(err => console.log(err))

    })
}


