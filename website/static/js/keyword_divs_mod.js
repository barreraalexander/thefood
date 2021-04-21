keyword_divs_ctnr = document.querySelector('#kw_divs_ctnr');
if (keyword_divs_ctnr){
    let kw_div1 = document.querySelector("#kw_div1")
    let kw_div2 = document.querySelector("#kw_div2")
    let kw_div3 = document.querySelector("#kw_div3")
    let kw_div4 = document.querySelector("#kw_div4")
    
    kw_elems = [kw_div1, kw_div2, kw_div3, kw_div4]

    for (let elem of kw_elems){
        elem.addEventListener ("click", async function(){
            
            let keyword = elem.getAttribute("data-keyword")
            
            const res = await fetch
            (`/api/fetch_recipes_by_keyword/${keyword}/1`)
            const data = await res.json();
            
            // RUN FOOD_CTNR_MOD
            food_ctnr_mod(data)

        })
    } 
}
