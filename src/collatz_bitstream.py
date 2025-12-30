# collatz_bitstream.py

class CollatzBitstreamGenerator:
    def __init__(self, seed: int):
        if seed <= 0:
            raise ValueError("Seed pozitif bir tam sayı olmalıdır.")
        self.seed = seed

    def collatz_step(self, x: int) -> int:
        """
        Collatz dönüşümü:
        - x çiftse  -> x / 2
        - x tekse   -> 3x + 1
        """
        if x % 2 == 0:
            return x // 2
        else:
            return 3 * x + 1

    def generate_bits(self, total_bits: int = 68) -> list:
        """
        Collatz adımlarından bit üretir.
        Çift -> 0
        Tek  -> 1
        """
        bits = []
        x = self.seed

        while len(bits) < total_bits:
            if x % 2 == 0:
                bits.append(0)
            else:
                bits.append(1)

            # Collatz geçişi
            x = self.collatz_step(x)

            # 4-2-1 döngüsünü bilinçli kır
            if x == 1:
                x = x + self.seed  # kontrollü yeniden tohumlama

        return bits

    def generate_64bit_key_hex(self) -> str:
        """
        68 bit üretir, son 4 biti kırpar,
        64-bit hexadecimal anahtar döndürür.
        """
        bits = self.generate_bits(68)

        # Son 4 bit kırpılır
        trimmed_bits = bits[:-4]

        # Bit dizisini integer'a çevir
        value = 0
        for bit in trimmed_bits:
            value = (value << 1) | bit

        # 64-bit hex çıktı
        return f"{value:016x}"


# =========================
# ÖRNEK KULLANIM
# =========================
if __name__ == "__main__":
    seed = 9
    generator = CollatzBitstreamGenerator(seed)

    key_hex = generator.generate_64bit_key_hex()
    print("Üretilen 64-bit Anahtar (hex):", key_hex)

