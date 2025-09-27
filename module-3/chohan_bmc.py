
"""
chohan_bmc.py - Modified Cho-Han game for Module 3
Brennan Cheatwood
Assignment: 3.2

Changes made (Brownfield):
1) Input prompts changed to "bmc: " instead of ">" for both bet amount and CHO/HAN selection.
2) House fee increased from 10% to 12%.
3) Program intro now includes a notice: if the dice TOTAL is 2 or 7, player gets a 10 mon bonus.
4) Whenever the dice TOTAL is 2 or 7, output a message showing the total and award +10 mon to the purse.
5) Saved as chohan_bmc.py with inline comments marking changes.
"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han (Modified), by Brennan Cheatwood

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

NOTICE: If the dice total is exactly 2 or 7, you receive a 10 mon bonus!
''')  # <-- (3) Added notice about 2 or 7 bonus.

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('bmc: ')  # <-- (1) Prompt changed to "bmc: "
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('bmc: ').upper()  # <-- (1) Prompt changed to "bmc: "
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot  # Add the pot from player's purse.
        house_fee = (pot * 12) // 100  # <-- (2) 12% house fee
        print('The house collects a', house_fee, 'mon fee.')
        purse = purse - house_fee      # <-- (2) Apply 12% fee
    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('You lost!')

    # (4) Check for 2-or-7 total bonus (applies regardless of win/lose)
    total = dice1 + dice2
    if total in (2, 7):
        print(f'Lucky total {total}! You get a 10 mon bonus.')
        purse += 10

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
