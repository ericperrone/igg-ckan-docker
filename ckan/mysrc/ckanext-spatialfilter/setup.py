from setuptools import setup

setup(
    name='ckanext-spatialfilter',
    version='0.0.1',
    description='CKAN plugin per aggiungere filtro spaziale nella ricerca dataset',
    author='Tuo Nome',
    packages=['ckanext.spatialfilter'],  # <-- pacchetto specificato manualmente
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points='''
        [ckan.plugins]
        spatialfilter=ckanext.spatialfilter.plugin:SpatialFilterPlugin
    '''
)
