# import sys, os

# sys.path.append(os.path.abspath('_exts'))

extensions = [ 
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest', 
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo', 
    'sphinx.ext.coverage', 
    'sphinx.ext.pngmath',
    'sphinx.ext.ifconfig', 
    'sphinx.ext.viewcode',
] 

# 'ipython_console_highlighting', 
# 'inheritance_diagram', 
# 'numpydoc', 'lily',

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = 'Grundwissen Mathematik'
copyright = '2011-2015, Bernhard Grotz'

version = '0.3.0'
release = '0.3.0'

language = 'de'
spelling_lang = 'de_DE'

exclude_patterns = ["notes.rst", "*/notes.rst", "**/notes.rst","README.rst"]
todo_include_todos = False
trim_footnote_reference_space = True

pygments_style  = 'sphinx'
html_theme      = 'sphinxdoc'

html_title        = "Grundwissen Mathematik"
html_short_title  = "Grundwissen Mathematik"
htmlhelp_basename = "Grundwissen Mathematik"

html_logo    = "logo.png"
html_favicon = "favicon.ico"
html_static_path = ['_static']
html_last_updated_fmt = '%d. %b %Y'
html_use_smartypants = True
html_additional_pages = {'home': 'home.html'}
html_domain_indices = False
html_use_index = True
html_show_sourcelink = True
html_show_sphinx = False
html_show_copyright = False

html_search_language = 'en'
html_search_options = {'type': 'default'}

latex_documents = [
   ('index', 'grundwissen-mathematik.tex', 'Grundwissen Mathematik',
   'Bernhard Grotz', 'manual'),
]

# latex_logo = "logo.png"

# latex_show_pagerefs = True

latex_preamble = r'''
\usepackage[version=3]{mhchem}
\usepackage{amsmath, units, cancel}
\usepackage{amsfonts, amssymb,color}
\usepackage{nicefrac,marvosym,mathtools,wasysym} 
\setcounter{secnumdepth}{-1}
\setlength{\headheight}{15pt}
\setcounter{tocdepth}{2}
\clubpenalty  = 10000 % Disable single lines at the start of a page ("Schusterjungen")
\widowpenalty = 10000 % Disable single lines at the end   of a page ("Hurenkinder")
\displaywidowpenalty = 10000
\hyphenation{Soft-rutti}
'''

pngmath_latex_preamble = latex_preamble
latex_elements = {
    "babel": "\\usepackage[ngerman]{babel}",
    "preamble": latex_preamble,
    "classoptions": "oneside,openany",
    "papersize": 'a4paper',
    "pointsize": '12pt',
    "fontpkg": '',
    "fncychap": '\\usepackage[Conny]{fncychap}'
}
# Latex-Elements zum Vermeiden leerer Seiten:
# "classoptions": ",openany",

latex_domain_indices = False

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).

intersphinx_mapping = {
    'gw': ('http://grund-wissen.de/', None),
    'gwc': ('http://grund-wissen.de/chemie/', None),
    'gwp': ('http://grund-wissen.de/physik/', None),
    'gwe': ('http://grund-wissen.de/elektronik/', None),
    'gwl': ('http://grund-wissen.de/linux/', None),
    'gwic': ('http://grund-wissen.de/informatik/c/', None),
    'gwil': ('http://grund-wissen.de/informatik/latex/', None),
    'gwip': ('http://grund-wissen.de/informatik/python/', None),
}

