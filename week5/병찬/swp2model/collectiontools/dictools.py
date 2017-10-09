class DynamicProp(object):
    def __init__(self, **props):
        self.__dict__.update(props)
        for prop, value in props.items():
            if isinstance(value, dict):
                self.__dict__[prop] = DynamicProp(**value)


# usage of DynamicProp Extension
# class IocConfiguration(DynamicProp, providers.Configuration):
#     def __init__(self, *args, **kwargs):
#         providers.Configuration.__init__(self, *args, **kwargs)
#
#     def update(self, **config_info):
#         DynamicProp.__init__(self, **config_info)
