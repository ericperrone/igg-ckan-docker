import os
from ckan.plugins import implements, SingletonPlugin
from ckan.plugins.interfaces import IConfigurer
import ckan.plugins.toolkit as toolkit

class SpatialFilterPlugin(SingletonPlugin):
    implements(IConfigurer)

    def update_config(self, config):
        here = os.path.dirname(__file__)
        template_dir = os.path.join(here, 'templates')
        toolkit.add_template_directory(config, template_dir)
        public_dir = os.path.join(here, 'public')
        toolkit.add_public_directory(config, public_dir)
#        assets_dir = os.path.join(here, 'assets')
#        toolkit.add_resource(assets_dir, 'spatialfilter')
        toolkit.add_resource('public', 'spatialfilter')