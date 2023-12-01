import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    tebakan = None
    percobaan = 0

    print("Selamat datang di Game Tebak Angka!")
    print("Saya telah memilih sebuah angka antara 1 dan 100. Coba tebak!")

    while tebakan != angka_rahasia:
        tebakan = int(input("Masukkan tebakan Anda: "))
        percobaan += 1

        if tebakan < angka_rahasia:
            print("Tebakan terlalu rendah. Coba lagi.")
        elif tebakan > angka_rahasia:
            print("Tebakan terlalu tinggi. Coba lagi.")
        else:
            print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan.")

if __name__ == "__main__":
    tebak_angka()
