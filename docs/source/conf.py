# tp_bgdia700-develop/docs/source/conf.py

import os
import sys
import sphinx_rtd_theme

# Obtenir le chemin absolu du dossier contenant conf.py
current_dir = os.path.abspath(os.path.dirname(__file__))

# Chemin vers le répertoire racine du projet
project_dir = os.path.abspath(os.path.join(current_dir, '../..'))

# Ajouter le chemin racine du projet à sys.path
sys.path.insert(0, os.path.abspath('../'))  # ou './' selon la structure de votre projet


project = 'bgdia700'
copyright = '2024, Paul, Alexandre, Alexandre, Julian'
author = 'Paul, Alexandre, Alexandre, Julian'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
language = 'fr'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
autodoc_member_order = 'bysource'
autoclass_content = 'both'
