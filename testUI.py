import random
import time

suffix_counter = 0


suffix_types_inflection = ["Çoğul eki",
    "Hâl ekleri",
    "İyelik ekleri (tamlanan ekleri)",
    "İlgi ekleri (tamlayan ekleri)",
    "Eşitlik eki",
    "Vasıta eki",
    "Haber (bildirme) kip ekleri",
    "Dilek kip ekleri",
    "Ek-fiiller",
    "Şahıs (kişi) ekleri",
    "Mastar Ekleri"]

suffix_types_constr = ["İsimden İsim Yapan Ekler (İİYE)",
    "İsimden Fiil Yapan Ekler (İFYE)",
    "Fiilden İsim Yapan Ekler (FİYE)",
    "Fiilden Fiil Yapan Ekler (FFYE)"]

case_suffixes = ["Belirtme",
    "Yönelme",
    "Bulunma",
    "Ayrılma"]


subtitles = {"Hâl ekleri" : case_suffixes}



def hüso_ad_bulamadım():
    print("ÇEKİM EKLERİ")
    for i in suffix_types_inflection:
        if i in subtitles.keys():
            print(str(suffix_counter + 1) + ": " + i.capitalize())
            for j in range(1):
                for k in range(len(subtitles[i])):
                    print(str(suffix_counter + 1) + "-" + str(k + 1) + ": " + subtitles[i][k])
            suffix_counter += 1
        else:
            print(str(suffix_counter + 1) + ": " + i)
            suffix_counter += 1
    print("\n")

    print("YAPIM EKLERİ")
    for i in suffix_types_constr:
        print(str(suffix_counter + 1) + ": " + i)
        suffix_counter += 1
