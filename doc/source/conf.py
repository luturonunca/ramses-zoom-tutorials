# Local docs build, modelled on ramses-tutorials/doc/source/conf.py
project = "Cosmological zoom-in tutorials"
extensions = [
    "myst_parser",
    "sphinx.ext.mathjax",
    "nbsphinx",
    "sphinx_copybutton",
]
nbsphinx_execute = "never"
html_sourcelink_suffix = ""
master_doc = "index"
exclude_patterns = ["_build", "**.ipynb_checkpoints", "Cosmological-Zoom/ramses", "Cosmological-Zoom/MUSIC2", "Cosmological-Zoom/MyFirstZoom", "Cosmological-Zoom/.venv"]
html_theme = "sphinx_rtd_theme"
