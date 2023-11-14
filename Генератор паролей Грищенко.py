import random  # импорт библиотеки
def generatepassword1():       # задаем функции для каждого пароля(хотя как мне кажется в данном проекте они излишни)

        str1 = '123456789'
        psw = ''.join([random.choice(str1) for x in range(b)])
        print('Ваш пароль:', psw)
        print('Хорошего вам дня!')
def generatepassword2():
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    psw = ''.join([random.choice(str2) for x in range(b)])
    print('Ваш пароль:', psw)
    print('Хорошего вам дня!')
def generatepassword3():
    str1 = '123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    ls = str1 + str2
    psw = ''.join([random.choice(ls) for x in range(b)])
    print('Ваш пароль:', psw)
    print('Хорошего вам дня!')
def generatepassword4():
    str1 = '123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    ls = str1 + str3
    psw = ''.join([random.choice(ls) for x in range(b)])
    print('Ваш пароль:', psw)
    print('Хорошего вам дня!')
def generatepassword5():
    str1 = '123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    psw = ''.join([random.choice(ls) for x in range(b)])
    print('Ваш пароль:', psw)
    print('Хорошего вам дня!')
print('Я генератор паролей')# приветственное сообщение
print('Я у мею генерировать 5 типов паролей')
print('1. Пароль состоящий только из цифр.')
print('2. Пароль состоящий только из букв латинского алфавита.')
print('3. Пароль состоящий из цифр и букв латинского языка нижнего регистра')
print('4. Пароль состоящий из цифр и букв латинского языка верхнего регистра')
print('5. Пароль состоящий из цифр и букв латинского языка верхнего и нижнего регистров')
print('Выберете какой пароль хотите сгенерировать, а также введите длину желаемого пароля')
a = int(input()) # выбор типа пароля
b = int(input()) # выбор длинны пароля
if a == 1:
    generatepassword1()
if a == 2:
    generatepassword2()
if a == 3:
    generatepassword3()
if a == 4:
    generatepassword4()
if a == 5:
    generatepassword5()