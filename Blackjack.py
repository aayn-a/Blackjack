 
import random
import os
import time


# setting up deck and hands
while True:

  os.system('clear')
  cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K", "A", "A", "A", "A"]

  # aces can be 1 or 11
    # if you have [8, 2, A] -> A=11 
    # if you have [8, 9, A] -> A=1
    # [A, 5] you will tell them that their sum is 16 or 6 and recalculate if they hit
    # [A, 5, K]

  # always make Aces 11 unless it makes them bust
  # if you have [A, A, A], some A's can be 1 and others can 11

  player = []
  dealer = []

  for i in range(2):
    l = random.choice(cards)
    cards.remove(l)
    player.append(l)
  for i in range(2):
    l = random.choice(cards)
    cards.remove(l)
    dealer.append(l)




  print(player)

  # you only need to modify this function
  def sum(h):
    # sum up the hands
    sumOfPlayer = 0
    numOfAces = 0
    for i in range(len(h)):
      if h[i] ==  "J" or h[i] ==  "Q" or h[i] ==  "K":
        sumOfPlayer += 10
      elif h[i] == "A":
        sumOfPlayer += 1 # we need to add the minimum value rof each ace
        numOfAces += 1 # keeps track of how many aces we have
      else:
        sumOfPlayer += h[i]
    for i in range(numOfAces):
      if sumOfPlayer + 10 <=21:
        sumOfPlayer += 10
      
        

    return sumOfPlayer
      


  dealersturn = False
  playersturn = True
  print("Dealer's First card is a " , dealer[0])
  if sum(player) == 21:
    print('Blackjack! You win!')
    time.sleep(5)
    playersturn = False
    
  elif sum(player) > 21:
    print("Bust at the start")
    time.sleep(5)
    playersturn = False

  while playersturn:
    move = input("Hit or Stay? ")
    if move == 'h' or move == "hit":
      l = random.choice(cards)
      player.append(l)
      cards.remove(l)
      print(player)
      x = sum(player)
    if move=="done":
      break
      if x > 21:
        print("Bust")
        time.sleep(5)
        break

      if x == 21:
        print("Blackjack")
        time.sleep(5)
        break
      print("Dealer's First card" , dealer[0])
      
    elif move == "s" or move == "stay":
      dealersturn = True
      break

  while dealersturn:
      print(dealer)
      z = sum(player)
      j = sum(dealer)
      print("Dealer's sum: " + str(j))
      if j == 21:
        print("Dealer's Blackjack, you lose")
        time.sleep(5)
        break
      elif j > 21:
        print("Dealer's Bust! You win!")
        time.sleep(5)
        break
      elif j > z:
        print("Dealer wins")
        time.sleep(5)
        break
      else: 
        l = random.choice(cards)
        dealer.append(l)
        cards.remove(l)
        


            
        

        

        
            

      
        


