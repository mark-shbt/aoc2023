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

SPELLED_NUMS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

f = open("input.txt", "r")
lines = f.readlines()

score = 0


def get_number(word: str):
    first_num = ""
    first_num_index = 100000
    last_num = ""
    last_num_index = -1
    # spelled numbers
    for numbers in SPELLED_NUMS:
        if numbers not in word:
            continue
        indices = [match.start() for match in re.finditer(numbers, word)]
        if first_num_index > indices[0]:
            first_num = MAPPING.get(numbers) if numbers.isalpha() else numbers
            first_num_index = indices[0]
        if last_num_index < indices[-1]:
            last_num_index = indices[-1]
            last_num = MAPPING.get(numbers) if numbers.isalpha() else numbers
    num = first_num + last_num
    return int(num)


for word in lines:
    num = get_number(word)
    score += num

print(score)
