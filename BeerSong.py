from locale import str

from __builtin__ import range

def  Ninety_Nine_Bottles_of_Beer():
    for i in range(99, 0, -1):
        if i == 1:
            print(
            "1 bottle of beer on	the	wall, 1 bottle of beer take	one	down, pass it around, no more bottles of beer on the wall.")
        else:
            print(str(i) + " bottle of beer on the wall, 1 bottle of beer take one down, pass it around, "
                  + str(i - 1) + " bottles of beer on the wall.")

def main():
    Ninety_Nine_Bottles_of_Beer()

main()