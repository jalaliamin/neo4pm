import setuptools

setuptools.setup(
    name="#{Build.Repository.Name}#",
    version="#{version}#", 
    description="Python #{Build.Repository.Name}# Package",
    packages=setuptools.find_packages('src'),
    package_dir={'':'src'},
    install_requires=[
        'pandas',
        'numpy',
        'datetime',
        'py2neo',
    ]
)