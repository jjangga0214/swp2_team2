import typecheck as tc


@tc.typecheck
def interact_cli(*, parse: callable, run: callable):
    import collections
    while True:
        args = input("Enter arg(s) : ")
        try:
            args = parse(args)
        except ValueError as e:
            print(e)
            continue
        if args == -1:
            print("bye")
            break
        try:
            if isinstance(args, collections.Iterable):
                run(*args)
            else:
                run(args)
        except Exception as e:
            print(e)
