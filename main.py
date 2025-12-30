# main.py
from src.collatz_bitstream import CollatzBitstreamGenerator

if __name__ == "__main__":
    try:
        seed_input = int(input("Başlangıç değerini (Seed) girin: "))
        generator = CollatzBitstreamGenerator(seed_input)
        key = generator.generate_64bit_key_hex()
        print(f"\n[SİSTEM] Üretilen Anahtar: {key}")
    except ValueError as e:
        print(f"Hata: {e}")