print('Hello our beautiful user ! please enter your name')
Name = input()
print('Welcome ' + Name )
print('Please enter your age so we know what calculations are needed')
Age = input()
print('Thank you ' + Name)
if int(Age) == int(0) or int(Age) <= int(0) or int(Age) >= int(100):
  print('Sorry you are dead')
  print('You can not use the calculator')
  
if int(Age) == int(1) and int(Age) <= int(9):
  print('Choose from the following calculations')
  print('Addition = 1 / Substraction = 2')
  AnswerIf1 = input()
  
  if int(AnswerIf1) == int(1):
    print('Enter two numberes in two different lines for addition')
    AnIf_1 = input()
    AnIf_2 = input()
    Sum_AnIf_1 = (float(AnIf_1) + float(AnIf_2))
    print('Your answer is')
    print(Sum_AnIf_1)
    
  if int(AnswerIf1) == int(2):
    print('Enter two number in two different lines for substraction')
    AnIf_3 = input()
    AnIf_4 = input()
    Sum_AnIf_2 = (float(AnIf_3) - float(AnIf_4))
    print('Your answer is')
    print(Sum_AnIf_2)
    
if int(Age) == int(10) and int(Age) <= int(12):
  print('Choose from the following calculations')
  print('Addition = 1 / Substraction = 2 / Multiplication = 3')
  AnswerIf3 = input()
  
  if int(AnswerIf3) == int(1):
    print('Enter two numbers in two different lines for addition')
    IfAnswer1 = input()
    IfAnswer2 = input()
    Sum_If_Answer_1 = (float(IfAnswer1) + float(IfAnswer2))
    print('Your answer is')
    print(Sum_If_Answer_1)
    
  if int(AnswerIf3) == int(2):
    print('Enter two numbers in two different lines substraction')
    IfAnswer3 = input()
    IfAnswer4 = input()
    Sum_If_Answer_2 = (float(IfAnswer3) - float(IfAnswer4))
    print('Your answer is')
    print(Sum_If_Answer_2)
    
  if int(AnswerIf3) == int(3):
    print('Enter two numbers in two different lines for multiplication')
    IfAnswer5 = input()
    IfAnswer6 = input()
    Sum_If_Answer_3 = (float(IfAnswer5) * float(IfAnswer6))
    print('Your answer is')
    print(Sum_If_Answer_3)
    
if int(Age) == int(13) :
  print('Choose from the following calculations')
  print('Addition = 1 / Substraction = 2 / Muiltiplication = 3 / Division = 4 / Power {Index} {Exponent} = 5')
  AnswerIf2 = input()
  
  if int(AnswerIf2) == int(1):
    print('Enter two numbers in two different lines for addition')
    AIf_1 = input()
    AIf_2 = input()
    Sum_AIf_1 = (float(AIf_1) + float(AIf_2))
    print('Your answer is')
    print(Sum_AIf_1)
    
  if int(AnswerIf2) == int(2):
    print('Enter two numbers in two different lines for substraction')
    AnsIf_1 = input()
    AnsIf_2 = input()
    Sum_AnsIf_1 = (float(AnsIf_1) - float(AnsIf_2))
    print('Your answer is')
    print(Sum_AnsIf_1)
    
  if int(AnswerIf2) == int(3):
    print('Enter two numbers in two different lines for multiplication')
    AnswIf_1 = input()
    AnswIf_2 = input()
    Sum_AnswIf_1 = (float(AnswIf_1) * float(AnswIf_2))
    print('Your answer is')
    print(Sum_AnswIf_1)
    
  if int(AnswerIf2) == int(4):
    print('Enter two numbers in two different lines for division')
    AnsweIf_1 = input()
    AnsweIf_2 = input()
    Sum_AnsweIf_1 = (float(AnsweIf_1) / float(AnsweIf_2))
    print('Your answer is')
    print(Sum_AnsweIf_1)
    
  if int(AnswerIf2) == int(5):
    print('Enter two numbers in two different lines for power {index} {exponent}')
    AwI_9 = input()
    AwI_10 = input()
    Sum_AwI_5 = (float(AwI_9) ** float(AwI_10))
    print('Your answer is')
    print(Sum_AwI_5)
    
if int(Age) >= int(14) and int(Age) <= int(100):
  print('Choose from the following calculations')
  print('Addition = 1 / Substraction = 2 / Muiltiplication = 3 / Division = 4 / Power {Index} {Exponent} = 5 / Integer Division = 6 / Remainder = 7')
  AnswerIf4 = input()
  
  if int(AnswerIf4) == int(1):
    print('Enter two numbers in two different lines for addition')
    AI_1 = input()
    AI_2 = input()
    Sum_AI_1 = (float(AI_1) + float(AI_2))
    print('Your answer is')
    print(Sum_AI_1)
    
  if int(AnswerIf4) == int(2):
    print('Enter two numbers in two different lines for substraction')
    AI_3 = input()
    AI_4 = input()
    Sum_AI_2 = (float(AI_3) - float(AI_4))
    print('Your answer is')
    print(Sum_AI_2)
    
  if int(AnswerIf4) == int(3):
    print('Enter two numbers in two different lines for multiplication')
    AI_5 = input()
    AI_6 = input()
    Sum_AI_3 = (float(AI_5) * float(AI_6))
    print('Your answer is')
    print(Sum_AI_3)
    
  if int(AnswerIf4) == int(4):
    print('Enter two numbers in two different lines for division')
    AI_7 = input()
    AI_8 = input()
    Sum_AI_4 = (float(AI_7) / float(AI_8))
    print('Your answer is')
    print(Sum_AI_4)
    
  if int(AnswerIf4) == int(5):
    print('Enter two numbers in two different lines for power {index} {exponent}')
    AI_9 = input()
    AI_10 = input()
    Sum_AI_5 = (float(AI_9) ** float(AI_10))
    print('Your answer is')
    print(Sum_AI_5)
    
  if int(AnswerIf4) == int(6):
    print('Enter two numbers in two different lines for integer division')
    AI_11 = input()
    AI_12 = input()
    Sum_AI_6 = (float(AI_11) // float(AI_12))
    print('Your answer is')
    print(Sum_AI_6)
    
  if int(AnswerIf4) == int(7):
    print('Enter two numbers in two different lines for remainder')
    AI_13 = input()
    AI_14 = input()
    Sum_AI_7 = (float(AI_13) % float(AI_14))
    print('Your answer is')
    print(Sum_AI_7)

print('Do you want to continue using the calculator?')
Answer_Con = input()

    
print('Thank you for choosing us this time')
print('See you next time')
print('Bye')
Bye = input()

if Bye == ('bye') or Bye == ('Bye') or Bye == ('bYe') or Bye == ('byE') or Bye == ('BYe') or Bye == ('bYE') or Bye == ('ByE') or Bye == ('BYE'):
  print('Thank you so much for answering me')
  print('BYE!') 