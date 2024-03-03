DictMobil = {
    "Jenis"     : ["Agya"       , "Veloz"       , "Zenix"       , "Zigra"       , "Veloz"       , "Hi-Ace"      , "L-300"       , "Veloz"       ],
    "Brand"     : ["Toyota"     , "Toyota"      , "Toyota"      , "Daihatsu"    , "Toyota"      , "Toyota"      , "Mitsubishi"  , "Toyota"      ],
    "Plat"      : ["B 1234 CTH" , "B 9876 CTH"  , "N 1234 CTH"  , "N 9876 CTH"  , "D 1234 CTH"  , "D 9876 CTH"  , "A 1234 CTH"  , "A 9876 CTH"  ],
    "Kapasitas" : [5            , 7             , 8             , 6             , 7             , 12            , 3             , 7             ],
    "Tahun"     : [2021         , 2023          , 2022          , 2020          , 2019          , 2022          , 2021          , 2022          ],
    "Biaya"     : [250_000      , 300_000       , 400_000       , 275_000       , 300_000       , 10_600_000    , 75_000        , 4_000_000     ],
    "Jaminan"   : ["-"          , "KTP"         , "CC"          , "-"           , "-"           , "KTP"         , "-"           , "-"           ],
    "Status"    : ["Tersedia"   , "Dipakai"     , "Dipakai"     , "Tersedia"    , "Tersedia"    , "Dipakai"     , "Tersedia"    , "Tersedia"    ],
    "Mulai"     : ["-"          , "24-02-2024"  , "22-02-2024"  , "-"           , "-"           , "22-02-2024"  , "-"           , "-"           ],
    "Dipakai"   : [1            , 0             , 0             , 1             , 1             , 0             , 1             , 1             ]
}

# Main Menu
def TitleMenu(TextMenu):
    print()
    print("|" + f"{f"{"---------" + len(TextMenu) * "-" + "----------"}":^120}" + "|")
    print("|" + f"{f"{"--- MENU " + TextMenu + " MOBIL ---"}":^120}" + "|")
    print("|" + f"{f"{"---------" + len(TextMenu) * "-" + "----------"}":^120}" + "|")


DictMainMenu = {
    "Menu" : [
        "Daftar Mobil",
        "Sewa Mobil",
        "Kembalikan Mobil",
        "Tambah Mobil",
        "Update Mobil",
        "Hapus Mobil",
        "Keluar"
    ]
}

def MenuUtama():
    print()
    for index, item in enumerate(DictMainMenu["Menu"]):
        print("|" + f"{f"{index + 1}. {item}":^120}" + "|")
    global DictMainMenuValLen
    DictMainMenuValLen = index
    
    
def SubMenu(DictionaryMenu):
    print()
    for item in range(len(DictionaryMenu["Header"])):
        print("|" + f"{DictionaryMenu["Header"][item]:^120}" + "|")
    print()
    for index, item in enumerate(DictionaryMenu["Menu"]):
        print("|" + f"{f"{index + 1}. {item}":^120}" + "|")
    print()
    for item in range(len(DictionaryMenu["Footer"])):
        print("|" + f"{DictionaryMenu["Footer"][item]:^120}" + "|")


# Dictionary Menu
def DictSubMenu(TextMenu, TextString= ""):
    DictMobil = {
        "Header" : [
            "PILIHAN INPUT:",
            TextString
        ],
        "Menu" : [
            
            "Tampilkan seluruh inventory mobil",
            TextMenu 
        ],   
        "Footer" : [  
            "Kembali ke MENU UTAMA: menu",
            ""
        ]
    }
    
    return DictMobil


# Print Dictionary
## Print Mobil
def PrintColomMobil():
    print("|" + f"{f"{"No.":6}|{"Plat No.":^15}|{"Brand":13}|{"Jenis":10}|{"Tahun":7}|{"Kapasitas":10}|{"Biaya":^14}|{"Jaminan":10}|{"Status":12}|{"Mulai":12}":^120}" + "|")

## Daftar, Tambah, Update, Hapus = (0,1, MENU UTAMA), Sewa = (1,1), Kembali = (0,0)
def PrintDaftarMobil(Key = 'Plat', Dipakai = 0, Tersedia = 1):
    for index, item in enumerate(DictMobil[Key]):
        if DictMobil['Dipakai'][index] == Dipakai or DictMobil['Dipakai'][index] == Tersedia:
            Biaya = f"{DictMobil['Biaya'][index]:,}"
    #        ListValueIndex = index
            print("|" + f"{f"{index:<6}|{DictMobil['Plat'][index]:^15}|{DictMobil['Brand'][index]:13}|{DictMobil['Jenis'][index]:10}|{DictMobil['Tahun'][index]:^7}|{DictMobil['Kapasitas'][index]:^10}|{Biaya:^14}|{DictMobil['Jaminan'][index]:10}|{DictMobil['Status'][index]:12}|{DictMobil['Mulai'][index]:12}":^120}" + "|")

    # return ListValueIndex

