from libaoc import read_input

input = read_input('2022/Jour2.input')

def parse_input(intput: str) -> list[int]:
    score_list = []
    i=0
    for row in input.split('\n'):
        score_list.append(0)
        round = row.split(' ')
        match round[1]:
            case 'X':
                score_list[i] += 1
                match round[0]:
                    case 'A':
                        score_list[i] += 3
                    case 'B':
                        score_list[i] += 0
                    case 'C':
                        score_list[i] += 6
            case 'Y':
                score_list[i] += 2
                match round[0]:
                    case 'A':
                        score_list[i] += 6
                    case 'B':
                        score_list[i] += 3
                    case 'C':
                        score_list[i] += 0
            case 'Z':
                score_list[i] += 3
                match round[0]:
                    case 'A':
                        score_list[i] += 0
                    case 'B':
                        score_list[i] += 6
                    case 'C':
                        score_list[i] += 3
        i += 1
    return score_list

def add_score(score_list: list[int]) -> int:
    total_score = 0
    for score in score_list:
        total_score += score
    
    return total_score

score_list = parse_input(input)

print(add_score(score_list))

def parse_inputV2(input: list[str]) -> list[int]:
    score_list = []
    i=0
    for row in input.split('\n'):
        score_list.append(0)
        round = row.split(' ')