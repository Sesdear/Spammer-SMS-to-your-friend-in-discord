import pyautogui as pag
'''while not False:
    sg.Popup('YOUR PC IS BROKEN WITH PHP ELEPHANT, PRESS OK TO FIX IT',
              button_color=('black', 'blue')
            )
'''

'''size_screen = pag.size()
print(size_screen)
input_user = int(input("ВЫСОТА НАХУЙ: ")), int(input('ШИРИНА НАХУЙ: '))
a = pag.onScreen(input_user)

if a == True:
    print("You is PHP Terrorist")
    pag.moveTo(input_user)
else:
    print('YOU PHP GAY TRACING')'''

input_user_massege = input('Input you massage : ')
while True:
    pag.typewrite(input_user_massege, 0.05)
    pag.typewrite(['enter'])





