# Program rieši všetky 3 časti projektu. Hráči hrajú naraz proti sebe, vždy sa pohybuje len jedna figurka hráča A alebo B, a keď príde do domčeka, na počiatočnú
# pozíciu sa dá nová figurka. Hra sa vždy začína hráčom A. Pred domčekom figurka môže ísť na konkrétne miesto "D", ak padne na kocke potrebné číslo. Ak sa tak nestane hráč hádže,
# kým mu také číslo nepadne. Pokiaľ je domčekov viac ako 6 a všetky domčeky, na ktoré sa dá dostať pohybom, sú zaplnené figurkami, figurka sa dostane do domčeka pri akomkoľvek
# hode. Figurky sa môžu navzájom vyhadzovať a vyhodená figurka začína svoj pohyb v ďalšom kole zo štartovnej pozície príslušného hráča. Celá hra je simulácia, kde hráč len zadá veľkosť a celý priebeh hry mu vypíše.
from random import *            #Naimportujeme knižnicu random aby sme mohli hádzať náhodne číslo od 1 do 6 vo funkcii pohyb_hraca

def gensachovnicu(n):
    # Funkcia zabezpečuje genenrovanie šachovnice pomocou paramera n (veľkosť). Funkcia vráti zoznam zložený z 9 zoznamov. 
    # Každý zoznam predstavuje jeden riadok šachovnice.
    global stred, domcek_A, domcek_B, pocet_A_cok, pocet_B_cok      # Globalne premenné, ktoré sa využívajú vo funckii pohyb_hraca a v priebeh_hry.
    stred = n//2                                  # Pomocné premenné, ktoré určujú, kde je stred, aký je znak, kde sú prázdne miesta atď. 
    lave_prazdne_miesta = n//2 - 2 
    prave_prazdne_miesta = n - n//2 + 1 
    znak = ""  
    pocet_domcekov = 0                  # Premenné určújúce počet domčekov a počet figuriek v domčeku (potrebné hlavne pri pohybe).
    pocet_A_cok = 0                     
    pocet_B_cok = 0              
    sachovnica = []                     # Pomocné zoznamy, a zoznam šachovnice ako takej.
    riadok_sachovnice = []
    domcek_A = []   
    domcek_B = []
    for i in range(n):              # For cyklus na tvorenie každého riadku.
        for k in range(n):              # For cyklus na tvorenie každého znaku.
            if i == stred and k == stred:           # Pomocou predtým stanovených premenných následne vypíšeme pomocou i a k aké znaky budú v riadku.
                znak = "X"
                pocet_domcekov = 0                  # Vynulujeme počet domčekov, pretože ak sa nachádzame v strede, domčeky pre hráča A už ďalšie netreba.
            elif i == 0 and k == prave_prazdne_miesta - 1:
                znak = "A"
            elif i == n - 1 and k == lave_prazdne_miesta + 1:
                znak = "B"
            elif (i != 0 and i != n - 1) and k == stred:
                znak = "D"
                pocet_domcekov += 1
            elif (k != 0 and k != n - 1) and i == stred:
                znak = "D"
            elif i >=  (stred - 1) and i <= (stred + 1):
                znak = "*"
            elif k <= lave_prazdne_miesta or k >= prave_prazdne_miesta:
                znak = " "
            else:
                znak = "*"

            if znak == "D" and len(domcek_A) < pocet_domcekov:      # Najskôr priraďujeme domčeky hráčovi A do pomocného zoznamu.
                domcek_A.append(znak)
            elif znak == "D" and len(domcek_B) < pocet_domcekov:    # Keď prejdeme za stred, počet sa vynuluje a nasledujúce "D" priraďujeme do domčeka pre hráča B.
                domcek_B.append(znak)

            riadok_sachovnice.append(znak)          # Každý znak následne pridáme do pomocnej premmenej pre riadok šachovnice. 
   
        sachovnica.append(riadok_sachovnice)        # Každý riadok následne pridáme do celého zoznamu šachovnice a následne pomocnú premennú pre riadok nastavíme na prázdny zoznam.
        riadok_sachovnice = [] 

    return sachovnica


