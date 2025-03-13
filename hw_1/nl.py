if __name__ == "__main__":

    import fileinput
    ln = 0
    with fileinput.input() as f:
        for line in f:
            ln += 1
            print(f"{ln} {line.rstrip()}")
