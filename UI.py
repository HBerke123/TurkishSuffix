suffix_counter = 0
suffix_types_inflection = ["Çoğul eki", "Hâl ekleri", "İyelik ekleri (tamlanan ekleri)", "İlgi ekleri (tamlayan ekleri)", "Eşitlik eki", "Vasıta eki", "Haber (bildirme) kip ekleri", "Dilek kip ekleri", "Ek-fiiller", "Şahıs (kişi) ekleri", "Mastar Ekleri"]

suffix_types_constr = ["İsimden İsim Yapan Ekler (İİYE)", "İsimden Fiil Yapan Ekler (İFYE)", "Fiilden İsim Yapan Ekler (FİYE)", "Fiilden Fiil Yapan Ekler (FFYE)"]

def dui():
    global suffix_counter
    global suffix_types_constr
    global suffix_types_inflection

    print("ÇEKİM EKLERİ")
    for i in suffix_types_inflection:
        print(str(suffix_counter + 1) + ": " + i)
        suffix_counter += 1
    print("\n")

    print("YAPIM EKLERİ")
    for i in suffix_types_constr:
        print(str(suffix_counter + 1) + ": " + i)
        suffix_counter += 1