## Print Daftar Inside Loop
def PrintDaftarMobilIndex(index):
    Biaya = f"{DictMobil['Biaya'][index]:,}"
    print("|" + f"{f"{index:<6}|{DictMobil['Plat'][index]:^15}|{DictMobil['Brand'][index]:13}|{DictMobil['Jenis'][index]:10}|{DictMobil['Tahun'][index]:^7}|{DictMobil['Kapasitas'][index]:^10}|{Biaya:^14}|{DictMobil['Jaminan'][index]:10}|{DictMobil['Status'][index]:12}|{DictMobil['Mulai'][index]:12}":^120}" + "|")


# Divider
## Plain Divider
def SubMenuDivider(MenuDivider = 5):
    print()
    print("|" + f"{MenuDivider * 3 * "- - - ":^120}" + "|")

## Divider With Prompt
def DividerPrompt(TextString, TextStringMidEndWithSpace, MenuDivider = 5):
    print()
    print(TextString)
    print()
    print("|" + f"{f"{f"{MenuDivider * "- - - " + TextStringMidEndWithSpace + MenuDivider * "- - - "}"}":^120}" + "|")

## Divider No Prompt
def DividerLine(TextStringMidEndWithSpace, MenuDivider = 5):
    print()
    print("|" + f"{f"{f"{MenuDivider * "- - - " + TextStringMidEndWithSpace + MenuDivider * "- - - "}"}":^120}" + "|")


# Callback Functions
## Print Car List
def PrintCarList(Key = 'Plat', Dipakai = 0, Tersedia = 1):
    SubMenuDivider()
    print()
    PrintColomMobil()
    print()
    PrintDaftarMobil(Key, Dipakai, Tersedia)
    print()
    UserInput3 = input("+ Tekan apapun untuk kembali ke SUB-MENU: ")
    SubMenuDivider()

def PrintCarListNoMenu(Key = 'Plat', Dipakai = 0, Tersedia = 1):
    SubMenuDivider()
    print()
    PrintColomMobil()
    print()
    PrintDaftarMobil(Key, Dipakai, Tersedia)
    print()

## Check Number Plate
def CheckPlatMobil(ListUserInput3Split, UserInput3Upr):
    FoundIndex = -1
    FoundValue = 0
    if len(ListUserInput3Split[0]) > 0 and len(ListUserInput3Split[0]) < 3 and ListUserInput3Split[0].isdigit() == False and len(ListUserInput3Split[1]) > 0 and len(ListUserInput3Split[1]) < 5 and ListUserInput3Split[1].isdigit() == True and len(ListUserInput3Split[2]) > 0 and len(ListUserInput3Split[2]) < 4 and ListUserInput3Split[2].isdigit() == False:
        for index, item in enumerate(DictMobil["Plat"]):
            if UserInput3Upr == DictMobil["Plat"][index]:
                PrintColomMobil()
                print()
                PrintDaftarMobilIndex(index)
                print()
                FoundIndex = index
                FoundValue += 1
                
                return FoundIndex, FoundValue
            
            else:
                continue
            
## Change to Terpakai
def ChangeToDipakai(Index, InputTanggal, InputJaminan):
    DictMobil["Mulai"][Index] = InputTanggal
    DictMobil["Status"][Index] = 'Dipakai'
    DictMobil["Jaminan"][Index] = InputJaminan
    DictMobil["Dipakai"][Index] = 0

## Change to Tersedia
def ChangeToTersedia(Index):
    DictMobil["Mulai"][Index] = "-"
    DictMobil["Status"][Index] = 'Tersedia'
    DictMobil["Jaminan"][Index] = "-"
    DictMobil["Dipakai"][Index] = 1

def Sortir(Key):
    Val1 = DictMobil[Key].copy()
    Val2 = list(set(Val1))
    Val2.sort()
    PrintColomMobil()
    print()
    for index, item in enumerate(DictMobil[Key]):
        if Val2 == []:
            continue
        
        Val3 = max(Val2)
        for index, item in enumerate(DictMobil[Key]):
            if item == Val3:
                PrintDaftarMobilIndex(index)
        Val2.pop()
        
    print()    
    UserInput5 = input("+ Tekan apapun untuk kembali ke SUB-MENU: ")
    DividerLine("< Kembali ke SUB-MENU > ")

def Pembayaran(Day, Total, CheckPlatMobilIndex):
    print()
    print(f"Waktu sewa adalah: {Day} hari")
    print(f"Total yang harus dibayar adalah: {Total:,}")
    print()
    UserInput7 = int(input(">>>>>>> Masukkan nominal pembayaran: "))
    
    if UserInput7 > Total:
        print(f"Terima Kasih, kembalian anda adalah: {(UserInput7 - Total):,}")
        ChangeToTersedia(CheckPlatMobilIndex)
        DividerPrompt("[ Mobil sukses dikembalikan ]", "< Kembali ke SUB-MENU > ")
    
    elif UserInput7 < Total:
        print(f"Uang anda tidak mencukupi, nominal yang harus dibayar adalah: {Total:,}")
        DividerPrompt("[ Pembayaran Gagal ]", "< Kembali ke SUB-MENU > ")
        
    else:
        print("Terima Kasih")
        ChangeToTersedia(CheckPlatMobilIndex)
        DividerPrompt("[ Mobil sukses dikembalikan ]", "< Kembali ke SUB-MENU > ")
        
        
