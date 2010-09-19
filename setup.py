from distutils.core import setup
setup(
    name='concordance',
    version='0.1alpha',
    description='A simple GUI tool for building concordances',
    long_description='A simple GUI tool for building concordances',
    license='GNU GPL v3',
    author='Ludovico Fischer',
    author_email='livrerie@gmail.com',
    url='http://github.com/ludovicofischer/Concordance',
    package_dir={'': 'concordance'},
    py_modules=['concordance', 'texttools','ui_main_window'],
    scripts=['concordance/main.py'],
    requires=['PyQt',]
)
    
    
