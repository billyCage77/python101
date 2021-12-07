from question import Question, Secret
from runner import Runner


all_questions = [
    Question(question='welk ras is Falco?', correct_answer='whippet'),
    Question(question='welke kleur heeft Falco, officieel?', 
        correct_answer='blauw'),
    Question(question='Hoe oud is Falco?', 
        correct_answer='5',
        secret_enabled=True),
    Question(question='Wat snoept Falco het liefst aan tafel?', 
        correct_answer='kaas'),
    Question(question='Wat is Falco zijn favoriete bezigheid?', 
        correct_answer='slapen'),
    Question(question='Wat verwacht Falco rond half twaalf?', 
        correct_answer='stick'),
    Question(question='Wat moet Falco eerst en vooral doen, wanneer hij wakker wordt?', 
        correct_answer='plassen'),
    Question(question='Wat doet Falco wanneer hij iets nodig heeft?', 
        correct_answer='zagen'),
    Question(question='Hoeveel schepjes korrel moeten er in Falco zijn kom?', 
        correct_answer='2'),
]
secret = Secret('wassup?', all_questions)

if __name__ == '__main__':
    meespelen = input("Wil je meespelen? Keuzes: ['ja'/'nee']\n")
    if meespelen.lower() != "ja":
        print('Prettige dag nog!')
        exit()
    print('OK! Dan zullen we starten!')
    name = input('Wat is uw naam?\n').lower().capitalize()
    Runner(all_questions, name, secret).randomize().run()
 