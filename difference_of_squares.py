toplam1 = 0
toplam2 = 0
for i in range(1,11):
    toplam1 = toplam1 + i
    islem1 = toplam1 ** 2
    print("İlk on doğal sayının toplamının karesi:", islem1)
    islem2 = i ** 2
    toplam2 = toplam2 + islem2
    print("İlk on doğal sayının karelerinin toplamı:", toplam2)
