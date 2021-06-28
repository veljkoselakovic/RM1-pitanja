import sqlite3
import random
import Question

con = sqlite3.connect('rm1.db')
cur = con.cursor()
inp_section = input("K1, K2, K3 ili I?")

cur.execute("select MAX(idq) from questions")

questionNr = int(cur.fetchall()[0][0])

while True:

    rand_nr = random.randint(1, questionNr)
    if inp_section[0] == 'I':
        cur.execute("select * from questions where questions.idq = ?", (rand_nr,))
    else:
        cur.execute("select * from questions where questions.idq = ? and section = ? ", (rand_nr, inp_section[1]))
    fetched = cur.fetchone()
    if fetched is None:
        continue
    qText = fetched[1].strip()
    if fetched[2] == "MulChoice":
        question = Question.MultipleSolutionQuestion(qText, fetched[3])
    elif fetched[2] == "SingleChoice":
        question = Question.SingleSolutionQuestion(qText, fetched[3])
    elif fetched[2] == "Essay":
        question = Question.EssayQuestion(qText, fetched[3])
    elif fetched[2] == "True/False":
        question = Question.TrueFalseQuestion(qText, fetched[3])

    cur.execute("select * from statements where statements.idq = ?", (rand_nr,))
    output = cur.fetchall()
    if fetched[2] == "True/False":
        question.add_statement("True")
        # No soutions for these for now
    else:
        for x in output:
            question.add_statement(x[1], float(x[2]))
    print(question)

    inp = input()
    inp = inp.strip()

    try:

        if fetched[2] == "MulChoice":
            answs = inp.split()
            for answ in answs:
                question.mark_statement(int(answ))
            print(question.check_answer())
        elif fetched[2] == "SingleChoice":
            question.mark_statement(int(inp))
            print(question.check_answer())
        elif fetched[2] == "Essay":
            question.add_answer(inp)
            print(question.check_answer())
        elif fetched[2] == "True/False":
            question.add_answer(inp)
            print(question.check_answer())

    except:
        pass
    question.print_answer()
