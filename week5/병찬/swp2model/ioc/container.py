import dependency_injector.containers as containers
import dependency_injector.providers as providers
from swp2model import interaction, exec
import swp2model.ioc.provider as provider
from enum import Enum, unique, auto


class Core(containers.DeclarativeContainer):
    """IoC Container of core componant providers"""
    exec_analyzer = providers.Singleton(exec.ExecAnalyzer)
    # config = providers.Configuration('config')
    config = provider.IocConfiguration('config')


@unique
class ServiceType(Enum):
    SINGLETON = providers.Singleton
    FACTORY = providers.Factory
    CALLABLE = providers.Callable


@unique
class ServiceRole(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return str(name.lower())

    RUN = auto()


class Services(containers.DeclarativeContainer):
    """IoC container of business service componant providers"""
    dynamic = containers.DynamicContainer()

    @staticmethod
    def add(stype: ServiceType, service, name: str = None, *args, **kwargs):
        """
        registers object or function to Services.dynamic
        :param name: service name. if None, __name__ will be used
        """
        name = service.__name__ if name is None else name
        dynamic_provider = stype.value(service, *args, **kwargs)
        containers.DynamicContainer.__setattr__(
            Services.dynamic, name, dynamic_provider)


class Application(containers.DeclarativeContainer):
    """IoC container of application component providers"""
    main = providers.Callable(interaction.interact_cli, parse=int,
                              run=lambda *args, **kwargs: Services.dynamic.run(*args, **kwargs))