# Functions

## Daftar Mobil - DONE
def DaftarMobil():
    while True:
        TitleMenu("DAFTAR")
        SubMenu(DictSubMenu("Cari PLAT nomor mobil"))
        
        try:
            UserInput2 = input(">> Masukkan pilihan yang diinginkan: ")
            
            if UserInput2 == 'menu':
                DividerLine("> Kembali ke MENU UTAMA < ")
                break
            
            elif UserInput2 == '1':
                PrintCarListNoMenu()
                UserInput3 = input(">>> Apakah anda ingin mensortir daftar mobil? (ya/tidak): ")
                
                if UserInput3 == 'menu' or UserInput3 == 'tidak':
                    DividerLine("< Kembali ke SUB-MENU > ")
                    continue
                
                elif UserInput3 == 'ya':
                    SubMenuDivider()
                    print()
                    print("|" + f"{f"Berdasarkan:":^120}" + "|")
                    print("|" + f"{f"1. Tahun Mobil":^120}" + "|")
                    print("|" + f"{f"2. Kapasitas":^120}" + "|")
                    print("|" + f"{f"3. Biaya":^120}" + "|")
                    print()
                    UserInput4 = input(">>>> Masukkan pilihan yang diinginkan: ").lower()
                    print()
                    
                    if UserInput4 == 'menu':
                        DividerLine("< Kembali ke SUB-MENU > ")
                        continue
                    
                    elif UserInput4 == '1' or UserInput4 == 'tahun':
                        Sortir('Tahun')
                        
                    elif UserInput4 == '2' or UserInput4 == 'kapasitas':
                        Sortir('Kapasitas') 
                    
                    elif UserInput4 == '3' or UserInput4 == 'biaya':
                        Sortir('Biaya')
                            
                    else:
                        DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
                    
                else:
                    DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
            
            elif UserInput2 == '2':
                print()
                UserInput3Upr = input(">>> Masukkan PLAT nomor mobil (Cth. B 1234 CTH): ").upper()
                ListUserInput3Split = UserInput3Upr.split(" ")
                
                if len(ListUserInput3Split) == 3:
                    print()
                    CheckPlatMobilTuple = CheckPlatMobil(ListUserInput3Split, UserInput3Upr)
                    
                    if CheckPlatMobilTuple == None:
                        DividerPrompt("[ Mobil tidak ditemukan ]", "< Kembali ke SUB-MENU > ")
                        continue
                    
                    CheckPlatMobilValue = CheckPlatMobilTuple[1]
                    
                    if CheckPlatMobilValue == 1:
                        print("[ Mobil ditemukan ]")
                        print()
                        UserInput4 = input("+ Tekan apapun untuk kembali ke SUB-MENU: ")
                        DividerLine("< Kembali ke SUB-MENU > ")
                else:
                    DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
            else:
                DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")    
        except ValueError:
            DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
    

