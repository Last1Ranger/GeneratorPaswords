import random
print('Я генератор паролей')
print('Я у мею генерировать 5 типов паролей')
print('1. Пароль состоящий только из цифр.')
print('2. Пароль состоящий только из букв латинского алфавита.')
print('3. Пароль состоящий из цифр и букв латинского языка нижнего регистра')
print('4. Пароль состоящий из цифр и букв латинского языка верхнего регистра')
print('5. Пароль состоящий из цифр и букв латинского языка верхнего и нижнего регистров')
print('Выберете какой пароль хотите сгенерировать, а также введите длину желаемого пароля')
a = int(input())
b = int(input())
if a == 1:
    str1 = '123456789'
    psw = ''.join([random.choice(str1) for x in range(b)])
    print('Ваш пароль:', psw)
    print('Хорошего вам дня!')
if a == 2:
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    psw = ''.join([random.choice(str2) for x in range(b)])
    print('Ваш пароль:', psw)
    print('Хорошего вам дня!')
if a == 3:
    str1 = '123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    ls = str1 + str2
    psw = ''.join([random.choice(ls) for x in range(b)])
    print('Ваш пароль:', psw)
    print('Хорошего вам дня!')
if a == 4:
    str1 = '123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    ls = str1 + str3
    psw = ''.join([random.choice(ls) for x in range(b)])
    print('Ваш пароль:', psw)
    print('Хорошего вам дня!')
if a == 5:
    str1 = '123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    psw = ''.join([random.choice(ls) for x in range(b)])
    print('Ваш пароль:', psw)
    print('Хорошего вам дня!')