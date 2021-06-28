import itertools
import re

in_question = False
current_category = ""


def isQuestion(line):
    if line[:2] == "::":
        return True
    return False


def extractQuestion(line):
    x = re.search(r"::.*::", line)
    if x is not None:
        return x.group(0)
    else:
        return ""


def findFirstCapital(line):
    if '%' in line:
        ind = line.rfind('%')
        return ind + 1
    for i in range(0, len(line)):
        if line[i].istitle():
            return i
        if line[i] == ']' or line[i] == '+':
            return i + 1
    return 0


def extractValue(line):
    x = re.search(r"%-?([0-9]*[.]?)?[0-9]+%", line)
    if x is not None:
        return float(x.group(0)[1:-1])
    else:
        if line[0] == '=':
            return 100.0
        else:
            return 0.0



import sqlite3

con = sqlite3.connect('rm1.db')
cur = con.cursor()

cur.execute('''CREATE TABLE if not exists questions
               (idq INTEGER PRIMARY KEY, qText text, Type text, section text)''')
cur.execute('''CREATE TABLE if not exists statements
               (ids INTEGER PRIMARY KEY, sText text, val integer, idq integer, foreign key (idq) references questions(idq))''')

qs = list()
with open("mreze pitanja.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
    i = 0
    curQuestion = ""
    questionID = 1
    questionType = ""
    sectionID = 0
    statementCounter = 0
    while i < len(lines):
        if isQuestion(lines[i]):
            curQuestion = lines[i]
        else:
            if len(lines[i].strip()) == 0:
                if statementCounter == 0:
                    questionType = "True/False"
                elif statementCounter == 1:
                    questionType = "Essay"
                cur.execute('''INSERT INTO questions (qText, Type, section) VALUES (?, ?, ?)''', (curQuestion, questionType, str(sectionID)))
                questionID += 1
                curQuestion = ""
                questionType = ""
                statementCounter = 0
            elif '@' in lines[i].strip() :
                ind = lines[i].find('@')
                sectionID = lines[i][ind+1]
            else:
                if '%' in lines[i]:
                    questionType = "MulChoice"
                elif '%' not in lines[i]:
                    questionType = "SingleChoice"
                cur.execute('''INSERT INTO statements (sText, val, idq) VALUES (?, ?, ?)''',
                            (lines[i][findFirstCapital(lines[i]):], extractValue(lines[i]), questionID))
                statementCounter += 1

        i += 1
    con.commit()

con.close()
