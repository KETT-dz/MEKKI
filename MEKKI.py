import os
import time

def logo():
    print("""
███    ███ ███████ ██   ██ ██ ██
████  ████ ██       ██ ██  ██ ██
██ ████ ██ █████     ███   ██ ██
██  ██  ██ ██       ██ ██  ██ ██
██      ██ ███████ ██   ██ ██ ███████

      أداة MEKKI
===============================
""")

def info():
    os.system("clear")
    logo()
    print("معلومات الجهاز:")
    os.system("uname -a")
    print("\nIP العام:")
    os.system("curl -s ifconfig.me")
    input("\nاضغط Enter للرجوع...")

def dz_script():
    os.system("clear")
    logo()
    print("هذا سكربتش تجريبي داخل أداة MEKKI")
    print("✔ يعمل بنجاح")
    input("\nاضغط Enter للرجوع...")

def main():
    while True:
        os.system("clear")
        logo()
        print("1 - معلومات الجهاز")
        print("2 - سكربتش تجريبي")
        print("3 - خروج")
        print("===============================")

        choice = input("اختيارك: ")

        if choice == "1":
            info()
        elif choice == "2":
            dz_script()
        elif choice == "3":
            print("وداعاً...")
            time.sleep(1)
            break
        else:
            print("خيار غير صحيح!")
            time.sleep(1)

main()
