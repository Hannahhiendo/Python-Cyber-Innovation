#!/bin/python3

from random import randint
player = input('rock (r), paper (p), scissors (s)?')

  

if player == 'r':
  print('''0 vs''', end = ' ')
elif player == 'p':
  print('''___ vs ''', end = ' ')
else: 
  print('''>8 vs ''', end = ' ')

chosen = randint(1,3)


if chosen == 1:
  computer = 'r'
  print('0')

elif chosen == 2:
  computer = 'p'
  print('___')

else:
  computer = 's'
  print('>8')

if player == computer:
  print('DRAW')

elif player == 'r' and computer == 's':
  print('PLAYER WINS')
elif player == 'r' and computer == 'p':
  print('COMPUTER WINS')

elif player == 'p' and computer == 'r':
  print('PLAYER WINS')
elif player == 'p' and computer == 's':
  print('COMPUTER WINS')
  
elif player == 's' and computer == 'p':
  print('PLAYER WINS')
elif player == 's' and computer == 'r':
  print('COMPUTER WINS')