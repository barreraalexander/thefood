from flask import Markup, url_for

def component(model):
    clock_src = url_for('static', filename='images/assets/watch.svg.svg')
    html = Markup(f"""
    <div class="preview_div">
        <img onclick=submitView("{ model._id }") src="{model.img_locs.split('$')[0]}">
        <div class="description_div">
                <h3 onclick=submitView("{model._id}")>
                    {model.name}
                </h3>
            <p class="description_div_p">
                {model.description}
            </p>
            <div class="food_time_div">
                <div>
                    <img src="{clock_src}">
                        <p class="description_preptime">
                            {model.preptime}
                        </p>
                </div>
            </div>
        </div>
    </div>
    """)
    return html