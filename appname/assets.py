from flask_assets import Bundle

common_css = Bundle(
    'css/normalize.css',
    'css/skeleton.css',
    'css/site.css',
    filters='cssmin',
    output='public/css/common.css'
)

# I currently have no JS
# common_js = Bundle(
#     'js/vendor/jquery.min.js',
#     'js/vendor/bootstrap.min.js',
#     Bundle(
#         'js/main.js',
#         filters='jsmin'
#     ),
#     output='public/js/common.js'
# )
