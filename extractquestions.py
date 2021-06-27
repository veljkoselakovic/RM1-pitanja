import itertools
import re
import Question

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
    for i in range(0, len(line)):
        if line[i].istitle():
            return i
        if line[i] == ']' or line[i] == '+':
            return i + 1
    return 0


def extractStatement(line):
    x = re.search(r"([~|=]\*moodle+.*)|([~|=]\[moodle.*)|(%-?\d+%.*)", line)
    if x is not None:
        return x.group(0)
    else:
        return ""


def extractValue(line):
    x = re.search(r"%-?([0-9]*[.]?)?[0-9]*%", line)
    if x is not None:
        return float(x.group(0)[1:-1])
    else:
        x = re.search(r"=", line)
        if x is not None:
            return 100
        else:
            return 0


def countRows(line):
    x = len(re.findall(r"([~|=]\*moodle+.*)|([~|=]\[moodle.*)|(%-?([0-9]*[.]?)?[0-9]*%)", line))
    return x


qs = list()
with open("mreze pitanja.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
    curQ = ""
    curQobj = None
    answ = ""
    for line in lines:
        if isQuestion(line):

            curQ = extractQuestion(line)
            answ = extractStatement(line)
            curQobj = None
        else:
            if len(line) > 1 and line[1] == '%':
                if curQobj is None:
                    curQobj = Question.MultipleSolutionQuestion(curQ, "I")
                    qs.append(curQobj)
                if answ != "" and curQobj is not None:
                    curQobj.add_statement(answ[findFirstCapital(answ):], extractValue(answ))
                    answ = ""
                if curQobj is not None:
                    for i in range(countRows(line)):
                        try:
                            curQobj.add_statement(line[findFirstCapital(line):], extractValue(line))
                            line = line[findFirstCapital(line):]
                        except:
                            pass
            else:
                if curQobj is None:
                    curQobj = Question.SingleSolutionQuestion(curQ, "I")
                    qs.append(curQobj)
                if answ != "" and curQobj is not None:
                    curQobj.add_statement(answ[findFirstCapital(answ):], extractValue(answ))
                    answ = ""
                if curQobj is not None and len(line.strip()) != 0:
                    for i in range(countRows(line)):
                        try:
                            curQobj.add_statement(line[findFirstCapital(line):], extractValue(line))
                            line = line[findFirstCapital(line):]
                        except:
                            pass

import random

random.shuffle(qs)
for q in qs:

    if isinstance(q, Question.MultipleSolutionQuestion):
        print("------MULTIPLE CHOICE----------")
        print(q)
        answrs = input().strip().split(' ')
        for choice in answrs:
            q.mark_statement(int(choice))

    else:
        print(q)
        answr = int(input())
        q.mark_statement(answr)
    print(q.check_answer())
    q.print_answer()
