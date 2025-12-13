#Вариант 3
import re
import csv
#Задание 1

file = open('task1-en.txt', 'r') 
text = file.read()
file.close()

pattern1 = r'[a-z-A-Z]+,'
pattern2 = r'[+[\S]+]'

matches1 = re.findall(pattern1, text)
matches2 = re.findall(pattern2, text)
print(matches1)
print(matches2)

#Задание 2
file2 = open('task2.html', 'r', encoding='utf-8')
text2 = file2.read()
file2.close()
pattern3 = r'"#+\w{6}"'
matches3 = re.findall(pattern3, text2)
print(matches3)

#Задание 3
with open('task3.txt', "r", encoding="utf-8") as f:
    words = f.read().split()
re_email = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
re_date = re.compile(r'^\d{4}-\d{2}-\d{2}$')
re_url = re.compile(r'^https?://')
re_id = re.compile(r'^\d+$')

accounts = []

for i in range(0, len(words), 5):
    chunk = words[i:i + 5]

    email = None
    date = None
    url = None
    id_ = None
    surname = None

    for t in chunk:
        if re_email.match(t):
            email = t
        elif re_date.match(t):
            date = t
        elif re_url.match(t):
            url = t
        elif re_id.match(t):
            id_ = t
        else:
            surname = t
    
    accounts.append([id_, surname, email, date, url])

with open('task3.csv', "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["ID", "Фамилия", "Email", "Дата регистрации", "Сайт"])

    writer.writerows(accounts)
