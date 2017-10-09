import typecheck as tc
from enum import Enum, unique, auto
from frozendict import frozendict
import functools


@unique
class ExecMeta(str, Enum):
    '''
    Enum for property key of Meta information of function execution .
    It dose NOT limit the type or value.
    Rather, it should be decided on where it's used.
    '''

    def _generate_next_value_(name, start, count, last_values):
        return name.lower()

    FUNC = auto()  # function itself
    NAME = auto()  # function name
    ARGS = auto()
    KWARGS = auto()
    RESULT = auto()  # return value
    DURATION = auto()  # time consumed while execution
    TIME = auto()  # specify when the function is executed


class ExecAnalyzer(list):
    @tc.typecheck
    def exec(self, func: callable, *args, **kwargs) -> frozendict:
        from datetime import datetime
        import time

        now = datetime.now()

        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()

        args = args if len(args) >= 2 else args[0]

        record = \
            {
                ExecMeta.FUNC: func,
                ExecMeta.NAME: func.__name__,
                ExecMeta.ARGS: args,
                ExecMeta.KWARGS: kwargs,
                ExecMeta.RESULT: result,
                ExecMeta.DURATION: ended_at - started_at,
                ExecMeta.TIME: now
            }
        record = frozendict(record)
        self.append(record)
        return record


@tc.typecheck
def analyze(fmsg: tc.any(str, callable), *,
            log: callable,
            analyzer: ExecAnalyzer):
    def innerdecorate(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            # 캡처된 변수는 논리적으로 final 이므로 할당을 새로 하면 안된다
            # 따라서 dynamic 하게 값을 변경하기 위해 인자로 함수를 받아 실행가능하게 한다.

            fmsg_ = fmsg() if callable(fmsg) else fmsg

            exec_info = analyzer.exec(func, *args, **kwargs)
            msg = fmsg_.format(**exec_info)
            log(msg)

            return exec_info[ExecMeta.RESULT]

        return wrap

    return innerdecorate
