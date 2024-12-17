print("-EVC-PLUS-")
pin = 3456
balance = 40500
check_pin = eval(input("Fadlan Geli Pin-kaaga(enter your pin) "))
if check_pin == pin:
    print("1- I tus haraaga")
    print("2- Kaarka hadalka")
    print("3- Bixi biil")
    print("4. U wareeji Evc plus")
    print('5. Warbixin Kooban')
    print('6. Salaam Bank')
    print('7. Maareynta')
    print('8. TAAJ')
    print('9. Bill Payment')
    choose = eval(input())
    if choose == 1:
        print("Haraagaagu waa ", balance)
    elif choose == 2:
        print("1- Ku shubo airtime")
        print("2- Ugu shub airtime")
        print("3- MiFi backage")
        print("4- Ku shubo internet")
        print("5- Ugu shub qof kale (MMT)")
        dooro = eval(input())
        if dooro == 1:
            print("Fadlan Geli lacagta")
            lacagta = eval(input())
            print("Ma hubtaa in aad ""$", lacagta, "ku shubatid")
            print('1. Haa')
            print('2. Maya')
            doorasho = eval(input())
            if doorasho == 1:
                print("Waxaad ku shabatey", lacagta, "waxeyna kaa dhamaan doonta 1/1/2037.")
            else:
                print('Mahadsanid!.')
        elif dooro == 2:
            print('Fadlan Geli Mobile-ka')
            mob = input()
            print('Fadlan Geli Lacagta')
            lacagta1 = eval(input())
            print('Ma hubtaa inaad' '$', lacagta1, 'ugu shubtid', mob)
            print('1. Haa')
            print('2. Maya')
            doorasho1 = eval(input())
            if doorasho1 == 1:
                print('Waxaad' '$', lacagta1, 'ugu shubtey', mob)
            else:
                print('Mahadsanid!.')
        elif dooro == 3:
            print('EVCplus')
            print('1. Ku shubo Data-da MIFI')
            dooro2 = eval(input())
            if dooro2 == 1:
                print('-- Internet Bundle Recharge--')
                print('1. Maalinle (Daily)')
                print('2. Isbuucle (Weekly)')
                print('3. Bille(Monthly)')
                dooro3 = eval(input())
                if dooro3 == 1:
                    print('Fadlan dooro bundel ka')
                    print('1. $1 = 2 GB')
                    print('2. $2 = 5 GB')
                    dooro4 = eval(input())
                    if dooro4 == 1:
                        print('Fadlan Geli MIFI user')
                        mifi = eval(input())
                        print('Ma hubtaa inaad $1 ugu shubtid', mifi)
                        print('1. Haa')
                        print('2. Maya')
                        doorasho2 = int(input())
                        if doorasho2 == 1:
                            print('Waxaad 2GB ugu shubtey', mifi)
                        else:
                            print('Mahadsanid!.')
                    elif dooro4 == 2:
                        print('Fadlan Geli MIFI user')
                        mifi2 = int(input())
                        print('Ma hubtaa inaad $2 ugu shubtid', mifi2)
                        print('1. Haa')
                        print('2. Maya')
                        doorasho3 = eval(input())
                        if doorasho3 == 1:
                            print('Waxaad 5GB ugu shubtey', mifi2)
                        else:
                            print('Mahadsanid!.')
                elif dooro3 == 2:
                    print("Fadlan dooro bundel ka")
                    print("1. 5$ = 10GB")
                    print("2. 10$ = 25GB")
                    dooro5 = eval(input())
                    if dooro5 == 1:
                        print('Fadlan Geli MIFI user')
                        mifi3 = int(input())
                        print('Ma hubtaa inaad $5 ugu shubtid', mifi3)
                        print('1. Haa')
                        print('2. Maya')
                        doorasho4 = eval(input())
                        if doorasho4 == 1:
                            print('Waxaad 10GB ugu shubtey', mifi3)
                        else:
                            print('Mahadsanid!.')
                    elif dooro5 == 2:
                        print('Fadlan Geli MIFI user')
                        mifi4 = int(input())
                        print('Ma hubtaa inaad $10 ugu shubtid', mifi4)
                        print('1. Haa')
                        print('2. Maya')
                        doorasho5 = eval(input())
                        if doorasho5 == 1:
                            print('Waxaad 25GB ugu shubtey', mifi4)
                        else:
                            print('Mahadsanid!.')
                elif dooro3 == 3:
                    print("Fadlan dooro bundel ka")
                    print("1. 20$ = 40GB")
                    print("2. 40$ = 85GB")
                    print("3. 60$ = 150GB")
                    print("4. 30$ = Monthly Unlimit")
                    dooro6 = eval(input())
                    if dooro6 == 1:
                        print('Fadlan Geli MIFI user')
                        mifi5 = int(input())
                        print('Ma hubtaa inaad $20 ugu shubtid', mifi5)
                        print('1. Haa')
                        print('2. Maya')
                        doorasho6 = eval(input())
                        if doorasho6 == 1:
                            print('Waxaad 40GB ugu shubtey', mifi5)
                        else:
                            print('Mahadsanid!.')
                    elif dooro6 ==2:
                        print('Fadlan Geli MIFI user')
                        mifi6 = int(input())
                        print('Ma hubtaa inaad $40 ugu shubtid', mifi6)
                        print('1. Haa')
                        print('2. Maya')
                        doorasho7 = eval(input())
                        if doorasho7 == 1:
                            print('Waxaad 85GB ugu shubtey', mifi6)
                        else:
                            print('Mahadsanid!.')
                    elif dooro6 == 3:
                        print('Fadlan Geli MIFI user')
                        mifi7 = int(input())
                        print('Ma hubtaa inaad $60 ugu shubtid', mifi7)
                        print('1. Haa')
                        print('2. Maya')
                        doorasho8 = eval(input())
                        if doorasho8 == 1:
                            print('Waxaad 150GB ugu shubtey', mifi7)
                    elif dooro6 == 4:
                        print('Fadlan Geli MIFI user')
                        mifi8 = int(input())
                        print('Ma hubtaa inaad $30 ugu shubtid', mifi8)
                        print('1. Haa')
                        print('2. Maya')
                        doorasho9 = eval(input())
                        if doorasho9 == 1:
                            print('Waxaad Monthly Unlimit ugu shubtey', mifi8)
                        else:
                            print('Mahadsanid!.')
                    else:
                        print('Fadlan dooro number sax ah!.')
            else:
                print('Fadlan dooro number sax ah!.')
        elif dooro == 4:
            print("Fadlan dooro numberka aad ku shubeyso")
            print("1. Maalinle (Daily)")
            print("2. Isbuucle (Weakly)")
            print("3. Bille (Monthly)")
            print("4. TIME BASSED PACKAGE")
            print("5. DATA")
            dooro7 = eval(input())
            if dooro7 == 1:
                print("Fadlan Geli lacagta")
                lacagta2 = eval(input())
                print("Mahubtaa in aad", lacagta2,"$" " ku shubatid?")
                print('1. Haa')
                print('2. Maya')
                doorasho10 = eval(input())
                if doorasho10 == 1:
                    print('Waad ku guuleysatey inaa ku shubatid', lacagta2,"$" )
                else:
                    print('Mahadsanid!.')
            elif dooro7 == 2:
                print("Fadlan Geli lacagta")
                lacagta3 = eval(input())
                print("Mahubtaa in aad", lacagta3,"$" " ku shubatid?")
                print('1. Haa')
                print('2. Maya')
                doorasho11 = eval(input())
                if doorasho11 == 1:
                    print('Waad ku guuleysatey inaa ku shubatid', lacagta3, "$")
                else:
                    print('Mahadsanid!.')
            elif dooro7 == 3:
                print("Fadlan Geli lacagta")
                lacagta4 = eval(input())
                print("Mahubtaa in aad", lacagta4,"$" " ku shubatid?")
                print('1. Haa')
                print('2. Maya')
                doorasho12 = eval(input())
                if doorasho12 == 1:
                    print('Waad ku guuleysatey inaa ku shubatid', lacagta4, "$")
                else:
                    print('Mahadsanid!.')
            elif dooro7 == 4:
                print("Fadlan Geli lacagta")
                lacagta5 = eval(input())
                print("Mahubtaa in aad", lacagta5, "$" " ku shubatid?")
                print('1. Haa')
                print('2. Maya')
                doorasho13 = eval(input())
                if doorasho13 == 1:
                    print('Waad ku guuleysatey inaa ku shubatid', lacagta5, "$")
                else:
                    print('Mahadsanid!.')
            elif dooro7 == 5:
                print("Fadlan Geli lacagta")
                lacagta6 = eval(input())
                print("Mahubtaa in aad", lacagta6, "$" " ku shubatid?")
                print('1. Haa')
                print('2. Maya')
                doorasho14 = eval(input())
                if doorasho14 == 1:
                    print('Waad ku guuleysatey inaa ku shubatid', lacagta6, "$")
                else:
                    print('Mahadsanid!.')
            else:
                print('Fadlan dooro number sax ah!.')
        elif dooro == 5:
            print('Fadlan Geli Mobile-ka')
            mob1 = int(input())
            print('Fadlan Geli Lacagta')
            lacagta7 = eval(input())
            print('Ma hubtaa inaad' '$', lacagta7, 'ugu shubtid', mob1)
            print('1. Haa')
            print('2. Maya')
            doorasho15 = eval(input())
            if doorasho15 == 1:
                print('Waxaad' '$', lacagta7, 'ugu shubtey', mob1)
            else:
                print('Mahadsanid!.')
        else:
            print('Fadlan dooro number sax ah!.')
    elif choose == 3:
        print("Bixi Biil")
        print("1. Post paid")
        print("2. Ku iibso")
        dooro8 = eval(input())
        if dooro8 ==1:
            print("Post Paid")
            print("1. Ogow Biilka")
            print("2.Bixi Biil")
            print("3. Ka Bixi Biil")
            dooro9 = eval(input())
            if dooro9 == 1:
                print("error occured please try again later")
            elif dooro9 == 2:
                print("Fadlan Geli Lacagta")
                lacagta8 = eval(input())
                print("Ma hubtaa inaad bixisid bill lacagtiisa tahey:", lacagta8,'$')
                print('1. Haa')
                print('2. Maya')
                doorasho16 = eval(input())
                if doorasho16 == 1:
                    print('Waad ku guuleysatey inaa bixiso Bill dhan', lacagta8,'$' )
                else:
                    print('Mahadsanid!.')
            elif dooro9 == 3:
                print("error occured please try again later")
            else:
                print('Fadlan dooro number sax ah!.')
    elif choose == 4:
        print('Fadlan Geli Mobile-ka')
        mob2 = int(input())
        print('Fadlan Geli Lacagta')
        lacagta9 = eval(input())
        print('Ma hubtaa inaad', lacagta9, '$' 'ugu wareejisid', mob2)
        print('1. Haa')
        print('2. Maya')
        doorasho17 = eval(input())
        if doorasho17 == 1:
            total= balance - lacagta9
            print('Waxaad', lacagta9,'$' 'ugu wareejisid', mob2,'haraagaaga waa', total)
        else:
            print('Mahadsanid!.')
    elif choose == 5:
        print("Warbixin Kooban")
        print("1. Last Action")
        print("2. Wareejintii u danabeysay")
        print("3. iibsashadii u danbaysay")
        print("4. Last  3 Actions")
        print("5. Email Me My Actvity")
        dooro10 = eval(input())
        if dooro10 == 1:
            print(" 10,000$ ayaad u wareejisay 252615445363, Taariikh: 21-12-2024 8:30:25")
        elif dooro10 == 2:
            print("Statemntiga :")
            print("1. Udirtey")
            print("2. Ka Heshay")
            dooro11 = eval(input())
            if dooro11 == 1:
                print('Fadlan Geli Mobile-ka')
                mob3 = eval(input())
                print("operation succeeded No Transaction to display")
            elif dooro11 == 2:
                print('Fadlan Geli Mobile-ka')
                mob4 = eval(input())
                print("operation succeeded No Transaction to display")
            else:
                print('Fadlan dooro number sax ah!.')
        elif dooro10 == 3:
            print("Fadlan Geli Aqoonsiga ganacsadaha")
            aqoonsi = eval(input())
            print("operation succeeded No Transaction to display")
        elif dooro10 == 4:
            print("Your mini statement has been sent as SMS to your registered mobile no")
        elif dooro10 == 5:
            print("Fadlan Geli Email kaaga ")
            email = eval(input())
            print("operation succeeded No Transaction to display")
    elif choose == 6:
        print("Salaam Bank")
        print("1. Ka wareeji EVCPlus")
        bank = eval(input())
        if bank == 1:
            print("Fadlan dooro xisaabta Bankiga")
            print("1. Bank beeraha")
            print("2. SALAAM SOMALI BANK")
            print("3. Salaam sch")
            print("4. darasalaam Bank")
            bank1 = eval(input())
            if bank1 == 1:
                print("Fadlan Geli Account-ga")
                account = eval(input())
                print("Fadlan Geli Macluumaad")
                macluumaad = eval(input())
                print("Invalid input format(length)")
            elif bank1 == 2:
                print("Fadlan Geli Account-ga")
                account1 = eval(input())
                print("Fadlan Geli Macluumaad")
                macluumaad1 = eval(input())
                print("Invalid input format(length)")
            elif bank1 == 3:
                print("Fadlan Geli Account-ga")
                account2 = eval(input())
                print("Fadlan Geli Macluumaad")
                macluumaad2 = eval(input())
                print("Invalid input format(length)")
            elif bank1 == 4:
                print("Fadlan Geli Account-ga")
                account3 = eval(input())
                print("Fadlan Geli Macluumaad")
                macluumaad3 = eval(input())
                print("Invalid input format(length)")
            else:
                print('Fadlan dooro number sax ah!.')
        else:
            print('Fadlan dooro number sax ah!.')
    elif choose == 7:
        print("Maareynta")
        print("1. Bedelka lambarka sirta ah")
        print("2. Bedel Luqadda")
        print("3. Wargalin Mobile Lumay")
        print("4. Lacag Xirasho")
        print("5. U celi lacag qaldantay")
        maareyn = eval(input())
        if maareyn == 1:
            print("Fadlan Geli Pin-kaaga cusub")
            pin_change = eval(input())
            print("Hubi Pin-kaaga cusub")
            pin_change1 = eval(input())
            if pin_change == pin_change1:
                print("[-EVCPlus-]")
                print("Waad ku guuleysatey in aad badasho PIN-kaaga.")
            else:
                print("INPUT MISMATCH")
        elif maareyn == 2:
            print("Fadlan Dooro Luqadda")
            print("1. English")
            print("2. Somali")
            luqad = eval(input())
            if luqad == 1:
                print("[-EVCPlus-]")
                print("You have succesfully changed your language")
            elif luqad == 2:
                print("[-EVCPlus-]")
                print("Waad ku guuleysatey in aad badasho luqadda")
        elif maareyn == 3:
            print("Fadlan Geli Mobile Lumay")
            print("Fadlan Geli macluumaad")
            maclumad = eval(input())
            print("Wadd ku guuleysatey")
            lumay = eval(input())
            print("Waad ku mahadsantahay wargalinta")
        elif maareyn == 4:
            print("Fadlan Geli Numberka Khaladka ah")
            khalad = eval(input())
            print("Macmiil sida ugu dhaqsiha badan ayaa kuugu xeri doona lacagtaada")
        elif maareyn == 5:
            print("Fadlan Geli Aqoonsiga Lacaga dirida")
            aqoonsi = eval(input())
    elif choose == 8:
        print("TAAJ")
        print("1. Dibadda")
        print("2. Ogow khidmada")
        print("3. Macluumaadka xawaalada")
        taaj = eval(input())
        if taaj == 1:
            print("Fadlan Geli talefanka qaataha")
            tell5 = eval(input())
            print("Fadlan geli magaca qaataha oo sedexan")
            magac = str(input())
            print("Fadlan Geli magaalada qaataha uu joogo")
            magaalo = str(input())
            print("Fadlan geli Lacagta")
            lacagta15 = eval(input())
            print("Fadlan Geli Macluumaad")
            macluumaad = eval(input())
            print("Invalid input format(length)")
        elif taaj == 2:
            print("Fadlan Dooro shirkada")
            print("1. PAY TO EVCPLUS TMT")
            print("2. TAAJ")
            print("3. TAAJ PAY")
            print("4. NEW ETAAJ")
            print("5. TAAJ IPS")
            khidmad = eval(input())
            if khidmad == 1:
                print("Fadlan Geli talefanka qaataha")
                tell = eval(input())
                print("Fadlan geli lacagta")
                lacagta10 = eval(input())
                print("error occured please try again")
            elif khidmad == 2:
                print("Fadlan Geli talefanka qaataha")
                tell1 = eval(input())
                print("Fadlan geli lacagta")
                lacagta11 = eval(input())
                print("error occured please try again")
            elif khidmad == 3:
                print("Fadlan Geli talefanka qaataha")
                tell2 = eval(input())
                print("Fadlan geli lacagta")
                lacagta12 = eval(input())
                print("error occured please try again")
            elif khidmad == 4:
                print("Fadlan Geli talefanka qaataha")
                tell3 = eval(input())
                print("Fadlan geli lacagta")
                lacagta13 = eval(input())
                print("error occured please try again")
            elif khidmad ==5:
                print("Fadlan Geli talefanka qaataha")
                tell4 = eval(input())
                print("Fadlan geli lacagta")
                lacagta14 = eval(input())
                print("error occured please try again")
        elif taaj ==3:
            print("Fadlan Geli aqoonsiga lacag dirida")
            aqoonsi = eval(input())
            print("some parameters are missing, please check your request")
        else:
            print('Fadlan dooro number sax ah!.')
    elif choose ==9:
        print("EVCPLUS")
        print("1. Itus Haraaga Bill-ka")
        print("2. Wada Bixi Bill-ka")
        print("3. Qayb ka bixi BIll")
        bill = eval(input())
        if bill == 1:
            print("Fadlan Geli Bill refference number")
            bill_ref = eval(input())
            print("some parameters are missing, please check your request")
        elif bill == 2:
            print("Fadlan Geli Bill refference number")
            bill_ref1 = eval(input())
            print("Invalid input parameter")
        elif bill == 3:
            print("Fadlan Geli Bill refference number")
            bill_ref2 = eval(input())
            print("some parameters are missing, please check your request")
        else:
            print('Fadlan dooro number sax ah!.')


else:
    print("Numberka sirta waa qalad")