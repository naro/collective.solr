from zope.i18nmessageid import MessageFactory
from App.config import getConfiguration
from logging import getLogger
logger = getLogger('collective.solr')
zope_conf = getConfiguration()

SolrMessageFactory = MessageFactory('solr')

# expects this key in zope.conf:
#    <product-config collective.solr>
#        solr-host localhost
#        solr-port 8983
#        solr-base /solr
#    </product-config>
# This configuration is optional and overrides setting in the controlpanel.

SOLR_PRODUCTCONFIG_HOST = None
SOLR_PRODUCTCONFIG_PORT = None
SOLR_PRODUCTCONFIG_BASE = None

if hasattr(zope_conf, 'product_config'):
    config = zope_conf.product_config.get('collective.solr', {})
    if config is not None:
        SOLR_PRODUCTCONFIG_HOST = config.get('solr-host', SOLR_PRODUCTCONFIG_HOST)
        try:
            port = int(config.get('solr-port'))
        except ValueError:
            port = None
        SOLR_PRODUCTCONFIG_PORT = port
        SOLR_PRODUCTCONFIG_BASE = config.get('solr-base', SOLR_PRODUCTCONFIG_BASE)
        if SOLR_PRODUCTCONFIG_HOST or SOLR_PRODUCTCONFIG_PORT or SOLR_PRODUCTCONFIG_BASE:
            logger.info('Using some solr server configuration values from zope.conf')
    del config
    del port

del zope_conf
