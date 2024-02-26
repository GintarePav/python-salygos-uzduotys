# Knygynuose knygų populiarumas nustatomas pagal parduotų egzempliorių skaičių –kuo daugiau knygos egzempliorių parduota, tuo knyga populiaresnė. Parenkite programą, kuri nustatytų populiariausią knygą iš 3 naujausių knygų. Knygą apibūdina kodas k (triženklis sveikasis skaičius) ir parduotų egzempliorių skaičius s. Jeigu yra kelios populiariausios knygos, tai turi būti pateikti jų visų kodai.

def ivestiKoda(uzklausosTekstas):
    def ivestiIrValiduoti(uzklausosTekstas):
            kodas = str(int(input(f'{uzklausosTekstas}')))
            if int(kodas) > 0 and len(kodas) == 3:
                return kodas
            else:
                print("Negalimas kodo formatas, bandykite dar karta")
                return ivestiIrValiduoti(uzklausosTekstas)
    ivestasKodas = ivestiIrValiduoti(uzklausosTekstas)
    return ivestasKodas

def ivestiEgzempliorius(uzklausosTekstas):
    def ivestiIrValiduoti(uzklausosTekstas):
        egzemplioriai = int(input(f'{uzklausosTekstas}'))
        if egzemplioriai < 0:
            print("Negalimas skaicius, bandykite dar karta")
            return ivestiIrValiduoti(uzklausosTekstas)
        else: 
            return egzemplioriai
    egzemploriuSkaicius = ivestiIrValiduoti(uzklausosTekstas)
    return egzemploriuSkaicius


kodas1 = ivestiKoda('Parasykite trizenkli pirmosios knygos koda: ')
parduota1 = ivestiEgzempliorius('Parasykite kiek pirmosios knygos egzemploriu buvo parduota: ')

kodas2 = ivestiKoda('Parasykite trizenkli antrosios knygos koda: ')
parduota2 = ivestiEgzempliorius('Parasykite kiek antrosios knygos egzemploriu buvo parduota: ')

kodas3 = ivestiKoda('Parasykite trizenkli treciosios knygos koda: ')
parduota3 = ivestiEgzempliorius('Parasykite kiek treciosios knygos egzemploriu buvo parduota: ')

def ispausdintiAtaskaita():
    didziausias = None
    reikiamasKodas = ""

    def pridetiKoda(kodas):
        nonlocal reikiamasKodas
        reikiamasKodas += f' {kodas}'
        
    def rastiDidziausia():
        nonlocal didziausias, reikiamasKodas
        if parduota1 >= parduota2:
            didziausias = parduota1
            reikiamasKodas = kodas1
        else: 
            didziausias = parduota2
            reikiamasKodas = kodas2

        if parduota3 > didziausias:
            didziausias = parduota3
            reikiamasKodas = kodas3

        return didziausias, str(reikiamasKodas)
    
    rastiDidziausia()
    
    def rastiDar():
        nonlocal reikiamasKodas
        if didziausias == 0:
            reikiamasKodas = "N/A"
        elif didziausias == parduota1:
            if didziausias == parduota2:
                pridetiKoda(kodas2)
            if didziausias == parduota3:
                pridetiKoda(kodas3) 
        elif didziausias == parduota2:
            if didziausias == parduota1:
                pridetiKoda(kodas1)
            if didziausias == parduota3:
                pridetiKoda(kodas3)
        else:
            if didziausias == parduota1:
                pridetiKoda(kodas1)
            if didziausias == parduota2:
                pridetiKoda(kodas2)
        return reikiamasKodas
         
    koduSarasas = rastiDar()
    return koduSarasas
    
ataskaita = ispausdintiAtaskaita()
print(f'Populiariausios knygos kodas(-ai): {ataskaita}')