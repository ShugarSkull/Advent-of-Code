def read_input(file: str) -> str:
    with open(file, 'r') as input:
        return input.read()

print(read_input('Jour1.input'))