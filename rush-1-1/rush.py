import sys


def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        line = ""
        for col in range(x):
            if (row == 0 or row == y - 1) and (col == 0 or col == x - 1):
                line += "o"
            elif row == 0 or row == y - 1:
                line += "-"
            elif col == 0 or col == x - 1:
                line += "|"
            else:
                line += " "
        print(line)


if __name__ == "__main__":
    tests = [(5, 3), (5, 1), (1, 1), (1, 5), (4, 4)]
    for x, y in tests:
        print(f"rush({x}, {y})")
        rush(x, y)
        print()
