
#funkce pro vypocet anuitní splatky uveru
def vyse_splatky(uver, urokova_sazba, pocet_obdobi):
    U = uver
    p = urokova_sazba
    n = pocet_obdobi

    a = U * p * (1 + (1 / (pow((p + 1),n)-1)))
    return a

def jednodenni_urok(jistina, urokova_sazba, pocet_obdobi):
    urok = urokova_sazba / pocet_obdobi * jistina
    return urok

def splatky(splatka, uver, pocet_obdobi, urokova_sazba):
    splatky = []
    jistina = uver
    
    for cislo_obdobi in range(1, pocet_obdobi + 1):
        mesicni_urok = jednodenni_urok(jistina, urokova_sazba, pocet_obdobi) * 30
        umor = splatka - mesicni_urok
        jistina = jistina - umor

        splatky.append([int(umor), int(mesicni_urok), int(jistina)])

        print(cislo_obdobi)
        print(splatky[cislo_obdobi-1][0])
        print(splatky[cislo_obdobi-1][1])
        print(splatky[cislo_obdobi-1][2])
        #print(f"{splatka}|{int(umor)}|{int(mesicni_urok)}|{int(jistina)}")
    
    return splatky


def main():

    #LTV loan to value
    #DTI debt to income
    #DSTI debt service to income
    #https://www.hyponamiru.cz/kompletni-pruvodce-jak-se-pocita-a-splaci-hypoteka/

    #uver 'U' v Kč
    U = 3000000
    #uver U_mil v milionech Kč
    U_mil = round(U / 1000000)

    #urokova sazba 'p' např. 5,99% = 0,0599/12
    p = 0.0599/12

    #pocet obdobi 'n' měsíců
    n = 360
    
    #vyse splatky 'a'
    a = round(vyse_splatky(U, p, n))
    
    print(f'Anuitní splátka úvěru { U_mil } mil. Kč je { a } Kč měsíčně.')

    splatky(a, U, n, p*12)




if __name__ == '__main__':
    main()
