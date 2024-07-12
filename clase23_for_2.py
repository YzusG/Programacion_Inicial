numero = [2,4,5,7,8,122,123,45, -5, -3]
from colorama import init, Fore, Back, Style


init()
print(Fore.GREEN)
# for num in numero:
#     if(num %2 ==0):
#         print(num)
#     else:
#         continue
print("\033[H\033[J")  # Limpiamos la pantalla


for num in numero:
    if(num %2 ==0):
        print(f"{num} es par")
    else:
        print(f"{num} es impar")