

started = False
while True:
    task = input('command> ').lower()
    if task == 'start':
        started = True
        print('Car Started!')
    elif started == True:
        print('Car already started')
    elif task == 'stop':
        print('Car Stopped')
        # if started:
        # print('Car Already stopped')
    elif task == 'help':
        help = '''
                Help!
        Enter start to start the car
        Enter stop or exit to stop or exit the car
        Enter start to exit the car
        '''
        print(help)
    elif task == 'exit' or task == 'quit':
        break
    else:
        print('Please Retry! \nTask not recognized')
else:
    print('Game Exited')
