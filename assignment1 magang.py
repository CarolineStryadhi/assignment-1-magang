def urut_katanya(input_stringnya):
# Klasifikasi katanya dalam string jadi list
    katanya = input_stringnya.split()

# Balik urutan list katanya
    urut_berhasil = ' '.join(katanya[::-1])

    return urut_berhasil

# Manggil fungsi
input_stringnya = "saya sedang makan nasi"
menghasilkan = urut_katanya(input_stringnya)
print(menghasilkan)
