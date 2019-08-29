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
    def __init__(self, desctiption, qualifying_question, following_questions):
        self.description = desctiption
        self.qualifying_question = qualifying_question
        self.following_questions = []
        self.add_following_questions(following_questions)
        self.active_question = None

    def __str__(self):
        return self.description

    def add_following_questions(self, following_questions):
        for question in following_questions:
            self.following_questions.append(question)

    def ask_question(self):
        if self.active_question is None:
            self.active_question = -1
            return self.qualifying_question
        self.active_question += 1
        try:
            return self.following_questions[self.active_question]
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
        qualifying_question=Question(
            'Do you like meerkats?', 
            answers={
                'Obviously.': True,
                'No They are Lame.': False
            }
        ),
        following_questions=[

        ]
    ),
    Section(
        desctiption="""
================= Taylor Swift =================
This section is all about Taylor Swift, the singer-songwriter and cat mum to Meredith, Oliva and Benji.""",
        qualifying_question=Question(
            'Do you like Taylor Swift?',
            answers={
                'Obviously.': True,
                'No she is lame.': False,
            }
        ),
        following_questions=[
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
