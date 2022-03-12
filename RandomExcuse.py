#generates a random excuse

import random

myGenericList = ["""Good Evening,\n
(Insert excuse here), therefore I will not make it into the office tomorrow.\n
Very Respectfully,\n
Jordan""",

'''Greetings,\n
I’m sorry that I can’t make it in today, (Insert excuse here). I will be available online later in the day.\n
Very Respectfully,\n
Michael''',

'''Good Morning, \n
Unfortunately, I will not be able to make it into the office today, (Insert excuse here). \n
Very Respectfully,\n
Samantha''']

myGenericExcuse = ["My child got sick last night",
"I am feeling under the weather",
"I have a doctors appointment",
"I have a family emergency",
"A family member tested positive for COVID",
"I have to take my dog to the vet",
"My spouse is sick and I have to take care of the baby"]


#Pull random GenericList (1-3)
mainEmail = random.choice(myGenericList)
mainExcuse = random.choice(myGenericExcuse)

print(mainEmail.replace("(Insert excuse here)", mainExcuse))
