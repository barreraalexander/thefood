function food_ctnr_mod (model) {
    var chosen_recipe_id = document.querySelector('#chosen_recipe_id');
    var liked_recipe_id = document.querySelector('#liked_recipe_id');
    var chosen_recipe_link = document.querySelector('#chosen_recipe_link');
    var chosen_recipe_section = document.querySelector('#index_section4');
    var model_name = document.querySelector('#model_name');
    var model_rating = document.querySelector('#model_rating');
    var model_img_src = document.querySelector('#model_img_src');
    var model_prep_time = document.querySelector('#model_prep_time');
    var model_cook_time = document.querySelector('#model_cook_time');
    var model_total_time = document.querySelector('#model_total_time');
    var model_ings_list = document.querySelector('#model_ings_list');
    var model_steps_list = document.querySelector('#model_steps_list');
    var roll_again_btn = document.querySelector('#roll_again_btn');

    chosen_recipe_id.setAttribute("value", model._id);
    liked_recipe_id.setAttribute("value", model._id);
    chosen_recipe_link.setAttribute("href", model.href);
    let div_style = `background-image:url(${model.img_locs.split("$")[0]})`;
    model_img_src.setAttribute("style", div_style);
    roll_again_btn.setAttribute("onclick", `getKeyword('${model.keyword}')`);
  
    model_name.innerHTML = model.name;
    model_rating.innerHTML = model.rating;
    model_prep_time.innerHTML = 'Prep ('+ model.preptime+')'; 
    model_cook_time.innerHTML = 'Cook   ('+ model.cooktime+')'; 
    model_total_time.innerHTML = 'Total   ('+ model.totaltime+')';

    var ings_split = model.ingredients.split("$");
    var steps_split = model.steps.split("$");
    
    var ing;
    for (ing in ings_split){
        model_ings_list.innerHTML += `<li>${ings_split[ing]}</li>`;
    }
    var step;
    for (step in steps_split){
        model_steps_list.innerHTML += `<div class="ing_step_div">
        <p class="step_num">${parseInt(step)+1}.</p>
        <p class="step_content">${steps_split[step]}</p>
                                       </div>`;
    }
    chosen_recipe_section.classList.remove('invisible');
    window.scrollTo (0, 0);
}


