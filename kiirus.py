
nimi = str(input("Sisestage oma nimi: "))
lubatud = int(input("Sisestage lubatud kiirus: "))
tegelik = int(input("Sisestage tegelik kiirus: "))
trahv = (int(tegelik) - int(lubatud)) * 3
trahv = min(trahv,190)
print(f"{nimi} kiiruse ületamise eest on teie trahv {trahv}")









