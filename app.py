# 1
son = int(input())
if son % 3 == 0 or son % 5 == 0:
    print("Mos son")
else:
    print("Mos emas")


# 2
login = input()
if len(login) < 5 or " " in login:
    print("Noto‘g‘ri login")
else:
    print("To‘g‘ri login")


# 3
parol = input()
has_upper = any(i.isupper() for i in parol)
has_digit = any(i.isdigit() for i in parol)

if has_upper and has_digit:
    print("Kuchli parol")
else:
    print("Kuchsiz parol")


# 4
son = int(input())
if son > 0 and son % 2 == 0:
    print("Musbat juft")
elif son > 0 and son % 2 != 0:
    print("Musbat toq")
else:
    print("Manfiy yoki nol")


# 5
matn1 = input()
matn2 = input()

if len(matn1) == len(matn2):
    print("Uzunligi teng")
else:
    print("Uzunligi teng emas")
