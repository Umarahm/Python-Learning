# print("Welcome to Roller Coster")
# height=int(input('Enter your height:'))
# price=0
# if height>=160:
#   age=int(input("Enter your age: "))
#   if age < 12:
#     price=5
#     print(f"PLEASE PAY {price}$")
#   elif age >= 12 and age <18:
#     price=7
#     print(f"PLEASE PAY {price}$")
#   elif age>=45 and age <= 55:
#     price=0
#     print("Sorry about midlife crisis FREEEEEE BABYYYYY")
#     print(f"PLEASE PAY {price}$")
#   else:
#     price = 10
#     print(f"PLEASE PAY {price}$")
    
#   wants_photo=input("Enter Y to add photo and N to not add photo")
#   if wants_photo == 'Y':
#     price=price+3
#     print(price)
#   else:
#     price=price+0
#     print(price)
# else:
#   print("Height not above 160cm not allowed")

# Which year do you want to check?
# year = int(input())

# if(year % 4==0):
#   if(year % 100 == 0):
#     if(year % 400 == 0):
#       print("Leap year")
#     else:
#       print('Not leap year')
#   else:
#     print('Leap year')
# else:
#   print("Not leap year")

print('''  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/''')

print("Welcome to the Treasure hunt Challenge")
print("Your mission is to Reach the final door and aquire the treaure")
print("You are a pesky Pirate AAAARRGH MATEY!!")
print('''                                    # #  ( )
                                  ___#_#___|__
                              _  |____________|  _
                       _=====| | |            | | |==== _
                 =====| |.---------------------------. | |====
   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
     \                                                             /
      \_______________________________________________WWS_________/
  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww ''')
choice1=input("You are enroute to the ISLAND in your ship but you have to make a tough choice to take left 'L' or right 'R'::")
if choice1 == 'L':
  print("Congratulations! you've made the right choice")
  print("You are one step closer to the TREASURE CHEST!!")
  print("***************************************************************************************************************")
  print("You are Walking on the way to the 'X'mark and you come across a river!!")
  choice2=input("Press 'W' to wait for a nearby canoe or press 'S' to swim with your crew::")
  if choice2 == 'W': 
    print("RESPECTS!!! \n You Hath Snubbed the Title of a Pesky Pirate and lowered your head to board a public canoe ")
    print("You have reached the X spot on your MAP!!! \n Now you see 3 different doors Red , Yellow and Blue")
    choice3=input("Enter R for red door \n Enter Y for yellow door \n Enter B for blue door")
    if choice3 == 'Y':
      print("CONGRATULATIONS PIRATE YOU'VE SUCCESSFULLY REACHED THE TREASURE \n Party at the rich crew's deck ")
    elif choice3 == 'B':
      print("You've found a room filled with SKULLS")
      print('''   (
          ;
         | |
         | |
        ,`-'.
       ( O O )
        ( ^ )
         HHH    ''')
    else:
      print("YOU HATH REACHETH NOTHINGNESS AS THYSELF!!!!")
  else:
    print("THERE WERE ALLIGATORS IN THE WATERS!!!!  RAAAAAAAAAH \n You die a painful death")
    print('''           .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
          snd                         (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-''')
else:
  print("The RIGHT path isn'nt always the right path my child! \n Your boat gets caught up in a STORMMM \n aaaaaaaaand you die")
  print('''     %%% %%%%%%%            |#|
    %%%% %%%%%%%%%%%        |#|####
  %%%%% %         %%%       |#|=#####
 %%%%% %   @    @   %%      | | ==####
%%%%%% % (_  ()  )  %%     | |    ===##
%%  %%% %  \_    | %%      | |       =##
%    %%%% %  u^uuu %%     | |         ==#
      %%%% %%%%%%%%%      | |           V''')
      
  
  