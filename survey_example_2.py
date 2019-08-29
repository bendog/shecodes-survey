#!/usr/bin/env python3

"""
an example of how to create base classes and then inherit and extend with child classes
"""


# Base Classes 


class Answer(object):
    code = ""
    text = ""
    action = True


class Question(object):
    text = ""
    answers = {}

    def __str__(self):
        response = self.text
        for code, answer in self.answers.items():
            response += "\n[%s] %s" % (code, answer.text)
        return response


class Section(object):
    description = ""
    questions = []

    def __init__(self):
        self.active_question = -1

    def __str__(self):
        return self.description

    def ask_question(self):
        self.active_question += 1
        try:
            return self.questions[self.active_question]
        except IndexError:
            return None


class Survey(object):
    sections = []

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


# meerkat specific classes 


class MeerkatsAnsA(Answer):
    code = 'a'
    text = 'Obviously.'


class MeerkatsAnsB(Answer):
    code = 'b'
    text = 'No They are Lame.'
    action = False

class MeerkatsQ(Question):
    text = 'Do you like meerkats?'
    answers = {
        'a': MeerkatsAnsA(),
        'b': MeerkatsAnsB(),
    }

class MeerkatsSection(Section):
    description = """
Welcome to this survey
TODO write a description here"""
    questions = [
        MeerkatsQ(),
    ]


# taylor swift Q1


class TaylorAnsA(Answer):
    code = 'a'
    text = 'Obviously.'
    
class TaylorAnsB(Answer):
    code = 'b'
    text = 'No she is lame.'
    action = False

class TaylorQ(Question):
    text = 'Do you like Taylor Swift?'
    answers = {
        'a': TaylorAnsA(),
        'b': TaylorAnsB(),
    }


# taylor swift q2


class TaylorSongAnsA(Answer):
    code = 'a'
    text = 'ME!'
    
class TaylorSongAnsB(Answer):
    code = 'b'
    text = 'You need to calm down.'
    
class TaylorSongAnsC(Answer):
    code = 'c'
    text = "You know what, I can't decide, I love all of them."

class TaylorSongQ(Question):
    text = 'What is your favourite Taylor Swift song?'
    answers = {
        'a': TaylorSongAnsA(),
        'b': TaylorSongAnsB(),
        'c': TaylorSongAnsC(),
    }


# taylor swift Q3 


class TaylorCatAnsA(Answer):
    code = 'a'
    text = 'Meredith.'


class TaylorCatAnsB(Answer):
    code = 'b'
    text = 'Olivia.'


class TaylorCatAnsC(Answer):
    code = 'c'
    text = 'Benji.'


class TaylorCatAnsD(Answer):
    code = 'c'
    text = 'All of the above.'


class TaylorCatQ(Question):
    text = "Which of Taylor's cats is the cutest?"
    answers = {
        'a': TaylorCatAnsA(),
        'b': TaylorCatAnsB(),
        'c': TaylorCatAnsC(),
        'd': TaylorCatAnsD(),
    }


# taylor swift section


class TaylorSection(Section):
    description = """
================= Taylor Swift =================
This section is all about Taylor Swift, the singer-songwriter and cat mum to Meredith, Oliva and Benji."""
    questions = [
        TaylorQ(),
        TaylorSongQ(),
        TaylorCatQ(),
    ]


# setup survey


class MySurvey(Survey):
    sections = [
        MeerkatsSection(),
        TaylorSection(),
    ]


if __name__ == '__main__':
    # initiate the survey
    my_survey = MySurvey()
    # run the survey 
    my_survey.run()