## Sewa Mobil
def SewaMobil():
    while True:
        TitleMenu("SEWA")
        SubMenu(DictSubMenu("Cari PLAT nomor mobil"))
        
        try:
            UserInput2 = input(">> Masukkan pilihan yang diinginkan: ")
            if UserInput2 == 'menu':
                DividerLine("> Kembali ke MENU UTAMA < ")
                break
            
            elif UserInput2 == '1':
                PrintCarList()

            elif UserInput2 == '2':
                print()
                PrintColomMobil()
                print()
                PrintDaftarMobil(Dipakai=1)
                
                print()
                UserInput3Upr = input(">>> Masukkan PLAT NOMOR mobil (Cth. B 1234 ABC): ").upper()
                
                ListUserInput3Split = UserInput3Upr.split(" ")
                
                if UserInput3Upr == 'MENU':
                    DividerLine("< Kembali ke SUB-MENU > ")
                    
                elif len(ListUserInput3Split) == 3:
                    print()
                    CheckPlatMobilTuple = CheckPlatMobil(ListUserInput3Split, UserInput3Upr)
                    
                    if CheckPlatMobilTuple == None:
                        DividerPrompt("[ Mobil tidak ditemukan ]", "< Kembali ke SUB-MENU > ")
                        continue
                    
                    CheckPlatMobilIndex = CheckPlatMobilTuple[0]
                    CheckPlatMobilValue = CheckPlatMobilTuple[1]
                                    
                    if CheckPlatMobilValue == 1 and DictMobil["Status"][CheckPlatMobilIndex] == 'Tersedia':
                        print("[ Mobil ditemukan ]")
                        print()
                        
                        UserInput4 = input(">>>> Apakah mobil ini ingin disewa (ya/tidak): ")
                        
                        if UserInput4 == 'menu':
                            DividerPrompt("[ Data mobil belum disimpan ]", "< Kembali ke SUB-MENU > ")
                            continue
                        
                        elif UserInput4 == 'ya':
                            print()
                            UserInput5 = input(">>>>> Akan disewa mulai kapan? (DD-MM-YYYY): ")
                            
                            ListUserInput5Split = UserInput5.split("-")
                            LongIntUserInput5 = UserInput5.replace("-","")
                            
                            if LongIntUserInput5.isdigit() == True and len(ListUserInput5Split[0]) == 2 and int(ListUserInput5Split[0]) < 31 and len(ListUserInput5Split[1]) == 2 and int(ListUserInput5Split[1]) < 12 and len(ListUserInput5Split[2]) == 4:        
                                print()
                                UserInput6 = input(">>>>>>> Apakah anda yakin? ")
                                    
                                if UserInput6 == 'menu' or UserInput6 == 'tidak':
                                    DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")

                                elif UserInput6 == 'ya':
                                    print()
                                    UserInput7Upr = input(">>>>>>> Dengan jaminan apa? ").upper()
                                    
                                    if UserInput7Upr == 'MENU':
                                        DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                                        
                                    else:
                                        print()
                                        UserInput8 = input(">>>>>>> Apakah anda yakin? ")
                                    
                                        if UserInput8 == 'menu' or UserInput8 == 'tidak':
                                            DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                                            
                                        elif UserInput8 == 'ya':
                                            ChangeToDipakai(CheckPlatMobilIndex, UserInput5, UserInput7Upr)
                                            
                                            DividerPrompt("[ Mobil sukses disewa ]", "< Kembali ke SUB-MENU > ")
                                        
                                        else:
                                            DividerPrompt("[ Jawaban tidak sesuai ]", "< Kembali ke SUB-MENU > ")
                                        
                                else:
                                    DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
                            else:
                                DividerPrompt("[ Data mobil belum disimpan ]", "< Kembali ke SUB-MENU > ")
                                
                        elif UserInput4 == 'tidak':
                            DividerPrompt("[ Mobil gagal disewa ]", "< Kembali ke SUB-MENU > ")
                                                                        
                        else:
                            DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")                      
                    else:
                        DividerPrompt("[ Mobil sedang disewa ]", "< Kembali ke SUB-MENU > ")                 
                else:
                    DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
            else:
                DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")

        except ValueError:
            DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")


