import time,sys,os,keyboard
def main():
    space = " "
    block = ""
    num = 0
    character = "(O_o)"
    intr = "                       |_| |_|"
    while True:
        print("//====================")
        print("||",space*num,character)
        print(intr)
        os.system("cls")
        if keyboard.is_pressed("d"):
            num=num+1
            os.system("cls")
        elif keyboard.is_pressed("a"):
            num=num-1
            os.system("cls")
        elif keyboard.is_pressed("t"):
            break
        elif num == 18:
            intr = "                          |_|"
        elif num == 21:
            intr = "=======================================|    |    |"
        elif num == 43:
            intr = "::::::::::::::::::::::::::::::::::::::::::::::::::::"
        elif num == 51:
            intr = "WARNING: THIS IS FLANCE ATTACKER | WARNING: THIS IS FLANCE ATTACKER"
        elif num == 66:
            intr = "{0_O} \n /|\ \n || "
            character = "(O)"
        elif num == 90:
            intr = "{0OO} \n /____AGA__|TS_\ \n |FA||| "
            character = "(O)"
        elif num == 0:
            intr == "========================================"
        print("X=",num)
print("POWER INTOR BETA")
print("Press E to play game.")
keyboard.wait("e")
main()
    
    

