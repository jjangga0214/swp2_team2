from swp2model.ioc.container import Core, Services, ServiceType, ServiceRole
from swp2model.exec import ExecAnalyzer
import swp2model.exec as exec
from typing import Union
import functools
from enum import Enum


def analyze(fmsg: Union[str, callable] = lambda: Core.config.analyze.fmsg, *,
            log: callable = lambda msg: Core.config.analyze.log(msg),
            analyzer: ExecAnalyzer = Core.exec_analyzer()):
    """
    wrapper for exec.anlyzer decorator. applies config to exec.anlyzer
    :param fmsg: string
    :param log: logging function.
    :type log: (str)-> void
    :return: exec.analyze decorator
    """
    return exec.analyze(fmsg, log=log, analyzer=analyzer)


def service(stype: ServiceType, name: str = None, *args, **kwargs):
    """
    decorator that registers object or function to Services.dynamic
    :param name: service name. if None, __name__ will be used
    """
    name = name.value if isinstance(name, Enum) else name

    def innerdecorate(func):
        Services.add(stype, func, name, *args, **kwargs)

        @functools.wraps(func)
        def wrap(*args, **kwargs):
            return func(*args, **kwargs)

        return wrap

    return innerdecorate
