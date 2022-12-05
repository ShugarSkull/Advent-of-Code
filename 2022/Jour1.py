from libaoc import read_input

input = read_input('2022/Jour1.input')

def parse_input(input: str) -> list[int]:
    calories_list = [0]
    i = 0
    for row in input.split('\n'):
        match row:
            case '':
                calories_list.append(0)
                i += 1
            case _:
                calories_list[i] += int(row)
    
    return calories_list

def n_maximum_calories(calories_list: list[int], n: int) -> list[int]:
    # pas la meilleur méthode
    n_maximum_calories: int = 0
    for i in range(n):
        n_maximum_calories += calories_list.pop(calories_list.index(max(calories_list)))
        #   ˆˆˆ pas optimisé 
    return n_maximum_calories

print(max(parse_input(input)))
print(n_maximum_calories(parse_input(input), 3))
