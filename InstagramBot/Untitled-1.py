import re
def MaxValue(sayi,maxdeger):
    sayi = str(sayi)
    for i in sayi:
        if(int(i) > maxdeger):
             return False
        return True
def OndalıkAl(n: float) -> float:
    return float(re.search(r'\.\d+', str(n)).group(0))
def OnlukCevir(sayi,taban):
    if taban == 2:
            Liste = ""
            while(sayi > 0):
                kalan = sayi % 2
                sayi = int(sayi/2)
                Liste = Liste + str(kalan)
            Liste= Liste[::-1]
            return int(Liste)
def OndalıklıOnlukCevir(sayi,taban):
    if (taban==2):
        virguloncesi = OnlukCevir(int(sayi),2)
        liste = ""
        virgulsonrasi = OndalıkAl(sayi)
        while(virgulsonrasi>0.20):
            virgulsonrasi = OndalıkAl(sayi)
            ondalık = virgulsonrasi * 2
            virgulsonrasi= OndalıkAl(ondalık)
            liste = liste + str(int(ondalık))
        return liste
       
#def İkilikCevir(sayi,taban):
    #if not MaxValue(sayi,1):

#print(str(OndalıkAl(20.32)))
print(str(OndalıklıOnlukCevir(41.6875,2)))
