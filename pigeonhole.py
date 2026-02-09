import sys

if len(sys.argv) < 2:
    print("Usage: python pigeonhole.py <file.ph>")
    sys.exit(1)

with open(sys.argv[1]) as f:
    code = f.read()

code = code.replace("display(", "print(")

exec(code)

