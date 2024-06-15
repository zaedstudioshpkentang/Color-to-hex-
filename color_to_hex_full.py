import webcolors

def color_to_hex(color_name):
    try:
        # Mendapatkan kode warna hex dari nama warna
        hex_code = webcolors.name_to_hex(color_name)
        return hex_code
    except ValueError:
        # Jika nama warna tidak ditemukan, kembalikan pesan "Unknown color"
        return "Unknown color"

def main():
    # Meminta input nama warna dari pengguna
    color_name = input("Enter the color name: ")
    # Mengkonversi nama warna menjadi kode warna hex
    hex_code = color_to_hex(color_name)
    # Mencetak hasil konversi
    print(f"The hex code for {color_name} is: {hex_code}")

if __name__ == "__main__":
    main()