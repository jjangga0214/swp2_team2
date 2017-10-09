import typecheck as tc
from swp2model import seq
from swp2model.exec import ExecMeta as Meta
import swp2model.ioc.decorator as iocd
import swp2model.ioc.container as container
import statistics


@iocd.service(container.ServiceType.CALLABLE)
@iocd.analyze()
def fibo_iter(n: int):
    return seq.fibo_iter(n)


@iocd.service(container.ServiceType.CALLABLE)
@iocd.analyze()
def fibo_recur(n: int):
    return seq.fibo_recur(n)


@iocd.service(iocd.ServiceType.CALLABLE)
@tc.typecheck
def run(n: int):
    container.Services.dynamic.fibo_iter(n)
    container.Services.dynamic.fibo_recur(n)


@iocd.service(container.ServiceType.CALLABLE)
def stat():
    for fname in ("fibo_iter", "fibo_recur"):
        filtered = filter(lambda snapshot: snapshot[Meta.NAME] is fname,
                          container.Core.exec_analyzer())
        durations = map(lambda snapshot: snapshot[Meta.DURATION], filtered)
        durations = list(durations)
        print()
        print("[%s TIME BENCHMARK]" % fname)
        print("     mean : %f" % statistics.mean(durations))
        print("     variance : %f" % statistics.variance(durations))
        print("     stdev : %f" % statistics.stdev(durations))


if __name__ == "__main__":
    container.Core.config.update(**{
        "analyze": {
            "fmsg": "{%s}({%s})={%s}, time={%s}" % tuple(map(lambda el: el.value, (
                Meta.NAME, Meta.ARGS, Meta.RESULT, Meta.DURATION))),
            "log": print
        }
    })
    container.Application.main()
    container.Services.dynamic.stat()
