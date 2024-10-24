# def sonni_top():
#     print("O'ylayotgan soningizni 1 dan 1000 gacha o'ylang.")
#     input("O'ylaganingizdan keyin Enter tugmasini bosing...")

#     past = 1
#     yuqori = 1000
#     urinishlar = 0

#     while past <= yuqori:
#         urinishlar += 1
#         tahmin = (past + yuqori) // 2
#         javob = input(f"Men o'ylayapman: {tahmin}. Bu son (=) to'g'ri, (+) katta yoki (-) kichik? ").lower()

#         if javob == '=':
#             print(f"Men topdim! Siz o'ylagan son {tahmin}.")
#             print(f"Men {urinishlar} urinishda topdim.")
#             break
#         elif javob == '-':
#             yuqori = tahmin - 1
#         elif javob == '+':
#             past = tahmin + 1
#         else:
#             print("Iltimos, '=', '+', yoki '-' deb yozing.")

# sonni_top()
# from math import sqrt

# def tub_sonni_top(son):
#     if son < 2:  
#         return False
#     for i in range(2, int(sqrt(son)) + 1):  
#         if son % i == 0:  
#             return False
#     return True  
# tub=int(input())
# print(tub_sonni_top(tub))
"""tub son 
"""
# max_son=int(input("son kiriting "))
# tub_sonlar=[]

# for son in range(2,max_son+1):
#     tub=True

#     for i in range(2,son):
#         if son%i==0:
#             tub=False
#             break
    
#     if tub:
#         tub_sonlar.append(son)
# print(tub_sonlar)   
# a=input("Ism kiriting ")
# if bool(a):
#     print("Rahmat")
# else:
#     print("Ism kiritmadiz")
# while True:
#     son=int(input("Son kiriting: "))
#     print(f"Siz kiritkan sonning 2-darajasi {son**2}ga teng")
#     savol=input("Yana kiritasizmi yes/no : ").lower()
#     if savol=="yes":
#         continue
#     elif  savol=="no":
#         print("Dastur tugadi ")
#         break
#     else:print("Error")
# while True:
#     yosh=int(input("yilingizni kiriting: "))
#     print(f"sizi yoshiz {2024-yosh}da")
#     savol=input("Chiqish uchun exit deb yozing ").lower()
#     if savol=="exit":
#         print("Dastur tugadi")
#         break
#     else:
#         continue
# password=1060
# xato=0
# while True:
#     parol=int(input("Parol kiriting: "))
#     if parol==password:
#         print(f"{xato+1}-ta urinishda siz parolni tugri topdingiz")
#         break
#     if parol!=password:
#         xato+=1
#         print(f"{3-xato} urinishiz qoldi")
#     if xato==3:
#         while True:
#             print("Xato parol")
# while True:
#     son=input("Son kiriting: (chiqish uchun exit dep yozing: ) : ").lower()
#     if son.isdigit():
#         print(f"{son} ning kvadrati {int(son)**2}")
#     elif son=='exit':
#         print("Dastur tugadi")
#         break

# kitoblar=[]
# while 1:
#     k=input("yaxshi korgan kitobingiz:(chiqish uchun stop dep yozing: ) :  ").lower()
#     if k=='stop':
#         break
#     else:
#         kitoblar.append(k)   
# print(kitoblar)
"""2-mashq"""
# i=1
# while i:
#     yosh=input("yosh kiriting: ").lower()
#     if yosh=='quit' or yosh=='exit':
#         print("dastur tugadi")
#         i=0
#     if yosh.isdigit():
#         if int(yosh)<=7:
#             print("2000 so'm")   
#         elif 7<int(yosh)<=18:
#             print("3000 so'm")
           
#         elif 19<=int(yosh)<=65:
#             print("10000 so'm")
#         else:
#             print("Sizga bepul")
    