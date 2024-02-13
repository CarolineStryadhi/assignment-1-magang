def urutan_terbaik_kata(input_string):
# Klasifikasi kata dalam string jadi list
    kata = input_string.split()

# Balik urutan list kata
    urutan_terbaik = ' '.join(kata[::-1])

    return urutan_terbaik

# Manggil fungsi
input_string = "saya sedang makan nasi"
hasil = urutan_terbaik_kata(input_string)
print(hasil)