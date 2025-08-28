from setuptools import setup, find_packages

setup(
    name='ckanext-iggtheme',
    version='0.0.1',
    description='CKAN plugin personalizzazione per igg',
    author='Eric Perrone',
    packages=find_packages(),
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points='''
        [ckan.plugins]
        iggtheme=ckanext.iggtheme.plugin:IggThemePlugin
    ''',
    package_data={
        'ckanext.iggtheme': [
            'templates/*.*',
            'templates/*/*.*',
            'templates/*/*/*.*'
        ],
    },
)
