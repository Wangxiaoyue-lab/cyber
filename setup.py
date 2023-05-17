from setuptools import setup,find_packages

setup(
    name='cyber',
    version='0.1',
    description='A system for bioinformatics management',
    author='Cao Jun',
    author_email='caojundudu@eqq.com',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
        'pandas',
        'session_info',
        'pdf2image',
        'graphviz',
        'PIL',
        'pdfkit'
    ]
)