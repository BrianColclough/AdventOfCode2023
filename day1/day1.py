import re

# Path: day1/day1.py
path = 'day1/day1.txt'
fileContents = open(path, 'r')

lines = fileContents.readlines()

total = 0

# for line in lines:
#     firstDigit = None
#     lastDigit = None
#     for letter in line:
#         if letter.isdigit():
#             if firstDigit == None:
#                 firstDigit = letter
#             else:
#                 lastDigit = letter
#     if lastDigit == None:
#         lastDigit = firstDigit

#     number = firstDigit + lastDigit
#     total += int(number)
    
# print(total)

numberMap = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4', 
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine':'9',
    '1':'1',
    '2':'2',
    '3':'3',
    '4':'4',
    '5':'5',
    '6':'6',
    '7':'7',
    '8':'8',
    '9':'9'
}

for line in lines:
    firstDigit = None
    lastDigit = None
    regex = re.compile("(?:one|two|three|four|five|six|seven|eight|nine|\d)", re.IGNORECASE)

    line = line.replace('twone', '21')
    line = line.replace('oneight', '18')
    line = line.replace('threeight', '38')
    line = line.replace('nineight', '98')
    line = line.replace('fiveight', '58')
    line = line.replace('eighthree', '83')
    line = line.replace('eightwo', '82')
    
    contents = re.findall(regex, line)
    print(contents, line)
    for group in contents:
        if group == None:
            continue
        if not firstDigit:
            firstDigit = numberMap[group]
        else:
            lastDigit = numberMap[group]
     
    if firstDigit == None:
        continue
    if lastDigit == None:
        lastDigit = firstDigit
   
    number = firstDigit + lastDigit
    total += int(number)
print('total:', total)

    

