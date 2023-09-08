def hitung_rata_rata(angka):
    total= sum(angka)
    rata_rata = total /len(angka)
    return rata_rata

def input_angka():
    angka= []
    while True:
        try:
            bilangan=float(input("masukkan angka (0 untuk mengakhiri):"))
            if bilangan == 0:
                break
            angka.append(bilangan)
        except ValueError:
            print("Masukkan angka yang valid")
    return angka
    
if __name__ =="__main__":
        print("Program Menghitung rata-rata")
        daftar_angka = input_angka()
        
        if daftar_angka:
            rata_rata = hitung_rata_rata(daftar_angka)
            print(f"rata rata dari angka-angka yang dimasukkan adalah: {rata_rata:.2f}")
        else:
            print("tidak ada angka yang dimasukkan")