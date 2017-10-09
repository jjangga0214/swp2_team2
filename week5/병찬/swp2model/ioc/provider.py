import dependency_injector.providers as providers
import swp2model.collectiontools.dictools as dictools


class IocConfiguration(dictools.DynamicProp, providers.Configuration):
    def __init__(self, *args, **kwargs):
        providers.Configuration.__init__(self, *args, **kwargs)

    def update(self, **config_info):
        dictools.DynamicProp.__init__(self, **config_info)
