
if __name__ == "__main__":
    import sys

    def wc(source):
        l, w, b = 0, 0, 0
        for line in source:
            l += 1
            w += len(line.split())
            for symbol in line:
                b += 1 if symbol.isascii() else 2
        return l, w, b

    args = sys.argv[1:]
    args_count = len(args)

    if args_count == 0:
        l, w, b = wc(sys.stdin)
        print(f"{l} {w} {b}")
    elif args_count == 1:
        with open(args[0]) as file:
            l, w, b = wc(file)
            print(f"{l} {w} {b} {args[0]}")
    else:
        total_l, total_w, total_b = 0, 0, 0
        for filename in args:
            with open(filename) as file:
                l, w, b = wc(file)
                total_l += l
                total_w += w
                total_b += b
                print(f"{l} {w} {b} {filename}")
        print(f"{total_l} {total_w} {total_b} <--total")