
# 'verb_conjugations' is a list of dictionaries
# each dictionary contains the 'question' & 'answer' and the interaction with the user
verb_conjugations = [
  {'to': "ser":"to be",
   'yo':"soy":"I am",
   'tú':"eres":"you are",
   'el/ella':"es":"he/she is",
   'nosotros':"somos":"we are",
   'vosotros':"sois":"you(pl) are",
   'ellos/as':"son":"they are"
  },
  {'to': "tener":"to have",
   'yo':"tengo":"i have",
   'tú':"tienes":"you have",
   'el/ella':"tiene":"he/she has",
   'nosotros':"tenemos":"we have",
   'vosotros':"tenéis":"you(pl) have",
   'ellos/as':"tienen":"they have"
  }
]

score = 0

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
