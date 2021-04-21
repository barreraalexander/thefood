from flask import Markup, url_for

RATE_SVG = """
            <svg xmlns="http://www.w3.org/2000/svg" width="14.75" height="14.814" viewBox="0 0 14.75 14.814">
                <path id="start-filled" d="M7,1,8.5,5.533H13L9.5,8.467,10.75,13,7,10.333,3.25,13,4.5,8.467,1,5.533H5.5Z" transform="translate(0.375 0.592)" fill="#f1c471" stroke="#f1c471" stroke-width="1"/>
            </svg>
            """

def component(rate=1) :
    style=''

    html = Markup(f"""
        <div class="rate_div_component", style="{style}">
            {RATE_SVG}
            <p style="font-size:.6rem;">
                {rate}
            </p>
        </div>
    """)

    return html


def component2(rate=1) :
    """
    Some kwargs for this component
    ______________________________
    color = 'white' or 'gray', default is gray
    width = 'css width', default is 2em
    """
    style=''

    html = Markup(f"""
        <div class="rate_div_component", style="{style}">
            {RATE_SVG}
            <p style="font-size:.6rem;">
                {rate}
            </p>
        </div>
    """)
    return html
