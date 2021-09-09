import random
pass_input = input('(Yes or No) Would you like to generate a password? ').lower()
if pass_input == 'yes':
    pass_input_choice = input("(Yes or No) Would you like to have symbols and numbers in your password? ".lower())
    if pass_input_choice == 'yes':
        choice = input('(Choose: S,N or B) Symbol, numbers or both of them? ').lower()
        class really_hard_stuff():
            if choice == 'b':
                print('Thank you, generating password')
                char = ['a','b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                num = ['1','2','3','4','5','6','7','8','9','10']
                sym = ['#','<','?','>',',','.','*','^','%','£','$']
                # b
                b_pass_1 = random.choice(char) + random.choice(num) + random.choice(sym) + random.choice(char) + random.choice(num) + random.choice(sym) 
                b_pass_2 = random.choice(char) + random.choice(num) + random.choice(sym) + random.choice(char) + random.choice(num) + random.choice(sym) 
                b_pass_3 = random.choice(char) + random.choice(num) + random.choice(sym) + random.choice(char) + random.choice(num) + random.choice(sym) 
                b_pass_4 = random.choice(char) + random.choice(num) + random.choice(sym) + random.choice(char) + random.choice(num) + random.choice(sym) 
                b_pass_5 = random.choice(char) + random.choice(num) + random.choice(sym) + random.choice(char) + random.choice(num) + random.choice(sym) 
                # s
                s_pass_1 = random.choice(char) + random.choice(sym) + random.choice(char) + random.choice(sym) +  random.choice(char) + random.choice(sym)
                s_pass_2 = random.choice(char) + random.choice(sym) + random.choice(char) + random.choice(sym) +  random.choice(char) + random.choice(sym) 
                s_pass_3 = random.choice(char) + random.choice(sym) + random.choice(char) + random.choice(sym) +  random.choice(char) + random.choice(sym) 
                s_pass_4 = random.choice(char) + random.choice(sym) + random.choice(char) + random.choice(sym) +  random.choice(char) + random.choice(sym) 
                s_pass_5 = random.choice(char) + random.choice(sym) + random.choice(char) + random.choice(sym) +  random.choice(char) + random.choice(sym)  
                print('Listing five passwords.')
                print(f'Password 1: {b_pass_1}')
                print(f'Password 2: {b_pass_2}')
                print(f'Password 3: {b_pass_3}')
                print(f'Password 4: {b_pass_4}')
                print(f'Password 5: {b_pass_5}')
            elif choice == 's':
                char = ['a','b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                num = ['1','2','3','4','5','6','7','8','9','10']
                sym = ['#','<','?','>',',','.','*','^','%','£','$']
                s_pass_1 = random.choice(char) + random.choice(sym) + random.choice(char) + random.choice(sym) +  random.choice(char) + random.choice(sym)
                s_pass_2 = random.choice(char) + random.choice(sym) + random.choice(char) + random.choice(sym) + random.choice(char) + random.choice(sym) 
                s_pass_3 = random.choice(char) + random.choice(sym) + random.choice(char) + random.choice(sym) + random.choice(char) + random.choice(sym) 
                s_pass_4 = random.choice(char) + random.choice(sym) + random.choice(char) + random.choice(sym) + random.choice(char) + random.choice(sym) 
                s_pass_5 = random.choice(char) + random.choice(sym) + random.choice(char) + random.choice(sym) + random.choice(char) + random.choice(sym)  
                print('Thank you, generating password')
                print(f'Password 1: {s_pass_1}')
                print(f'Password 1: {s_pass_2}')
                print(f'Password 1: {s_pass_3}')
                print(f'Password 1: {s_pass_4}')
                print(f'Password 1: {s_pass_5}')

            elif choice == 'n':
                char = ['a','b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                num = ['1','2','3','4','5','6','7','8','9','10']
                sym = ['#','<','?','>',',','.','*','^','%','£','$']
                n_pass_1 = random.choice(char) + random.choice(num) + random.choice(char) + random.choice(num) +  random.choice(char) + random.choice(num)
                n_pass_2 = random.choice(char) + random.choice(num) + random.choice(char) + random.choice(num) + random.choice(char) + random.choice(num) 
                n_pass_3 = random.choice(char) + random.choice(num) + random.choice(char) + random.choice(num) + random.choice(char) + random.choice(num) 
                n_pass_4 = random.choice(char) + random.choice(num) + random.choice(char) + random.choice(num) + random.choice(char) + random.choice(num) 
                n_pass_5 = random.choice(char) + random.choice(num) + random.choice(char) + random.choice(num) + random.choice(char) + random.choice(num)  
                print('Thank you, generating password')
                print(f'Password 1: {n_pass_1}')
                print(f'Password 1: {n_pass_2}')
                print(f'Password 1: {n_pass_3}')
                print(f'Password 1: {n_pass_4}')
                print(f'Password 1: {n_pass_5}')                

else:
    print('Thank you, goodbye.')


