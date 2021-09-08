import random
class Pass():
    pass_input = input('(Yes or No) Would you like to generate a password? ').lower()
    if pass_input == 'yes':
        print('Thank you, generating password')
        abc = ['a','b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        abc_1 = random.choice(abc) + random.choice(abc) + random.choice(abc) + random.choice(abc) + random.choice(abc) + random.choice(abc)
        abc_2 = random.choice(abc) + random.choice(abc) + random.choice(abc) + random.choice(abc) + random.choice(abc) + random.choice(abc)
        abc_3 = random.choice(abc) + random.choice(abc) + random.choice(abc) + random.choice(abc) + random.choice(abc) + random.choice(abc)
        abc_4 = random.choice(abc) + random.choice(abc) + random.choice(abc) + random.choice(abc) + random.choice(abc) + random.choice(abc)
        abc_5 = random.choice(abc) + random.choice(abc) + random.choice(abc) + random.choice(abc) + random.choice(abc) + random.choice(abc)
        print('Listing five passwords.')
        print(f'Password 1: {abc_1}')
        print(f'Password 2: {abc_2}')
        print(f'Password 3: {abc_3}')
        print(f'Password 4: {abc_4}')
        print(f'Password 5: {abc_5}')
    else:
        print('Thank you, goodbye.')

