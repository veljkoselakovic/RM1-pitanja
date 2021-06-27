class Statement(object):

    def __init__(self, text, value):
        self.text = text
        self.value = value
        self.marked = False

    def mark(self):
        self.marked = True

    def unmark(self):
        self.marked = False

    def isMarked(self):
        return self.marked

    def getValue(self):
        return self.value

    def __str__(self):
        return self.text


class Question(object):

    def __init__(self, text, category):
        self.text = text
        self.category = category
        self.statement_list = list()

    def mark_statement(self, statement_index):
        if statement_index <= 0 or statement_index > len(self.statement_list):
            return #raise Exception("Answer doesn't exist")
        self.statement_list[statement_index - 1].mark()

    def unmark_statement(self, statement_index):
        if statement_index <= 0 or statement_index > len(self.statement_list):
            return #raise Exception("Answer doesn't exist")
        self.statement_list[statement_index - 1].unmark()

    def add_statement(self, text, value):
        s = Statement(text, value)
        self.statement_list.append(s)

    def __str__(self):
        output_string = ""
        output_string += self.text
        output_string += "\n"
        i = 0
        for S in self.statement_list:
            output_string += str(i + 1) + ": " + str(S).rstrip()
            output_string += "\n"
            i += 1
        return output_string

    def check_answer(self):
        sum_ = 0;
        for S in self.statement_list:
            if S.isMarked():
                sum_ += S.getValue()
        if sum_ < 0:
            return 0
        return sum_ / 100

    def print_answer(self):
        for S in self.statement_list:
            if S.getValue() > 0:
                print(S)


class MultipleSolutionQuestion(Question):

    def __init__(self, text, category):
        super().__init__(text, category)


class SingleSolutionQuestion(Question):
    def __init__(self, text, category):
        super().__init__(text, category)

    def mark_statement(self, statement_index):
        for S in self.statement_list:
            if S.isMarked():
                raise Exception("Can't select multiple values")
        super().mark_statement(statement_index)

class EssayQuestion(Question):
    def __init__(self, text, category):
        super().__init__(text, category)
        self.solution = ""
        self.answer = ""
    def add_statement(self, text, value=100):
        self.solution = text
    def add_answer(self, text):
        self.answer = text.strip()

    def check_answer(self):
        if self.solution == self.answer:
            return 1.0
        else:
            return 0.0



