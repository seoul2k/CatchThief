from distutils.core import setup

from Cython.Build import cythonize

setup(
    name='cython_CTT',
    ext_modules=cythonize("AI_Choice.py", language_level=3),
    #ext_modules=cythonize("AI_Choice_ui.py", language_level=3),
    #ext_modules=cythonize("AI_Thief.py", language_level=3),
    #ext_modules=cythonize("AI_Police.py", language_level=3),
    #ext_modules=cythonize("Floyd.py", language_level=3),
    #ext_modules=cythonize("MainWindow.py", language_level=3),
    #ext_modules=cythonize("Role.py", language_level=3),
)