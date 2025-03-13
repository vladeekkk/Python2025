from collections import deque

if __name__ == "__main__":
    import sys

    std_limit = 17
    file_limit = 10

    def tail(source, limit = file_limit):
        q = deque(maxlen=limit)
        for line in source:
            q.append(line)

        for line in q:
            print(line, end = "")

    args = sys.argv[1:]
    args_count = len(args)

    if args_count == 0:
        tail(sys.stdin, std_limit)
    elif args_count == 1:
        with open(args[0]) as file:
            tail(file)
    else:
        is_first_file = True
        for filename in args:
            with open(filename) as file:
                if is_first_file:
                    print(f"==> {filename} <==")
                    is_first_file = False
                else:
                    print(f"\n==> {filename} <==")
                tail(file)