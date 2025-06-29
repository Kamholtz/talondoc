# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
from pathlib import Path

from sphinx.application import Sphinx

project = "TalonDoc"
copyright = "2022, Wen Kokke"
author = "Wen Kokke"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# sys.path.append(str(Path("/talon-user").resolve()))
sys.path.append(str(Path("../..").resolve()))

extensions = [
    # Enables support for Markdown
    # https://www.sphinx-doc.org/en/master/usage/markdown.html
    "myst_parser",
    # Enables support for tabs
    # https://sphinx-tabs.readthedocs.io/en/latest/#sphinx-tabs
    "sphinx_tabs.tabs",
    # Enable support for Talon
    "talondoc.sphinx",
]

# -- Options for MyST --------------------------------------------------------

myst_enable_extensions = [
    # Enables colon fence directives
    # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#syntax-colon-fence
    "colon_fence",
    # Enables definition lists
    # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#definition-lists
    "deflist",
]

# -- Options for Sphinx Tabs -------------------------------------------------

# Disable tab closing.
# https://sphinx-tabs.readthedocs.io/en/latest/#sphinx-configuration
sphinx_tabs_disable_tab_closing = True

# Disable default CSS stylesheet.
# Custom stylesheet is added under 'Options for HTML output'.
# # https://sphinx-tabs.readthedocs.io/en/latest/#sphinx-configuration
sphinx_tabs_disable_css_loading = True


# -- Options for TalonDoc ----------------------------------------------------

# talon_packages = [
#     {
#         "name": "user",
#         "path": "/talon-user/community",
#         "exclude": [
#             "conftest.py",
#             "test/stubs/talon/__init__.py",
#             "test/stubs/talon/grammar.py",
#             "test/stubs/talon/experimental/textarea.py",
#             "test/repo_root_init.py",
#             "test/test_code_modified_function.py",
#             "test/test_create_spoken_forms.py",
#             "test/test_dictation.py",
#             "test/test_formatters.py",
#             # "plugin/listening_timeout/*"
#         ],
#         "trigger": "ready",
#     },
#     {
#         "name": "talon_hud",
#         "path": "/talon-user/talon_hud",
#         "exclude": ["docs/*", "themes/*", "preferences/*"],
#         "trigger": "ready",
#     },
# ]

talon_package = {
    "name": "user",
    "path": "../user",
    "exclude": [
        "community/conftest.py",
        "community/test/stubs/talon/__init__.py",
        "community/test/stubs/talon/grammar.py",
        "community/test/stubs/talon/experimental/textarea.py",
        "community/test/repo_root_init.py",
        "community/test/test_code_modified_function.py",
        "community/test/test_create_spoken_forms.py",
        "community/test/test_dictation.py",
        "community/test/test_formatters.py",
        "community/lang/kotlin/kotlin.py",
        "community/lang/kotlin/kotlin.talon",
        "community/lang/kotlin/*",
        "community/lang/java/*",
        "community/lang/kotlin/*",
        "community/lang/php/*",
        "community/lang/proto/*",
        "community/lang/r/*",
        "community/lang/ruby/*",
        "community/lang/rust/*",
        "community/lang/scala/*",
        "community/lang/stata/*",
        "cursorless-settings",
        "cursorless-talon/**/*",
        "neovim-talon/*",
        "talon_hud/*",
        "talon_hud/content/*",
        "talon_hud/**/*",
        # "plugin/listening_timeout/*"
    ],
    "trigger": "ready",
}


# def talon_docstring_hook(sort: str, name: str) -> Optional[str]:
#     return None
#


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "sphinx_rtd_theme"
html_theme = "furo"
html_static_path = ["_static"]

# -- Options HTML Theme Furo -------------------------------------------------
html_theme_options = {
    "navigation_with_keys": True,
}


def setup(app: Sphinx) -> None:
    # Add custom styles for Sphinx Tabs
    app.add_css_file("css/custom-tabs.css")
    # Add custom styles for fragmenting tables
    app.add_css_file("css/custom-fragtables.css")
    # Add custom script for fragmenting tables
    app.add_js_file("js/custom-fragtables.js")
