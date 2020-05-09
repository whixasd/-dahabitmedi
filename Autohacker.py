import os
import time
import sys
soru = input("Hiçbir sorumluluk kabul etmiyoruz eğitim amaçlı kullanacakmısın?:")
if soru.lower().startswith("e"):
    pass
else:
    print("kapatılıyor....")
    sys.exit()
ipadresi = input("ip adresi :")
print("çıkmak için q")
os.system("clear")
time.sleep(4)
def izleritemizle():
    os.system("rm gerek.txt")
    print("İyi günler.")
def tarama(ip):
    global a
    os.system("nmap -n -sV -p- {}".format(ip))
def acıklama():
    a = """
    

 ███

███████╗██╗  ██╗██████╗ ██╗   ██╗██╗     ███████╗███████╗██████╗ 
██╔════╝╚██╗██╔╝██╔══██╗██║   ██║██║     ██╔════╝██╔════╝╚════██╗
█████╗   ╚███╔╝ ██████╔╝██║   ██║██║     ███████╗█████╗   █████╔╝
██╔══╝   ██╔██╗ ██╔═══╝ ██║   ██║██║     ╚════██║██╔══╝  ██╔═══╝ 
███████╗██╔╝ ██╗██║     ╚██████╔╝███████╗███████║███████╗███████╗
╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝
                                                                 
Başlatılıyor....

    """
    print(a)
    time.sleep(1)
    print("""
     nmap scriptlerini otomatik bulur ve exploit eder.""")
def exploitbuluygula():
    global ipadresi
    bul = input("servis ismi:")
    if bul =="q":
        sys.exit()
    else:
        pass



    a = open("gerek.txt","a")
    de = os.listdir("/usr/share/nmap/scripts")
    time.sleep(3)
    os.system("clear")
    for yazdır in de:
        a.write("{} \n".format(yazdır))
    print("""Bulunan uygulanabilecek scriptler:""")
    os.system("grep {} gerek.txt".format(bul))
    secim = input("Uygulamak istiyormusunuz E/H:")

    secim = secim.lower()
    if secim.startswith("e"):
       ismial = input("uygulamak istediğiniz scriptin adı:")

       os.system(f"nmap -n -sV -p- {ipadresi} --script {ismial[:-4]}")


acıklama()
tarama(ipadresi)
exploitbuluygula()
time.sleep(8)
izleritemizle()
