class Question:
    def __init__(self, pyetje, pergjigje):
        self.pyetje = pyetje
        self.pergjigje = pergjigje


Questions = [
    "1. Are roses red ? \n\n (a) Yes \n (b) No",
    "2. Are bananas yellow ? \n\n (a) Yes \n (b) No",
    "3. Are cherries yellow ? \n\n (a) Yes \n (b) No",
]
Questionlist =[
    Question(Questions[0], "a"),
    Question(Questions[1], "a"),
    Question(Questions[2], "b")
]
def test_result(Questionlist):
    score=0
    for question in Questionlist:
        answer=input(question.pyetje + "\n\n Your answer: ")
        if answer == question.pergjigje:
            score += 1
    print("you answered right " + str(score) + " out of " + str(len(Questionlist)) + " questions !")
test_result(Questionlist)
