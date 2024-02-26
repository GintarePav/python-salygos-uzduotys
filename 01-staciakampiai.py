# Duotos 3 stačiakampių kraštinės. Parašyti programą kuri atspausdintų mažiausiojo plotą.

def spausdintiPlota() :
    def krastine(uzklausosTekstas):
        def ivestiIrValiduoti(uzklausosTekstas):
            krastine = int(input(f'{uzklausosTekstas}'))
            if krastine < 1:
                print("Negalimas ilgis, bandykite dar karta")
                return ivestiIrValiduoti(uzklausosTekstas)
            else:
                return krastine
        krastinesIlgis = ivestiIrValiduoti(uzklausosTekstas)
        return krastinesIlgis

    def plotas(krastine1, krastine2):
        return krastine1 * krastine2
       
    stat1_Kr1 = krastine("Koks pirmo staciakampio pirmosios krastines ilgis? ")
    stat1_Kr2 = krastine("Koks pirmo staciakampio antrosios krastines ilgis? ")
    stat2_Kr1 = krastine("Koks antro staciakampio pirmosios krastines ilgis? ")
    stat2_Kr2 = krastine("Koks antro staciakampio antrosios krastines ilgis? ")
    stat3_Kr1 = krastine("Koks trecio staciakampio pirmosios krastines ilgis? ")
    stat3_Kr2 = krastine("Koks trecio staciakampio antrosios krastines ilgis? ")

    if plotas(stat1_Kr1, stat1_Kr2) < plotas(stat2_Kr1, stat2_Kr2) and plotas(stat1_Kr1, stat1_Kr2) < plotas(stat3_Kr1, stat3_Kr2):
        print(f'Maziausias duotu staciakampiu plotas yra pirmojo - {plotas(stat1_Kr1, stat1_Kr2)} kv. matavimo vnt.')
    elif plotas(stat2_Kr1, stat2_Kr2) < plotas(stat3_Kr1, stat3_Kr2) and plotas(stat2_Kr1, stat2_Kr2) < plotas(stat1_Kr1, stat1_Kr2):
        print(f'Maziausias duotu staciakampiu plotas yra antrojo - {plotas(stat2_Kr1, stat2_Kr2)} kv. matavimo vnt.')
    elif plotas(stat3_Kr1, stat3_Kr2) < plotas(stat1_Kr1, stat1_Kr2) and plotas(stat3_Kr1, stat3_Kr2) < plotas(stat2_Kr1, stat2_Kr2):
        print(f'Maziausias duotu staciakampiu plotas yra treciojo - {plotas(stat3_Kr1, stat3_Kr2)} kv. matavimo vnt.')
    else:
        print(f'Du mazesni staciakampiai yra vienodo ploto - {min(plotas(stat1_Kr1, stat1_Kr2), plotas(stat2_Kr1, stat2_Kr2), plotas(stat3_Kr1, stat3_Kr2))} kv. matavimo vnt.')
    
rezultatas = spausdintiPlota()