def pohyb_hraca(n, sachovnica, hrac, opacny_hrac):
    # Pohyb je založený najpr na najdenie indexu figurky, ktorá nie je v domčeku. Následne je urobený pohyb samostatne buď pre figurku A alebo figurku B. 
    # Celý pohyb je rozdelený podľa toho, kde sa nachádza figurka. Rozdelenie je do dvoch podmienok, či je index stĺpca figurky za polkou alebo pred polkou. (Ak sa rovná polke zaléží od figurky). 
    global pocet_A_cok, pocet_B_cok, pohyb         # Aktuálne hodnoty týchto premenných su potrebné pre funkciu priebeh_hry a samotnú funkciu ako takú.   
    pohyb = randint(1,6)      # Náhodný hod kockou od 1 do 6.
    hladanie_indexu = True
    print("Hráč", hrac, "hodil na kocke číslo:", pohyb)

    for r_i in range(len(sachovnica)):              # Hľadanie indexov pre figurku. 
        if hladanie_indexu == True:
            for s_i in range(len(sachovnica[0])):
                if sachovnica[r_i][s_i] == hrac:
                    riadok_index = r_i
                    stlpec_index = s_i
                    if stlpec_index == stred and (riadok_index > 0 and riadok_index < n - 1):       # Pokiaľ cyklus zaznamená figurku, ktorá je v domčeku, vynechá ju a hľadá inú. 
                        pass
                    else:
                        hladanie_indexu = False
                        sachovnica[riadok_index][stlpec_index] = "*"        # Miesto, na ktorom sa nachádza figurka sa prepíše na *.
                        break

    if hladanie_indexu == True:             # Pokiaľ nenašlo figurku, ktorá by bola mimo domček (Bola vyhodená druhým hráčom), index riadka a stĺpca je na počiatočnej pozícii.
        if hrac == "A":
            riadok_index = 0
            stlpec_index = stred + 1
        elif hrac == "B":
            riadok_index = n - 1
            stlpec_index = stred - 1

    povodny_riadok_index = riadok_index         # Pomocné premenné, potrebné pre prípad, kedy figurka nevie vstúpiť do domčeku, lebo na príslušnej pozícii je už iná figurka hráča.
    povodny_stlpec_index = stlpec_index

    pocet_krokov = 0        # Premenná, ktorá ráta koľko krokov už figurka vykonala, ak sa číslo na kocke rovná počtu krokov, žiadny ďalší pohyb sa už nevykonná.
    if hrac == "A":                 # Pohyb pre hráča A.
        if stlpec_index > stred:        # Najskôr sa zisťuje, či je index stĺpca figurky väčší ako stred.
            for r in range(riadok_index, len(sachovnica)):      # Prechádzanie od riadku v ktorom je figurka až po koniec šachovnice. 
                if pocet_krokov != pohyb:
                    if r < stred + 1:                   # Zisťujeme aký je index riadka figurky.
                        for s in range(stlpec_index, len(sachovnica[0])):       # Keď je riadok menší ako stred + 1, figurka sa pohybuje smerom do konca riadka.
                            if sachovnica[r][s] == "*" or sachovnica[r][s] == opacny_hrac:  # Figurka rieší pohyb len pokiaľ je na danom mieste "*" alebo opačný hráč.
                                pocet_krokov += 1
                                if stlpec_index == stred + 1 and riadok_index != stred - 1:     # Niekoľko podmienok, podľa toho, či sa mení index riadka alebo index stĺpca.
                                    riadok_index += 1
                                elif riadok_index == stred - 1 and stlpec_index != n - 1:
                                    stlpec_index += 1
                                else:
                                    riadok_index += 1
                            
                            if pocet_krokov == pohyb:           # Ak počet krokov figurky je toľko, koľko je hod kockou, figurka sa na dané indexy prepíše v zozname.
                                sachovnica[riadok_index][stlpec_index] = hrac
                                break               # Po splnení podmineky sa cyklus ukončí a ďalej sa už pohybovať nebude, vďaka podmienke ktorá je na riadku napr. 92.

                    elif r >= stred + 1:                
                        for s in range(stlpec_index, stred - 1, - 1):    # Prechádzanie od stĺpca, v ktorom je smerom k stredu (spiatočný pohyb v zozname).
                            if sachovnica[r][s] == "*" or sachovnica[r][s] == opacny_hrac:          # Opäť sa rieši na akom mieste je figurka. Podľa toho sa menia jej indexy a následne jej prepis.
                                pocet_krokov += 1
                                if riadok_index == stred + 1 and stlpec_index == stred + 1:
                                    riadok_index += 1
                                elif riadok_index == n - 1 or riadok_index == stred + 1:
                                    stlpec_index -= 1
                                else:
                                    riadok_index += 1

                            if pocet_krokov == pohyb:
                                sachovnica[riadok_index][stlpec_index] = hrac
                                break

        if stlpec_index <= stred:                   # Pokiaľ je index stĺpca figurky menší alebo rovný ako stred, pohyb sa rieší nasledujúcimi podmienkami.
            for r in range(riadok_index, - 1, - 1):
                if pocet_krokov != pohyb:
                    if r > stred - 1:       # Opäť zisťujeme aký je index riadka figurky a poďla nej sa robí pohyb. 
                        for s in range(stlpec_index, - 1, - 1):         # Ak je v riadku väčšom ako stred - 1, cyklus prechádza každý riadok spätne a vykoná pohyb pri každej "*" alebo opačnej figurke.
                            if sachovnica[r][s] == "*" or sachovnica[r][s] == opacny_hrac:
                                pocet_krokov += 1
                                if (stlpec_index == stred - 1 and riadok_index != stred + 1) or stlpec_index == 0:
                                    riadok_index -= 1
                                else:
                                    stlpec_index -= 1

                            if pocet_krokov == pohyb:
                                sachovnica[riadok_index][stlpec_index] = hrac
                                break

                    elif r <= stred - 1:            # Podmienky pre pohyb ak je index riadku figurky menší alebo rovný ako stred - 1.
                        for s in range(stlpec_index, stred):
                            if sachovnica[r][s] == "*" or sachovnica[r][s] == opacny_hrac:
                                pocet_krokov += 1
                                if (riadok_index == stred - 1 and stlpec_index != stred - 1) or riadok_index == 0:
                                    stlpec_index += 1
                                else:
                                    riadok_index -= 1

                            if pocet_krokov == pohyb:
                                sachovnica[riadok_index][stlpec_index] = hrac
                                break

        if stlpec_index == stred and riadok_index == 0:             # Špeciálna podmienka ak je figurka pred domčekom. 
            for r in range(riadok_index, stred):                    # Cyklus, ktorý vedie figurku smerom k stredu šachovnice (k "X").
                if pocet_krokov != pohyb:
                    for s in range(stlpec_index, stlpec_index + 1):
                        if sachovnica[r][s] == "D" or sachovnica[r][s] == hrac:     # Cyklus hľadá stĺpce v ktorom je D (voľné miesto), alebo už tam je figurka hráča.
                            pocet_krokov += 1
                            riadok_index += 1
                        if pocet_krokov == pohyb:
                            if sachovnica[r][s] == hrac and pocet_A_cok < 6:    # Špeciálna podmienka, ak je počet domčekov menší ako 6 (najväčší možný hod kockou), figurka nám pôjde na domčeky podľa kocky, prípadne podľa počtu krokov.
                                sachovnica[povodny_riadok_index][povodny_stlpec_index] = hrac       # Ak na danej pozícii už je figurka, pohyb sa "akokeby" nevykoná a pozícia figurky bude tam, odkiaľ sa hádzalo kockou.
                                break
                            elif pocet_A_cok >= 6:      # Ak je domčekov viac ako 6 a figurka je na políčku pred domčekami, nezáleží, koľko padne na kocke, figurka sa premiestni automaticky na najbližší voľný domček.
                                pocet_A_cok += 1
                                sachovnica[pocet_A_cok][s] = hrac
                            else:                       # Ak je presun možný a domčekov je menej ako 6, vykoná sa pohyb
                                sachovnica[r][s] = hrac
                                pocet_A_cok += 1

                            domcek_A.pop(0)             # Do pomocného zoznamu sa nám len vylúči jedno "D" a pridá "A". Pozícia v tomto zozname nie je v súlade s tým, na akom mieste figurka reálne je, pre nás je dôležítý len počet.
                            domcek_A.append(hrac)
                            print("Hráč A priviedol figurku do domčeka")
                            if "D" in domcek_A:         # Pokiaľ sa v pomocnou zozname stále nachádza "D", nová figurka sa automaticky dá na štartovnú pozíciu. Netreba hodiť 6 na kocke.
                                sachovnica[0][stred + 1] = hrac
                            break
                            
            if pocet_krokov != pohyb:           # Pokiaľ na kocke padne väčšie číslo ako je dostupných možností (prípad keď je pred domčekom a hráč hodí väčšie číslo ako je počet domčekov). Figurka bude mať pôvodnú pozíciu odkiaľ sa hádzalo.
                sachovnica[povodny_riadok_index][povodny_stlpec_index] = hrac
                riadok_index = povodny_riadok_index
                stlpec_index = povodny_stlpec_index

    elif hrac == "B":
        # Nasledujúci pohyb pre hráča B je takmer identický ako pre hráča A. Rozdiel je len v niektorých podmienkach, miesto odkiaľ ide figurka do domčeku, štartovná pozícia a sú vymenné podmienky pri hľadaní indexu stĺpca figurky. 
        # Snažil som sa spojiť tieto pohyby, tým pádom by som mal menej riadkov a kód efektívnejší, avšak, vždy sa mi stala situácia, kedy sa pohyb vykonal nesprávne. Preto je to takto rozdelené.
        if stlpec_index < stred:            # Štartovná pozícia figurky (jej index stĺpca) je menšia ako index stredu. Preto začíname pohyb odtiaľ.
            for r in range(riadok_index, - 1, - 1):
                if pocet_krokov != pohyb:
                    if r > stred - 1: 
                        for s in range(stlpec_index, - 1, - 1):
                            if sachovnica[r][s] == "*" or sachovnica[r][s] == opacny_hrac:
                                pocet_krokov += 1
                                if (stlpec_index == stred - 1 and riadok_index != stred + 1) or stlpec_index == 0:
                                    riadok_index -= 1
                                else:
                                    stlpec_index -= 1

                            if pocet_krokov == pohyb:
                                sachovnica[riadok_index][stlpec_index] = hrac
                                break

                    elif r <= stred - 1:
                        for s in range(stlpec_index, stred):
                            if sachovnica[r][s] == "*" or sachovnica[r][s] == opacny_hrac:
                                pocet_krokov += 1
                                if (riadok_index == stred - 1 and stlpec_index != stred - 1) or riadok_index == 0:
                                    stlpec_index += 1
                                else:
                                    riadok_index -= 1

                            if pocet_krokov == pohyb:
                                sachovnica[riadok_index][stlpec_index] = hrac
                                break

        if stlpec_index >= stred:           # Zmena oproti pohybu hráča A, v podmienke musí byť aj "rovná sa stredu", inak by figurka neprešla cez štartovnú pozíciu hráča A.
            for r in range(riadok_index, len(sachovnica)):
                if pocet_krokov != pohyb:
                    if r < stred + 1:
                        for s in range(stlpec_index, len(sachovnica[0])):
                            if sachovnica[r][s] == "*" or sachovnica[r][s] == opacny_hrac:
                                pocet_krokov += 1
                                if stlpec_index == stred + 1 and riadok_index != stred - 1:
                                    riadok_index += 1
                                elif riadok_index == stred - 1 and stlpec_index != n - 1:
                                    stlpec_index += 1
                                elif stlpec_index == stred:
                                    stlpec_index += 1
                                else:
                                    riadok_index += 1
                            
                            if pocet_krokov == pohyb:
                                sachovnica[riadok_index][stlpec_index] = hrac
                                break

                    elif r >= stred + 1:
                        for s in range(stlpec_index, stred, - 1):
                            if sachovnica[r][s] == "*" or sachovnica[r][s] == opacny_hrac:
                                pocet_krokov += 1
                                if riadok_index == stred + 1 and stlpec_index == stred + 1:
                                    riadok_index += 1
                                elif riadok_index == n - 1 or riadok_index == stred + 1:
                                    stlpec_index -= 1
                                else:
                                    riadok_index += 1

                            if pocet_krokov == pohyb:
                                sachovnica[riadok_index][stlpec_index] = hrac
                                break

        if stlpec_index == stred and riadok_index == n - 1:     # Zmenené len indexy, kde je miesto pred domčekom. Vstup do domčeka je rovnako vyriešený ako pri hráčovi A.
            for r in range(riadok_index, stred, - 1):
                if pocet_krokov != pohyb:
                    for s in range(stlpec_index, stlpec_index - 1, - 1):
                        if sachovnica[r][s] == "D" or sachovnica[r][s] == hrac:
                            pocet_krokov += 1
                            riadok_index -= 1
                        if pocet_krokov == pohyb:
                            if sachovnica[r][s] == hrac and pocet_B_cok < 6:
                                sachovnica[povodny_riadok_index][povodny_stlpec_index] = hrac
                                break
                            elif pocet_B_cok >= 6:
                                pocet_B_cok += 1
                                sachovnica[n - pocet_B_cok - 1][s] = hrac           # Opäť, ak je viac domčekov ako 6, priradí sa figurka B na najbližši voľný domček.
                            else:
                                sachovnica[r][s] = hrac
                                pocet_B_cok += 1
                            
                            domcek_B.pop(0)
                            domcek_B.append(hrac)
                            print("Hráč B priviedol figurku do domčeka")
                            if "D" in domcek_B:         # Ak je voľný domček, na štartovnú pozíciu sa dá ďalšia figurka hráča B.
                                sachovnica[n - 1][stred - 1] = hrac
                            break
                            
            if pocet_krokov != pohyb:
                sachovnica[povodny_riadok_index][povodny_stlpec_index] = hrac
                riadok_index = povodny_riadok_index
                stlpec_index = povodny_stlpec_index
    
    return sachovnica               

