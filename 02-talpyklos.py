# 3V. Laboratorijoje esančioje talpykloje yra x litrų skysčio. Jį reikia supilti į ritinio formos indą, kurio spindulys –r cm, o aukštis –h cm. Parašykite programą, kuri nustatytų, ar skystis tilps inde. Jei taip, programa turi nurodyti, kiek vietos inde dar liko, o jei ne –kiek litrų skysčio liko nesupilta. Ritinio tūrio formulė V=πr2h.

# Testui suvesti skaicius: x=5, r=12, h=10 ir x=20, r=15, h=100

def ivestiVertes(uzklausosTekstas):
    def ivestiIrValiduoti(uzklausosTekstas):
            verte = int(input(f'{uzklausosTekstas}'))
            if verte < 1:
                print("Negalimas dydis, bandykite dar karta")
                return ivestiIrValiduoti(uzklausosTekstas)
            else:
                return verte
    ivestaVerte = ivestiIrValiduoti(uzklausosTekstas)
    return ivestaVerte


skyscioKiekis = ivestiVertes("Kiek litru skyscio turime? ")
ritinioSpindulys = ivestiVertes("Koks ritinio spindulys centimetrais? ")
ritinioAukstis = ivestiVertes("Koks ritinio aukstis centimetrais? ")

ritinioTuris = round(((3.14 * (ritinioSpindulys ** 2)) * ritinioAukstis) * 0.001, 2) # konvertuojame kubinius centimetrus i litrus
print(f'Indo turis = {ritinioTuris}')

def talpintiSkysti():
    if ritinioTuris >= skyscioKiekis:
        likutis = round(ritinioTuris - skyscioKiekis, 2)
        print(f'Skystis inde telpa.\nLaisvos vietos liko {likutis} l.')
    else:
        perteklius = round(skyscioKiekis - ritinioTuris, 2)
        print(f'Skystis inde netelpa.\nLiko nesupilta {perteklius} l.')

arTelpaSkystis = talpintiSkysti()