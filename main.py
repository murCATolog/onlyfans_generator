import re

print ('Введи інформацію про себе.')

personal_info = []

prompts = ['Імʼя: ',
           'Прізвище: ',
           'Твій нік в Інстаграм: ',
           'Вік: ',
           'Зріст: ',
           'Вага: ',
           'Пару речень про себе: ',
           ]

while len(personal_info) < len(prompts):
    prompts_generator = input(prompts[len(personal_info)])

    if len(personal_info) <= 1 and not prompts_generator.isalpha():
        print('Треба вводити лише літери.')
        continue
    elif len(personal_info) == 2 and not re.match("^[a-zA-Z0-9_-]+$", prompts_generator):
        print('Треба вводити лише латинські літери')
        continue
    elif 2 < len(personal_info) <= 5 and not prompts_generator.isdigit():
        print('Треба вводити лише цифри.')
        continue
    elif len(personal_info) == 6 and len(prompts_generator) < 15:
        print('Замало інформації.')
        continue
    elif len(prompts_generator) < 2:
        print('Замало символів.')
        continue
    else:
        personal_info.append(prompts_generator)

print(personal_info)