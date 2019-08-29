#!/usr/bin/env python3

"""
This file is going to be an example of how ot build the survey using inits + methods
"""

class Answer(object):

    def __init__(self, code, answer_text, action=False):
        self.code = code
        self.answer_text = answer_text
        self.action = action


class Question(object):
    def __init__(self, question_text):
        self.question_text = question_text
        self.answers = []

    def add_answer(self, answer):
        self.answers.append(answer)


class Section(object):
    def __init__(self, qualifying_question):
        self.qualifying_question = qualifying_question
        self.following_questions = []

    def add_following_question(self, following_question):
        self.following_questions.append(following_question)



# setup  section 1
meerkats_q = Question('Do you like meerkats?')
meerkats_q.add_answer(Answer(code='a', answer_text='Obviously.'))
meerkats_q.add_answer(Answer(code='b', answer_text='No They are Lame.'))

section_1 = Section(qualifying_question=meerkats_q)

# setup section 2
tswift_q = Question('Do you like Taylor Swift?')
tswift_q.add_answer(Answer(code='a', answer_text='Obviously.'))
tswift_q.add_answer(Answer(code='b', answer_text='No she is lame.'))

section_2 = Section(qualifying_question=tswift_q)

tswift_q = Question('What is your favourite Taylor Swift song?')
tswift_q.add_answer(Answer(code='a', answer_text='ME!'))
tswift_q.add_answer(Answer(code='b', answer_text='You need to calm down'))
tswift_q.add_answer(Answer(code='c', answer_text="You know what, I can't decide, I love all of them."))
section_2.add_following_question(tswift_q)

tswift_q = Question('What is your favourite Taylor Swift song?')
tswift_q.add_answer(Answer(code='a', answer_text='ME!'))
tswift_q.add_answer(Answer(code='b', answer_text='You need to calm down'))
tswift_q.add_answer(Answer(code='c', answer_text="You know what, I can't decide, I love all of them."))
tswift_q.add_answer(Answer(code='d', answer_text="All of the above"))
section_2.add_following_question(tswift_q)
