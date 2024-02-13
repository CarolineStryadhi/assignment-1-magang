def urut_kata(input_string):
# Klasifikasi kata dalam string jadi list
    kata = input_stringnya.split()

# Balik urutan list kata
    urut_done = ' '.join(kata[::-1])

    return urut_terbaik

# Manggil fungsi
input_stringnya = "saya sedang makan nasi"
menghasilkan = urut_kata(input_stringnya)
print(menghasilkan)
