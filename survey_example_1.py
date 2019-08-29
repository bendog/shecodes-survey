#!/usr/bin/env python3

"""
example of how to do the survey with nested classes using inits
"""

class Answer(object):
    def __init__(self, code, answer_text, action=False):
        self.code = code
        self.answer_text = answer_text
        self.action = action


class Question(object):
    def __init__(self, question_text, answers):
        self.question_text = question_text
        self.answers = {}
        self.add_answers(answers)

    def add_answers(self, answers):
        """ process a dictionary of ansawers to the questions """
        code = ord('a')
        for answer, action in answers.items():
            self.answers[chr(code)] = Answer(
                code=chr(code),
                answer_text=answer,
                action=action
            )
            code += 1

    def answer(self, answer_code):
        """ validate the answer and record """
        # TODO: this currently isn't being used
        return self.answers.get(answer_code)

    def __str__(self):
        response = self.question_text
        for code, answer in self.answers.items():
            response += "\n[%s] %s" % (code, answer.answer_text)
        return response


class Section(object):
    def __init__(self, desctiption, questions):
        self.description = desctiption
        self.questions = []
        self.add_questions(questions)
        self.active_question = -1  # set the initial question to -1 so it becomes 0, this is ugly, it should be handled lower down

    def __str__(self):
        return self.description

    def add_questions(self, questions):
        """ add the question to the seciton """
        for question in questions:
            # check that question is a question
            if isinstance(question, Question):
                self.questions.append(question)

    def ask_question(self):
        self.active_question += 1
        try:
            return self.questions[self.active_question]
        except IndexError:
            return None
    

class Survey(object):

    def __init__(self, sections):
        self.sections = sections

    def run(self):
        for section in self.sections:
            print(section)
            while True:
                q = section.ask_question()
                if not q:
                    # if there are no more questions move on to next seciton
                    break
                while True:
                    print(q)
                    a = input("what is your answer? ").strip().lower()
                    if a in q.answers.keys():
                        # if this answer is valid accept it and move on
                        break
                if not q.answers[a].action:
                    # if the action is false, skip this section
                    break


survey = Survey([
    Section(
        desctiption="""
Welcome to this survey
TODO write a description here""",
        questions=[
            Question(
                'Do you like meerkats?', 
                answers={
                    'Obviously.': True,
                    'No They are Lame.': False
                }
            ),
        ]
    ),
    Section(
        desctiption="""
================= Taylor Swift =================
This section is all about Taylor Swift, the singer-songwriter and cat mum to Meredith, Oliva and Benji.""",
        questions=[
            Question(
                'Do you like Taylor Swift?',
                answers={
                    'Obviously.': True,
                    'No she is lame.': False,
                }
            ),
            Question(
                'What is your favourite Taylor Swift song?',
                answers={
                    'ME!': True,
                    'You need to calm dow': True,
                    "You know what, I can't decide, I love all of them.": True,
                }
            ),
            Question(
                "Which of Taylor's cats is the cutest?",
                answers={
                    "Meredith.": True,
                    "Olivia.": True,
                    "Benji.": True,
                    "All of the above.": True
                }
            ),
        ]
    ),
])

if __name__ == '__main__':
    survey.run()
