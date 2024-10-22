#№1
##n=int(input())
##if n==14:
##    print("Поздравляю. Вам ровно 14")
##print("Добро пожаловать!" if n>=14 else "Вам ещё рано" if n<=14 else "Поздрявляю! Вам ровно 14")


###№2
##password = input("Введите пароль: ")
##if password == "secret":
##    print("Доступ разрешен!")
##else:
##    print("Неверный пароль!")


#№3
##a=input()
##if a.isdigit():
##    print('число')
##elif a.isalpha():
##    print('Буква')
##else:
##    print('Ни число ни буква')


#№4
#s=0
##a=float(input())
##if a>1000:
##    a=a-a*0.01
##    s+=a
##print(s)
##if 500<=a>=1000:
##    a=a-a*0.05
##s+=a
##print(s)
##if a<500:
##    print(a)


#№5
##k=0
##a,b,c,d,e= map(int, input().split())
##k=a+b+c+d+e
##print(k)



#№6
##a=int(input())
##s=1
##for i in range(2, a+1):
##    s*=i
##print(s)



#№7
##def count_vowels(text):
##    vowels = 'aeiouаеёиоуыэюяАЕЁИОУЫЭЮЯ'
##    count = 0
##    for char in text:
##        if char in vowels:
##            count += 1
##    return count
##
##user_input = input("Введите текст: ")
##vowel_count = count_vowels(user_input)
##print(f"Количество гласных букв в тексте: {vowel_count}")

##def check_password(password):
##    if len(password) < 8:
##        return False
##    if not any(char.isupper() for char in password):
##        return False
##    if not any(char.islower() for char in password):
##        return False
##    if not any(char.isdigit() for char in password):
##        return False
##   Функции не помню











