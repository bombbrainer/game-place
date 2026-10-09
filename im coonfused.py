# this was confusing
death='you have died'
choice = input('would you like to enter the forest or the castle <')
if choice.lower()=='the forest':
    choice  = input(' you walk into the forest and come acrost a frog do you touch it or leave it <')
    if choice.lower()=='touch it':
        print('you have died the frog was poisonous')
    elif choice.lower()=='leave it':
        print('you walk past the frog but you are now hungry')
        choice = input('you find a mushroom do you eat it or leave it <')
        if choice.lower()=='eat it':
            print(f'{death} it was poisonous')
        elif choice.lower()=='leave it':
            print(f'{death} you starved to death')
elif choice.lower()=='the castle':
    choice = input('you walk into the castle and are welcomed in do you head to the king or to the mess hall <')
    if choice.lower()=='the king':
        choice = input('you walk in the direction of the king but the gaurds stop you saying the king is asleep do you push past or go to the mess hall <')
        if choice.lower()=='push past':
            print(f'{death} the gaurds stabbed you like what did you expect')
        elif choice.lower()=='the mess hall':
            print('as you enter the mess hall you start to feel hungry')
            choice = input('do you get food (cheap) or do you walk past into the market <')
            if choice.lower()=='walk to the market': 
                print('you are super hungry now')
                choice = input('do you buy food or do you steal food <')
                if choice.lower()=='buy food':
                    print('you buy food but have no money left you are no longer hungry')
                    choice = input('do you head to the king or to the wizard')
                    if choice.lower()=='the wizard':
                        choice = input('the wizard says he must be paid to help you wake up the king do you leave the castle or head to the king <')
    elif choice.lower()=='the mess hall':
        print('as you enter the mess hall you start to feel hungry')
        choice = input('do you get food (cheap) or do you walk past into the market <')
        if choice.lower()=='walk to the market':
            print('you are super hungry now')
            choice = input('do you buy food or do you steal food <')
            if choice.lower()=='buy food':
                print('you buy food but have no money left you are no longer hungry')
                choice = input('do you head to the king or to the wizard<')
                if choice.lower()=='the wizard':
                    choice = input('the wizard says he must be paid to help you wake up the king do you leave the castle or head to the king <')