## Kembalikan Mobil - DONE
def KembalikanMobil():
    while True:
        TitleMenu("PENGEMBALIAN")
        SubMenu(DictSubMenu("Cari PLAT nomor mobil"))
        
        try:
            UserInput2 = input(">> Masukkan pilihan yang diinginkan: ")
            if UserInput2 == 'menu':
                DividerLine("> Kembali ke MENU UTAMA < ")
                break
            
            elif UserInput2 == '1':
                PrintCarList()
                
            elif UserInput2 == '2':
                print()
                PrintColomMobil()
                print()
                PrintDaftarMobil(Tersedia=0)
                
                print()
                UserInput3Upr = input(">>> Masukkan PLAT NOMOR mobil (Cth. B 1234 ABC): ").upper()
                
                ListUserInput3Split = UserInput3Upr.split(" ")
                
                if UserInput3Upr == 'MENU':
                    DividerLine("< Kembali ke SUB-MENU > ")
                    
                elif len(ListUserInput3Split) == 3:
                    print()
                    CheckPlatMobilTuple = CheckPlatMobil(ListUserInput3Split, UserInput3Upr)
                    
                    if CheckPlatMobilTuple == None:
                        DividerPrompt("[ Mobil tidak ditemukan ]", "< Kembali ke SUB-MENU > ")
                        continue
                    
                    CheckPlatMobilIndex = CheckPlatMobilTuple[0]
                    CheckPlatMobilValue = CheckPlatMobilTuple[1]
                                    
                    if CheckPlatMobilValue == 1 and DictMobil["Status"][CheckPlatMobilIndex] == 'Dipakai':
                        print("[ Mobil ditemukan ]")
                        print()
                        
                        UserInput4 = input(">>>> Apakah mobil ini ingin dikembalikan (ya/tidak): ")
                        
                        if UserInput4 == 'menu' or UserInput4 == 'tidak':
                            DividerPrompt("[ Data mobil belum disimpan ]", "< Kembali ke SUB-MENU > ")
                            continue
                        
                        elif UserInput4 == 'ya':
                            print()
                            UserInput5 = input(">>>>> Tanggal pengembalian mobil? (DD-MM-YYYY): ")
                            
                            ListUserInput5Split = UserInput5.split("-")
                            LongIntUserInput5 = UserInput5.replace("-","")
                            
                            if LongIntUserInput5.isdigit() == True and len(ListUserInput5Split[0]) == 2 and int(ListUserInput5Split[0]) < 31 and len(ListUserInput5Split[1]) == 2 and int(ListUserInput5Split[1]) < 12 and len(ListUserInput5Split[2]) == 4:        
                                print()
                                UserInput6 = input(">>>>>> Apakah anda yakin? ").lower()
                                
                                if UserInput6 == 'menu' or UserInput6 == 'tidak':
                                    DividerPrompt("[ Data mobil belum disimpan ]", "< Kembali ke SUB-MENU > ")
                                    continue
                                
                                elif UserInput6 == 'ya':
                                    ListDictMobil = DictMobil['Mulai'][CheckPlatMobilIndex]
                                    ListDictMobilSplit = ListDictMobil.split("-")
                                    
                                    if int(ListUserInput5Split[0]) > int(ListDictMobilSplit[0]) and int(ListUserInput5Split[1]) == int(ListDictMobilSplit[1]):
                                        Day = int(ListUserInput5Split[0]) - int(ListDictMobilSplit[0])
                                        Total = Day * DictMobil['Biaya'][CheckPlatMobilIndex]
                                        
                                        Pembayaran(Day, Total, CheckPlatMobilIndex)
                                        
                                    elif int(ListUserInput5Split[0]) < int(ListDictMobilSplit[0]) and int(ListUserInput5Split[1]) > int(ListDictMobilSplit[1]):
                                        Day = (int(ListUserInput5Split[0]) + (30 * (int(ListUserInput5Split[1]) - int(ListDictMobilSplit[1])))) - int(ListDictMobilSplit[0])
                                        Total = Day * DictMobil['Biaya'][CheckPlatMobilIndex]
                                        print()
                                        print(f"Waktu sewa adalah: {Day} hari")
                                        print(f"Total yang harus dibayar adalah: {Total:,}")
                                        print()
                                        UserInput7 = int(input(">>>>>>> Masukkan nominal pembayaran: "))
                                        
                                        if UserInput7 > Total:
                                            print(f"Terima Kasih, kembalian anda adalah: {(UserInput7 - Total):,}")
                                            ChangeToTersedia(CheckPlatMobilIndex)
                                            DividerPrompt("[ Mobil sukses dikembalikan ]", "< Kembali ke SUB-MENU > ")
                                        
                                        elif UserInput7 < Total:
                                            print(f"Uang anda tidak mencukupi, nominal yang harus dibayar adalah: {Total:,}")
                                            DividerPrompt("[ Pembayaran Gagal ]", "< Kembali ke SUB-MENU > ")
                                            
                                        else:
                                            print("Terima Kasih")
                                            ChangeToTersedia(CheckPlatMobilIndex)
                                            DividerPrompt("[ Mobil sukses dikembalikan ]", "< Kembali ke SUB-MENU > ")
                                    
                                    else:
                                        DividerPrompt("[ Pembayaran Gagal ]", "< Kembali ke SUB-MENU > ")
                                else:    
                                    DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
                            else:
                                DividerPrompt("[ Tanggal tidak sesuai ]", "< Kembali ke SUB-MENU > ")
                        else:
                            DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")              
                    else:
                        DividerPrompt("[ Mobil sedang tidak disewa ]", "< Kembali ke SUB-MENU > ")                 
                else:
                    DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
            else:
                DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")

        except ValueError:
            DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")


