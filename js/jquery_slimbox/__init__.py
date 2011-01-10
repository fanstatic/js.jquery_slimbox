from fanstatic import Library, Resource
import js.jquery

library = Library('slimbox', 'resources')

slimbox_css = Resource(library, 'css/slimbox2.css')

slimbox = Resource(library, 'src/slimbox2.js', minified='js/slimbox2.js',
    depends=[js.jquery.jquery, slimbox_css])
