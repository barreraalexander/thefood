// async function fetchRecipes(){
//     const res = await fetch
//     ('/api/fetch_recipes')
//     const data = await res.json();
//     return data
// }

// async function fetchRecipe(model_id){
//     const res = await fetch
//     (`/api/fetch_recipe/${model_id}`) 
//     const data = await res.json();
//     return data
// }

// surprise_btn.addEventListener('click', mod_food)

// function test(){
//     var test_btn = document.querySelector("#surprise_btn");
//     if (test_btn == false){
//         alert('not null')
//     } else {
//         alert('is null')
//     }
// }

var surprise_btn = document.querySelector("#surprise_btn");
if (surprise_btn){
    surprise_btn.addEventListener('click', async function(){
    
        const res = await fetch
        ('/api/fetch_recipe/random')
        const data = await res.json();
        
        // RUN FOOD_CTNR_MOD
        food_ctnr_mod(data);
    
    })
}