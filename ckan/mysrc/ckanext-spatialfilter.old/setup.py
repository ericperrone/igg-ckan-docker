from setuptools import setup, find_packages

setup(
    name='ckanext-spatialfilter',
    version='0.0.1',
    description='CKAN plugin per aggiungere filtro spaziale nella ricerca dataset',
    author='Eric Perrone',
    packages=find_packages(),
    # packages=['ckanext.spatialfilter'],  # <-- pacchetto specificato manualmente
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points='''
        [ckan.plugins]
        spatialfilter=ckanext.spatialfilter.plugin:SpatialFilterPlugin
    ''',
    package_data={
        'ckanext.spatialfilter': [
            'assets/*.*',
            'assets/*/*.*',
            'assets/*/*/*.*',
            'public/*.*',
            'public/*/*.*',
        ],
    },
)
