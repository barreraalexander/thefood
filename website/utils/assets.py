from flask_assets import Bundle

bundles = {
    'main_scss': Bundle(
        'scss/main.scss',
        filters='libsass',
        depends='scss/*.scss',
        output='gen/css/main.%(version)s.css'
    ),
    'main_js': Bundle(
        'js/back.js',
        'js/food_ctnr_mod.js',
        'js/keyword_divs_mod.js',
        'js/menu_mod.js',
        'js/redir.js',
        'js/slideshow.js',
        'js/submit_forms.js',
        'js/surprise_btn_mod.js',
        filters='jsmin',
        depends='js/*.js',
        output='gen/js/main.%(version)s.js'
    ),
    'index_js': Bundle(
        # 'js/ModFood.js',
        # 'js/SubmitForms.js',
        filters='jsmin',
        depends='js/*.js',
        output='gen/js/main.%(version)s.js'
    )
}