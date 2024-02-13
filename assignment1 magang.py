def urut_kata(input_string):
# Klasifikasi kata dalam string jadi list
    kata = input_stringnya.split()

# Balik urutan list kata
    urut_berhasil = ' '.join(kata[::-1])

    return urut_berhasil

# Manggil fungsi
input_stringnya = "saya sedang makan nasi"
menghasilkan = urut_kata(input_stringnya)
print(menghasilkan)
