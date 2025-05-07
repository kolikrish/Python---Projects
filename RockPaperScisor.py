import random
item_list = ['Rock','Paper','Scissor']

print('Rock , Paper , Scissor')
user_choice = input('Enter your move : ')
compu_choice = random.choice(item_list)

print(f'User choice = {user_choice} , Computer choice = {compu_choice}')

if user_choice == compu_choice:
    print('Both chooses same : = Match Tie')

elif user_choice == 'Rock':
    if compu_choice == 'Paper':
        print('Paper covers Rock = Computer Win')
    else:
        print('Rock smashes scissor = You Win')


elif user_choice == 'Paper':
    if compu_choice == 'Scissor':
        print('Scissor cuts paper , Computer Wins')
    else:
        print('Paper covers rock , You Win')

elif user_choice == 'Scissor':
    if compu_choice == 'Paper':
        print('Scissor cuts paper , You Win')
    else:
        print('Rock Smashes Scissor , Computer Win')

