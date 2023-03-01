# Cara 1
# print("==================== BARIS ARITMATIKA ====================")
# awal = int(input("Masukkan bilangan awal : "))
# selisih = int(input("Masukkan selisih bilangan : "))
# suku = int(input("Masukkan banyaknya suku : "))
# # rumus = awal+(suku-1)*selisih
# rumus = (selisih/2)*(2*awal+(suku-1)*selisih)
# print("Total dari deret aritmatika tersebut adalah : ",rumus)

# cara 2
print("="*20,"BARIS ARITMATIKA","="*20)
def fungsi_aritmatika (a, b, n):
    rumus = ( n / 2 ) * (2 * a + ( n - 1 ) * b)
    return rumus

a = int(input("Masukkan bilangan awal : "))
b = int(input("Masukkan selisih bilangan : "))
n = int(input("Masukkan banyaknya suku : "))
print("Total dari deret aritmatika tersebut adalah",fungsi_aritmatika(a,b,n))