def tlacsachovnicu(sachovnica_s_pohybom, n):
    # Celý predchádzajúci zoznam s pohybom táto funkcia zoberie a znak po znaku ho vypíše. Navyše sú tam pomocou cyklu a pár podmienok pripísané čísla, určujúce stĺpec a riadok šachovnice.
    # Ešte predtým je vo funckii priebeh_hry vrátený zoznam s pohybom priradený do premennej sachovnica_s_pohybom. 
    print(end = "  ")
    for r in range(n):                  # Cyklus pre prvý riadok len s číslami.
        if r >= 10:
            print("", r%10, end = " ")
        else:
            print("", r, end = " ")
    print()
    for s in range(len(sachovnica_s_pohybom)):      # Následne cyklus, ktorý vypisuje číslo riadka a každý riadok zoznamu.
        if s >= 10:
            print(s%10, end = " ")
        else:
            print(s, end = " ")
        for miesto in sachovnica_s_pohybom[s]:      # Cyklus, ktorý vypisuje každý znak riadka. 
            print("", miesto, end = " ")
        print()
    print()


def velkost():
    # Funkcia, ktorá zisťuje, aká má byť veľkosť šachovnice. Veľkosť musí byť nepárne číšlo a väčšie ako 3, pretože pre 3 nemá šachovnica domčeky.
    # Ak uživateľ zadal nesprávnu veľkosť, bude sa požadovať aby ju zadal znova.  
    v = int(input("Zadaj veľkosť šachovnice (musí byť nepárne číslo väčšie ako 3): "))
    while v%2 == 0 or v < 5:
        v = int(input("Zadaj znova veľkosť šachovnice (musí byť nepárne číslo väčšie ako 3): "))

    return v