## Tambah Mobil - DONE
def TambahMobil():
    while True:
        TitleMenu("TAMBAH")
        SubMenu(DictSubMenu("Daftar mobil baru"))
        
        try:
            UserInput2 = input(">> Masukkan pilihan yang diinginkan: ")
            if UserInput2 == 'menu':
                DividerLine("> Kembali ke MENU UTAMA < ")
                break
            
            elif UserInput2 == '1':
                PrintCarList()
                
            elif UserInput2 == '2':
                print()
                UserInput3Upr = input(">>> Masukkan PLAT nomor mobil (Cth. B 1234 CTH): ").upper()
                ListUserInput3Split = UserInput3Upr.split(" ")
                
                if len(ListUserInput3Split) == 3:
                    print()
                    CheckPlatMobilTuple = CheckPlatMobil(ListUserInput3Split, UserInput3Upr)
                    
                    if CheckPlatMobilTuple == None:
                        print("[ Mobil belum terdaftar ]")
                        print()
                        UserInput4 = input(">>>> Apakah anda mau mendaftar mobil baru? (ya/tidak): ")
                        
                        if UserInput4 == 'tidak' or UserInput4 == 'menu':
                            DividerPrompt("[ Data mobil belum disimpan ]", "< Kembali ke SUB-MENU > ")
                            continue
                        
                        elif UserInput4 == 'ya':
                            TambahItemList = [UserInput3Upr]
                            TambahIndexList = [2]
                            
                            print()
                            UserInput5 = input(">>>>> (1/2) Masukkan 'Brand' dan 'Jenis' mobil (Cth. Toyota, Yaris): ").title()
                            UserInput5Split = UserInput5.split(", ")
                                
                            if len(UserInput5Split) == 2 and UserInput5.isdigit() == False:
                                TambahItemList.append(UserInput5Split[0])
                                TambahIndexList.append(1)
                                
                                TambahItemList.append(UserInput5Split[1])
                                TambahIndexList.append(0)
                                
                                print()
                                UserInput6 = input(">>>>>> (2/2) Masukkan 'Tahun' dan 'Kapasitas' mobil (Cth. 2022, 5): ")
                                UserInput6Split = UserInput6.split(", ")
                                
                                if len(UserInput6Split) == 2 and UserInput6Split[0].isdigit() == True and len(UserInput6Split[0]) == 4 and UserInput6Split[1].isdigit() == True and len(UserInput6Split[1]) > 0 and len(UserInput6Split[1]) < 99:
                                    TambahItemList.append(UserInput6Split[0])
                                    TambahIndexList.append(4)
                                    
                                    TambahItemList.append(UserInput6Split[1])
                                    TambahIndexList.append(3)
                                    
                                    TambahItemList.append("-")
                                    TambahIndexList.append(5)
                                    
                                    TambahItemList.append("Tersedia")
                                    TambahIndexList.append(6)
                                    
                                    TambahItemList.append("-")
                                    TambahIndexList.append(7)
                                    
                                    
                                    print()
                                    print("Mobil yang akan ditambahkan:")
                                    print()
                                    TambahListGabungan = list(zip(['Plat', 'Brand', 'Jenis', 'Tahun', 'Kapasitas'], TambahItemList))
                                    for i in range(len(TambahListGabungan)):
                                        print(TambahListGabungan[i])
                                    
                                    print()
                                    UserInput7 = input(">>>>>>> Apakah anda yakin? (ya/tidak): ")
                                    
                                    if UserInput7 == 'tidak' or UserInput7 == 'menu':
                                        DividerPrompt("[ Data mobil belum disimpan ]", "< Kembali ke SUB-MENU > ")
                                        continue
                                        
                                    elif UserInput7 == 'ya':
                                        for IndexIndex, ItemIndex in enumerate(TambahIndexList):
                                            for index, item in enumerate(DictMobil):
                                                if index == ItemIndex:
                                                    break
                                                else:
                                                    continue
                                            DictMobil[item].append(TambahItemList[IndexIndex])
                                        DictMobil["Dipakai"].append(1)
                                        
                                        DividerPrompt("[ Mobil berhasil ditambahkan ]", "< Kembali ke SUB-MENU > ")
                                        continue
                                    
                                    else:
                                        DividerPrompt("[ Jawaban tidak sesuai ]", "< Kembali ke SUB-MENU > ")
                                        continue
                                else:
                                    DividerPrompt("[ Data mobil salah ]", "< Kembali ke SUB-MENU > ")
                                    continue
                            else:
                                DividerPrompt("[ Data mobil salah ]", "< Kembali ke SUB-MENU > ")
                                continue
                        else:
                            DividerPrompt("[ Jawaban tidak sesuai ]", "< Kembali ke SUB-MENU > ")
                            continue
                        
                    CheckPlatMobilValue = CheckPlatMobilTuple[1]

                    if CheckPlatMobilValue == 1:
                        print("[ Mobil sudah terdaftar ]")
                        print()
                        UserInput4 = input(">>>> Apakah anda mau UPDATE data Mobil (ya/tidak): ")
                    
                        if UserInput4 == 'tidak' or UserInput4 == 'menu':
                            DividerLine("< Kembali ke SUB-MENU > ")
                        
                        elif UserInput4 == 'ya':
                            DividerLine("> Menuju MENU UPDATE <")
                            UpdateMobil()
                            
                        else:
                            DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
                    else:    
                        DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
                else:
                    DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
            else:
                DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
        except ValueError:
            DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")


