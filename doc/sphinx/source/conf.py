# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'YTJ_mcar'
copyright = '2024, Youri'
author = 'Youri'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [

    "sphinx.ext.graphviz",

    "sphinx.ext.ifconfig",

    "sphinx.ext.intersphinx",

    "sphinx_copybutton",

    "sphinx_tabs.tabs",

    "sphinx_rtd_theme",

    "myst_parser",

]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

# -- Options for copybutton extension ----------------------------------------

copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "

copybutton_prompt_is_regexp = True

html_static_path = ['_static']

html_css_files = [

    "css/custom.css",

]
