from flask import Markup, url_for

def component(title='title'):
    html = Markup(f"""
    <section id="index_section4" class="invisible">
        <div>
            <div id="model_img_src" class="model_img_div">
                <button id='roll_again_btn' class="roll_again_btn" >
                    Roll Again
                </button>

                <div id="heart_icon" class="heart_icon_ctnr">
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 60 54">
                    <defs>
                        <style>
                            .cls-1 {{
                                opacity: 0.9;
                            }}
                        </style>
                    </defs>
                    <image id="heart.svg" class="cls-1" width="60" height="54" xlink:href="data:img/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFgAAABPCAYAAABvRgIXAAAE8klEQVR4nO2ceU/bQBDFX8xRKFCOBIqqqpXaSj3g+3+QXuoFlJYeXIUAgQAJqSZ9jrYmTuz1rr1J9if5r2B7/LBnZ2ZntwRzTANYAHCXxySAMR4tAE0AlwAuAJwBqAI4N3j/Xog98wBmaecd2lWiXXJc0R45jmlnZrIKLIbfB7BMo9NSB7AH4DfFN4nYswpgBcCUxnXFnn0Au1leBF2B5wA8BrCoe+MILQr9jaJnQcR8RGFNfaFHALYBnKY9Ma0B8tk/BVBJe6OE3ADYodCtlOeWKOxDAIEl+w4AbNCdJDYqKeIGngEYt2S8ivjoDyn8oPjVF/SxtmkA+EL30ZexBH8j/4QnPGy9GVEm+YnXErgMcVPrmn5Wh4Bf8DgHw570E1jEfcmBLG8CfjV1Ct2NFdqX5EUxzT0AM3QbsfQyTMR9BaBcgPGqDZUYkUXc5wYHMh3u0i3FitxL4Gd8CBcocwQP3cUi39wixQ0R/z8B4E+3H+MEXmUY5goi5BKAQz7MekFuIY45RhZn0d+7GSn/kTVH3g6VgNnYco4DWhoW6Soa6jndBF5z9AHA6GLSATu6UaI/3lV/i4ZdKxwdPXrci45bqsAlx/zuoPJYda+qwLpFEc//TKlvsSrwAy+UMTpahgLP5pTHjwodPUOBi8zWhpW2pqHAtsqPo0wlFHiCObXHLKLpRMA0z2OHOS+wXdoC+9jXHlNeYLtMhYOcxw7tQc6luuqwMRbkOJE5igSBRv+BJzmtgH1ZHjs0g+gUh8cojcBAL5gnnroX2C5tgeO6ZjzZqQVshPbYoRqw0dh087OHuoZJxqEXxDhtTUOB94bnuZyhrWko8KmpRR+eNhfhcgO1DvHTa2OMjpaqwLs+qzNCQ+1PUwWWmsSPwXwmp/ih1neipcqdNCtoPLe4ooYdogLLMqotr5s2W9SwQ7di+57P7rSodgt342YzPvk6cSqa1OwWcfNxMhJe+561xGzErZnrNeF5xvafmWJtdx5Z8fk1zsh+E56fc9xyYBA5p0ax9Juyb/HVX/Gzz7cQN/qmX1ibpCeiwbza5PYAg468eO+6rYuLkrTp5JJTS76P+B+f4lZ2RknT1VNjOGJqE45BZZM7tCQibdvUKd3E/IiKKxuFfE9zgk5fWpXnjdqCxZ1e4Vgcuo1/xyMm8o5ujSZLZ+WoiKwtLgy0robp4ULG67jKNg9tTPQGV4c0utiM1nZ1MNV8fcpYeWkIkpEW099fJi5msru9RqErAyyyFMvf99voKA2mlw/UuUteZQCXJlyztnBi8qI2RLhiV4u4izw2sTNBneIarxzaessarJMuOLwFTIgUbF7b6s+z+RmLP9tXtpR1kSNWxaz1g9j2ky2KPOngfhRSsPkYnQU2TV4D0R8+iCux8pZOXUGHPEf6Ew4i5QLDuBvu6pq43JiVvEOpc2Z+5QLufU1/e5TnTYuIVS8ZyC/luE76gpFC7utRikoGGuyCmdfc+z0NJ0kmJ21RZLZ1Q5GnLfZe7DP1tRop9MKFdPZA2fjTJN+5FXihuFIvOOYnbKIa16KwmUuNJnCpIHPGalw5Q5NL03Q1LCuuVbzqTEp0CkWXNqphWXGxpHjNwWkxRaGoxjDMuXXXrtZsm4wwkhSKJHF46+oCHpeL4mGhaLzH3m6/8ijYZGFQpnbEXciWsWFFTgZEWYuWa9qbGgB/AY15/sq692JJAAAAAElFTkSuQmCC"/>
                </svg>
                </div>
                
            </div>


            <div id="model_details_ctnr" class="model_details_div">
                
                <a id="chosen_recipe_link" href="#">
                    <h3 id="model_name"> Name of Recipe </h3>
                </a>
                
                <div id="prep_badges_ctnr" class="prep_badges_div">
                    
                    <div id="model_prep_time_ctnr">
                        <p id="model_prep_time">
                            Prep
                        </p>
                    </div>
                    
                    <div id="model_cook_time_ctnr">
                        <p  id="model_cook_time">
                            Cook
                        </p>
                    </div>
                    
                    <div id="model_total_time_ctnr">
                        <p id="model_total_time">
                            Total
                        </p>
                    </div>

                    <div id="model_rating_ctnr">
                        <img src="{url_for('static', filename='images/assets/rating star.svg.svg')}">
                        <p id="model_rating">
                            0
                        </p>
                    </div>
                </div>
                
                <hr>
                
                <div id="model_ings_ctnr">
                    <h5>
                        Ingredients
                    </h5>
                    <ul id="model_ings_list"></ul>
                </div>

                <hr>
                <div id="model_steps_ctnr">
                    <h5>
                        Steps
                    </h5>
                    <div id="model_steps_list"></div>
                </div>
            </div>


        </div>  
    </section>
    """)
    return html
