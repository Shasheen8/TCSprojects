car_game = ""
started = False
while True:
    car_game = input("> ").lower()
    if car_game == 'start':
        if started:
           print('Car already started')
        else:
            started = True
            print('Car started and is ready to go!')
    elif car_game == 'stop':
        if not started:
          print('Car is already stopped')
        else:
             started = False
             print('Car stopped')
    elif car_game == 'help':
      print("""
 start - start the car
 stop - stop the car 
 quit - to quit      
        """)

    elif car_game == 'quit':
     break
    else:
           print('Sorry I dont  understand this!')
