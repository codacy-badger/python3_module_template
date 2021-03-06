import sphinx_gallery
import sphinx_rtd_theme

try:
    from pyquickhelper.helpgen.default_conf import set_sphinx_variables, get_default_stylesheet
except ImportError as e:
    import os
    import sys
    paths = "\n".join(sys.path)
    raise ImportError("pyquickhelper is not installed. PYTHONPATH='{0}'\nsys.path=\n{1}".format(
        os.environ.get("PYTHONPATH", ""), paths))

set_sphinx_variables(__file__, "python3_module_template", "sdpython", 2018,
                     "sphinx_rtd_theme", [
                         sphinx_rtd_theme.get_html_theme_path()],
                     locals(), book=True,
                     extlinks=dict(issue=('https://github.com/sdpython/python3_module_template/issues/%s', 'issue')))

blog_root = "http://www.xavierdupre.fr/app/python3_module_template/helpsphinx/"

html_context = {
    'css_files': get_default_stylesheet(),
}

nblinks = {'slideshowrst': 'http://www.xavierdupre.fr/'}


def custom_latex_processing(latex):
    """
    process a latex file and returned the modified version

    @param      latex       string
    @return                 string
    """
    if latex is None:
        raise ValueError("Latex is null")
    # this weird modification is only needed when jenkins run a unit test in
    # pyquickhelper (pycode)
    return latex