def priebeh_hry(n):
    # Fukncia, ktorá zabezpečuje celý výpis šachovnice. Jej paramater je veľkosť šachovnice. 
    kolo = 0                # Premenná, ku ktorej budeme prirátavať počet kôl.

    print()
    sachovnica = gensachovnicu(n)
    tlacsachovnicu(sachovnica, n)       # Pred celým pohybom sa nám ešte vypíše šachovnica s figurkami na štartovných pozíciach.

    while "D" in domcek_A and "D" in domcek_B:          # Celý pohyb sa vykonáva, kým je v pomocnom zozname pre domček A alebo domček B stále voľné miesto pre figurku.
        kolo += 1           # Počítadlo kôl. 

        print("Kolo číslo:", kolo)      # Pred prvým pohybom hráča A nám vypíše nasledujúce kolo.
        sachovnica_s_pohybom = pohyb_hraca(n, sachovnica, "A", "B")
        tlacsachovnicu(sachovnica_s_pohybom, n)

        while pohyb == 6:      # Ak bola hodená šestka, hráč hádže znovu dokiaľ nepadne iné číslo než 6.
            if "D" not in domcek_A:        # Ak hráč A dostal figurku do domčeka šestkou, tak nechceme, aby sa hod hráča A vykonal znova.
                break
            sachovnica_s_pohybom = pohyb_hraca(n, sachovnica, "A", "B")
            tlacsachovnicu(sachovnica_s_pohybom, n)

        if "D" not in domcek_A:    # Špeciálna podmienka, ak hráč A už dostal poslednú figurku do domčeka, pohyb hráča B už nie je podstatný.
            break

        # Podobný princíp opakovania pohybu pre hráča B.
        sachovnica_s_pohybom = pohyb_hraca(n, sachovnica, "B", "A")
        tlacsachovnicu(sachovnica_s_pohybom, n)

        while pohyb == 6:
            if "D" not in domcek_B:             # Opäť nechceme, ak hráč B dostal poslednú figurku šestkou do domčeka, aby hádzal znova.
                break
            sachovnica_s_pohybom = pohyb_hraca(n, sachovnica, "B", "A")
            tlacsachovnicu(sachovnica_s_pohybom, n)

    if pocet_A_cok == len(domcek_A):        # Zistíme, ktorý hráč ma vo svojom pomocnom zozname pre domček "D", ten ktorý nemá, vyhral.
        print("HRÁČ A VYHRAL !!!")
    else:
        print("HRÁČ B VYHRAL !!!")
    print("HRA SKONČILA V KOLE ČÍSLO:", kolo)


n = velkost()       # Zavolanie funkcie na veľkosť šachovnice a priradenie jej výsledku do premennej n.
priebeh_hry(n)      # Zavolanie funkcie, ktorá vykonáva celý výpis od začiatku po koniec.