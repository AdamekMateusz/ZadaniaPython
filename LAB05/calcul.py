from complex_num import *
import sys
import keyboard

def get_real_get_img(number_str):
    if number_str.find('+') != -1:
        plus_sign = number_str.find('+')
        real_num = number_str[:plus_sign]
        
        real_num = real_num.replace(" ",'')
        real_num = int(real_num)
        img_num  = number_str[plus_sign+1:]
        img_num = img_num.replace(" ",'')

        img_num = [img_num.replace(x,'') for x in ('i','j') if x in img_num][0]

        img_num = int(img_num)
        return real_num, img_num

    elif number_str.find('-') != -1:
        minus_sign = number_str.find('-')
        real_num = number_str[:minus_sign]
        
        real_num = real_num.replace(" ",'')
        real_num = int(real_num)

        img_num  = number_str[minus_sign+1:]
        img_num = img_num.replace(" ",'')
        img_num = [img_num.replace(x,'') for x in ('i','j') if x in img_num][0]
        img_num = '-' + img_num
        img_num = int(img_num)
        return real_num, img_num
    else:
        raise 




if __name__ == '__main__':
    while True:
        print('\033[92m', 'Use operator (+, -, *, /)','\033[0m')
        # print('\033[91m', 'Press ESC if you want exit','\033[0m')
        first_number = input("First number: ")
        operator = input("Operator: ")
        secound_number = input("Secound number: ")
        # first_number = '4+6j'
        # operator = '+'
        # secound_number = '4+5j'

        first_number = get_real_get_img(first_number)
        secound_number = get_real_get_img(secound_number)

        first_number = Complex(first_number[0],first_number[1])
        secound_number = Complex(secound_number[0],secound_number[1])

        if operator == '+':
            result = first_number + secound_number
        elif operator == '-':
            result = first_number - secound_number
        elif operator == '*':
            result = first_number * secound_number
        elif operator == '/':
            result = first_number / secound_number 
        
        print('result: ',result)

        # if keyboard.is_pressed('Esc'):
        #     print("\nyou pressed Esc, so exiting...")
        #     sys.exit(0)
