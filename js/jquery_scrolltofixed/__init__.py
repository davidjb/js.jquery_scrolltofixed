from fanstatic import Library, Resource

library = Library('scrolltofixed', 'resources')

scrolltofixed = Resource(library, 'jquery-scrolltofixed.js',
                         minified='jquery-scrolltofixed-min.js')