## Update Mobil - DONE
def UpdateMobil():
    while True:
        TitleMenu("UPDATE")
        SubMenu(DictSubMenu("Masukkan PLAT nomor mobil"))
        
        try:
            UserInput2 = input(">> Masukkan pilihan yang diinginkan: ")
            if UserInput2 == 'menu':
                DividerLine("> Kembali ke MENU UTAMA < ")
                break
            
            elif UserInput2 == '1':
                PrintCarList()
            
            elif UserInput2 == '2':
                print()
                UserInput3Upr = input(">>> Masukkan PLAT nomor mobil (Cth. B 1234 CTH): ").upper()
                ListUserInput3Split = UserInput3Upr.split(" ")
                
                if len(ListUserInput3Split) == 3:
                    print()
                    CheckPlatMobilTuple = CheckPlatMobil(ListUserInput3Split, UserInput3Upr)
                    
                    if CheckPlatMobilTuple == None:
                        print("[ Mobil belum terdaftar ]")
                        print()
                        UserInput4 = input(">>>> Apakah anda mau TAMBAH data Mobil (ya/tidak): ")
                    
                        if UserInput4 == 'tidak' or UserInput4 == 'menu':
                            DividerLine("< Kembali ke SUB-MENU > ")
                            continue
                        
                        elif UserInput4 == 'ya':
                            DividerLine("> Menuju MENU TAMBAH MOBIL <")
                            TambahMobil()
                            continue
                        
                        else:
                            DividerPrompt("[ Jawaban tidak sesuai ]", "< Kembali ke SUB-MENU > ")
                            continue
                    
                    CheckPlatMobilIndex = CheckPlatMobilTuple[0]
                    CheckPlatMobilValue = CheckPlatMobilTuple[1]
                    
                    if CheckPlatMobilValue == 1:
                        print("[ Mobil ditemukan ]")
                        print()
                        UserInput4 = input(">>>> Apakah anda mau UPDATE data Mobil (ya/tidak): ")

                        if UserInput4 == 'tidak' or UserInput4 == 'menu':
                            DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                            
                        elif UserInput4 == 'ya':
                            print()
                            UserInput5 = input(">>>>> Masukkan Judul yang mau diganti (Cth. 'Brand'/'Tahun'): ").title()
                            
                            if UserInput5 == 'Menu':
                                DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                            
                            elif UserInput5 == 'Plat':
                                print()
                                UserInput6Upr = input(">>>>>> Ingin diganti menjadi? ").upper()
                                ListUserInput6Split = UserInput6Upr.split()

                                if UserInput6Upr == 'MENU':
                                    DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                                
                                elif len(ListUserInput6Split) == 3 and len(ListUserInput6Split[0]) > 0 and len(ListUserInput6Split[0]) < 3 and ListUserInput6Split[0].isdigit() == False and len(ListUserInput6Split[1]) > 0 and len(ListUserInput6Split[1]) < 5 and ListUserInput6Split[1].isdigit() == True and len(ListUserInput6Split[2]) > 0 and len(ListUserInput6Split[2]) < 4 and ListUserInput6Split[2].isdigit() == False:
                                    print()
                                    UserInput7 = input(">>>>>>> Apakah anda yakin? ")
                                    
                                    if UserInput7 == 'menu' or UserInput7 == 'tidak':
                                        DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                                    
                                    elif UserInput7 == 'ya':
                                        DictMobil['Plat'][CheckPlatMobilIndex] = UserInput6Upr
                                        DividerPrompt("[ Data sukses diganti ]", "< Kembali ke SUB-MENU > ")
                                        
                                    else:
                                        DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                                else:
                                    DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                            
                            elif UserInput5 == 'Status':
                                    print()
                                    UserInput6 = input(">>>>>> Apakah anda yakin? ")
                                    
                                    if UserInput6 == 'menu' or UserInput6 == 'tidak':
                                        DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                                    
                                    elif UserInput6 == 'ya':
                                        if DictMobil[UserInput5][CheckPlatMobilIndex] == "Tersedia":
                                            DictMobil[UserInput5][CheckPlatMobilIndex] = "Dipakai"
                                            DictMobil["Dipakai"][CheckPlatMobilIndex] = 1
                                            
                                        elif DictMobil[UserInput5][CheckPlatMobilIndex] == "Dipakai":
                                            DictMobil[UserInput5][CheckPlatMobilIndex] = "Tersedia"
                                            DictMobil["Dipakai"][CheckPlatMobilIndex] = 0
                                            
                                        DividerPrompt("[ Data sukses diganti ]", "< Kembali ke SUB-MENU > ")
                                    
                                    else:
                                        DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                                    
                            elif UserInput5 in DictMobil:
                                print()
                                UserInput6 = input(">>>>>> Ingin diganti menjadi? (Cth. Tanggal: DD-MM-YYYY, Plat: B 1234 CTH) ").title()
                                
                                if UserInput6 == 'Menu':
                                    DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                                
                                elif UserInput5 == 'Brand' or UserInput5 == 'Jenis':
                                    print()
                                    UserInput7 = input(">>>>>>> Apakah anda yakin? ")
                                    
                                    if UserInput7 == 'menu' or UserInput7 == 'tidak':
                                        DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                                    
                                    elif UserInput7 == 'ya':
                                        DictMobil[UserInput5][CheckPlatMobilIndex] = UserInput6
                                        DividerPrompt("[ Data sukses diganti ]", "< Kembali ke SUB-MENU > ")
                                    else:
                                        DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                                        
                                elif UserInput5 == 'Tahun' or UserInput5 == 'Kapasitas':
                                    print()
                                    UserInput7 = input(">>>>>>> Apakah anda yakin? ")
                                    
                                    if UserInput7 == 'menu' or UserInput7 == 'tidak':
                                        DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                                    
                                    elif UserInput7 == 'ya' and UserInput6.isdigit() == True and len(UserInput6) == 4 and int(UserInput6) > 0 and int(UserInput6) > 1999:
                                        DictMobil[UserInput5][CheckPlatMobilIndex] = int(UserInput6)
                                        DividerPrompt("[ Data sukses diganti ]", "< Kembali ke SUB-MENU > ")
                                    
                                    else:
                                        DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                                        
                                elif UserInput5 == 'Jaminan':
                                    UserInput6Upr = UserInput6.upper()
                                    print()
                                    UserInput7 = input(">>>>>>> Apakah anda yakin? ")
                                    
                                    if UserInput7 == 'menu' or UserInput7 == 'tidak':
                                        DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                                    
                                    elif UserInput7 == 'ya':
                                        DictMobil[UserInput5][CheckPlatMobilIndex] = UserInput6Upr
                                        DividerPrompt("[ Data sukses diganti ]", "< Kembali ke SUB-MENU > ")
                                    else:
                                        DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                        
                                elif UserInput5 == 'Mulai':
                                    ListUserInput6Split = UserInput6.split("-")
                                    LongIntUserInput6 = UserInput6.replace("-","")
                                    
                                    print()
                                    UserInput7 = input(">>>>>>> Apakah anda yakin? ")
                                    
                                    if UserInput7 == 'menu' or UserInput7 == 'tidak':
                                        DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                                    
                                    elif UserInput7 == 'ya' and LongIntUserInput6.isdigit() == True and len(ListUserInput6Split[0]) == 2 and len(ListUserInput6Split[0]) % 31 < 32 and len(ListUserInput6Split[1]) == 2 and  len(ListUserInput6Split[1]) % 12 < 13 and len(ListUserInput6Split[2]) == 4:
                                        DictMobil[UserInput5][CheckPlatMobilIndex] = UserInput6
                                        DividerPrompt("[ Data sukses diganti ]", "< Kembali ke SUB-MENU > ")
                                    else:
                                        DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                                else:
                                    DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")
                            else:
                                DividerPrompt("[ Data belum diganti ]", "< Kembali ke SUB-MENU > ")                    
                        else:
                            DividerPrompt("[ Jawaban tidak sesuai ]", "< Kembali ke SUB-MENU > ")
                    else:
                        DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
                else:
                    DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
            else:
                DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
        except ValueError:
            DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")


