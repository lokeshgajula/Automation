import random

NUM_OF_QUESTIONS = 20
NUM_OF_SETS = 35

capitals = {'Andhra Pradesh': 'Amaravati',
 'Arunachal Pradesh': 'Itanagar',
 'Assam': 'Dispur',
 'Bihar': 'Patna',
 'Chhattisgarh': 'Naya Raipur',
 'Goa': 'Panaji',
 'Gujarat': 'Gandhinagar',
 'Haryana': 'Chandigarh',
 'Himachal Pradesh': 'Shimla',
 'Jharkhand': 'Ranchi',
 'Karnataka': 'Bangalore',
 'Kerala': 'Thiruvananthapuram',
 'Madhya Pradesh': 'Bhopal',
 'Maharashtra': 'Mumbai',
 'Manipur': 'Imphal',
 'Meghalaya': 'Shillong',
 'Mizoram': 'Aizawl',
 'Nagaland': 'Kohima',
 'Odisha': 'Bhubaneswar',
 'Punjab': 'Chandigarh',
 'Rajasthan': 'Jaipur',
 'Sikkim': 'Gangtok',
 'State': 'Capital',
 'Tamil Nadu': 'Chennai',
 'Telangana': 'Hyderabad',
 'Tripura': 'Agartala',
 'Uttar Pradesh': 'Lucknow',
 'Uttarakhand': 'Dehradun,',
 'West Bengal': 'Kolkata'}

for setnum in range(NUM_OF_SETS):
    quizFile = open(f'sets\\capitalsquiz{setnum+1}.txt','w')
    answerKeyFile = open(f'sets\\capitalsquiz_ansers{setnum+1}.txt','w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20) + f'State Capitals Quiz  (Form{setnum+1})')
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(NUM_OF_QUESTIONS):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write(f'{questionNum +1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}.{ answerOptions[i]}\n")
        quizFile.write('\n')

        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]} ")
    quizFile.close()
    answerKeyFile.close()
        
    
