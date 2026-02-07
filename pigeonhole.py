import sys

def run_pigeonhole(code):
    py_lines = []

    for line in code.splitlines():
        stripped = line.strip()

        # Convert Pigeonhole display to Python print
        if stripped.startswith("display("):
            line = line.replace("display(", "print(")

        py_lines.append(line)

    exec("\n".join(py_lines))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pigeonhole.py <file.ph>")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith(".ph"):
        print("Error: file must end with .ph")
        sys.exit(1)

    with open(filename, "r") as f:
        code = f.read()

    run_pigeonhole(code)

