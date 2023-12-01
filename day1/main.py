import re

MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

SPELLED_NUMS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
NUMERIC_NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

f = open("input.txt", "r")
lines = f.readlines()

score = 0


def get_number(word: str):
    first_num = ""
    first_num_index = 100000
    last_num = ""
    last_num_index = -1
    # spelled numbers
    for spelled in SPELLED_NUMS:
        if spelled not in word:
            continue
        indices = [match.start() for  match in re.finditer(spelled, word)]
        if first_num_index > indices[0]:
            first_num = MAPPING.get(spelled)
            first_num_index = indices[0]
        if last_num_index < indices[-1]:
            last_num_index = indices[-1]
            last_num = MAPPING.get(spelled)
    for numeric in NUMERIC_NUMS:
        number = str(numeric)
        if number not in word:
            continue
        indices = [match.start() for  match in re.finditer(number, word)]
        if first_num_index > indices[0]:
            first_num = number
            first_num_index = indices[0]
        if last_num_index < indices[-1]:
            last_num = number
            last_num_index = indices[-1]
    num = first_num + last_num
    return int(num)


for word in lines:
    num = get_number(word)
    score += num

print(score)