## Hapus Mobil - DONE
def HapusMobil():
    while True:
        TitleMenu("HAPUS")
        SubMenu(DictSubMenu("Cari PLAT nomor mobil"))
        
        try:
            UserInput2 = input(">> Masukkan pilihan yang diinginkan: ")
            
            if UserInput2 == 'menu':
                DividerLine("> Kembali ke MENU UTAMA < ")
                break
            
            elif UserInput2 == '1':
                PrintCarList()
                
            elif UserInput2 == '2':
                print()
                UserInput3Upr = input(">>> Masukkan PLAT NOMOR mobil (Cth. B 1234 CTH): ").upper()
                
                ListUserInput3Split = UserInput3Upr.split(" ")
                
                if len(ListUserInput3Split) == 3:
                    print()
                    CheckPlatMobilTuple = CheckPlatMobil(ListUserInput3Split, UserInput3Upr)
                    
                    if CheckPlatMobilTuple == None:
                        DividerPrompt("[ Mobil tidak ditemukan ]", "< Kembali ke SUB-MENU > ")
                        continue
                    
                    CheckPlatMobilIndex = CheckPlatMobilTuple[0]
                    CheckPlatMobilValue = CheckPlatMobilTuple[1]
                                    
                    if CheckPlatMobilValue == 1:
                        UserInput4 = input(">>>> Apakah anda mau HAPUS data mobil? (ya/tidak): ").upper()
                        
                        if UserInput4 == 'YA':
                            for index, item in enumerate(DictMobil["Plat"]):
                                
                                if CheckPlatMobilIndex == index:
                                    for index, (key, value) in enumerate(DictMobil.items()):
                                        del value[CheckPlatMobilIndex]
                                
                                else:
                                    continue
                            DividerPrompt("[ Mobil berhasil dihapus ]", "< Kembali ke SUB-MENU > ")
                        
                        elif UserInput4 == 'TIDAK':
                            DividerPrompt("[ Mobil tidak jadi dihapus ]", "< Kembali ke SUB-MENU > ")
                         
                        else:
                            DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
                    else:
                        DividerPrompt("[ Mobil tidak ditemukan ]", "< Kembali ke SUB-MENU > ")
                else:
                    DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
            else:
                DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")
        except ValueError:
            DividerPrompt("[ Index tidak sesuai ]", "< Kembali ke SUB-MENU > ")


# Program

## Variables

UserInput1 = 0
DictMainMenuValLen = 0

## Function

while UserInput1 != (DictMainMenuValLen + 1):
    TitleMenu("UTAMA RENTAL")
    MenuUtama()
    print()
    
    try:
        UserInput1 = int(input("> Pilih index menu yang diinginkan: "))
        print()
        
        if UserInput1 == 1:
            SubMenuDivider()
            DaftarMobil()
            
        elif UserInput1 == 2:
            SubMenuDivider()
            SewaMobil()
            
        elif UserInput1 == 3:
            SubMenuDivider()
            KembalikanMobil()
            
        elif UserInput1 == 4:
            SubMenuDivider()
            TambahMobil()
            
        elif UserInput1 == 5:
            SubMenuDivider()
            UpdateMobil()
            
        elif UserInput1 == 6:
            SubMenuDivider()
            HapusMobil()
        
        elif UserInput1 < 1 or UserInput1 > (DictMainMenuValLen + 1):
            print("- Masukkan input menu yang sesuai! -")
            print()
            SubMenuDivider()
    
    except ValueError:
        print()
        print("- Masukkan input menu yang sesuai! -")
        print()
        SubMenuDivider()       

else:
    DividerLine("Keluar dari program: Sukses! ")
    print()
    quit()