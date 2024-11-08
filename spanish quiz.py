# 'verb_conjugations' is a list of dictionaries
# each dictionary contains the 'question' & 'answer' and the interaction with the user
verb_conjugations = [
  {'ser':"to be",
   'soy':"I am",
   'eres':"you are",
   'es':"he/she is",
   'somos':"we are",
   'sois':"you(pl) are",
   'son':"they are"
  },
  {'tener':"to have",
   'tengo':"i have",
   'tienes':"you have",
   'tiene':"he/she has",
   'tenemos':"we have",
   'tenéis':"you(pl) have",
   'tienen':"they have"
  }
]
#simple future tense suffix 

   {
    "yo":"é",
    "tú":"ás",
    "él/ella":"á",
    "nosotros":"emos",
    "vosotros":"áis",
    "ellos/ellas":"án"
  }


score = 0

'''
for verb_conjugations_question in verb_conjugations:
    response = input(f'{verb_conjugations_question["question"]} ?\n---> ').lower()
    answers = verb_conjugations_question["answer"].lower().split(" or ")
  
    if response not in answers:
        print(f'No, the answer to {verb_conjugations_question["question"]} is {answers[0]}')
        print(f'{verb_conjugations_question["snarky"]}\n')
    else:
        print("Correct!!!\n")
        score += 1
        print(f'{verb_conjugations_question["funfact"]}\n')

print(f'You got {score} out of {verb_conjugations.__len__()}!')
'''

