# 🔐 Collatz Bitstream Generator

> Deterministik bir matematiksel sistem, kaotik bir bit dizisi üretebilir mi?

Bu proje, **Collatz Sanısı (3n + 1 problemi)** temel alınarak geliştirilen,
deterministik fakat kaotik davranış sergileyen bir **bit akışı (bitstream) üretim sistemi**dir.

---

## 🎯 Projenin Amacı

Bu çalışmanın amacı:

- Basit bir matematiksel dönüşüm sisteminden
- Tek/çift kontrolüne dayalı olarak
- Kaotik görünümlü bir bit dizisi üretmek
- Bu bit dizisini 64-bit hexadecimal bir anahtar olarak ifade etmektir

> ⚠️ Bu proje **akademik ve deneysel amaçlıdır**.  
> Kriptografik güvenlik garantisi vermez.

---

## 🧠 Matematiksel Model

Sistem **Collatz dönüşümüne** dayanır:
f(x) =
x / 2 → x çift ise
3x + 1 → x tek ise

---

## 🔁 Bit Üretim Mekanizması

Her Collatz adımı **aynı zamanda bir bit üretir**:

| Sayının Durumu | Üretilen Bit |
|---------------|--------------|
| Çift          | 0            |
| Tek           | 1            |

Bu yöntem tahtadaki modelle birebir uyumludur.

---

## 🔄 4 → 2 → 1 Döngüsü ve Çözüm

Collatz dizisi kaçınılmaz olarak:

4 → 2 → 1 → 4

döngüsüne girer.

Bu projede:
- Sistem `1` değerine ulaştığında **durmaz**
- Seed değeri kontrollü biçimde eklenir
- Bit üretimi kesintisiz devam eder

Bu yaklaşım:
- Tekrarı azaltır
- Bit akışının kaotik görünümünü artırır

---

## ✂️ Bit Kırpma (Truncation)

- Sistem arka planda **68 bit** üretir
- Son **4 bit bilinçli olarak atılır**
- Kullanıcıya **64-bit** bir anahtar sunulur

Amaç:
- İç durumun doğrudan gözlemlenmesini zorlaştırmak

---

## ⚙️ Algoritma Akışı

1. Seed alınır
2. Collatz sistemi başlatılır
3. Her adımda:
   - Tek/çift kontrolü yapılır
   - Bit üretilir
   - Collatz dönüşümü uygulanır
4. 68 bit tamamlanınca:
   - Son 4 bit kırpılır
   - 64-bit hex anahtar oluşturulur
![Algoritma_akıs_diyagramı.png](../../Downloads/Algoritma_ak%C4%B1s_diyagram%C4%B1.png)

---

## ▶️ Örnek Çalıştırma

```bash
python collatz_bitstream.py
Örnek çıktı:
Üretilen 64-bit Anahtar (hex): 9a3f4c21b8e0d112
```
🚧 **Sınırlamalar**

Collatz sanısı matematiksel olarak kanıtlanmamıştır

Sistem deterministiktir

Kriptografik olarak güvenli kabul edilmez

Eğitim, analiz ve algoritmik düşünme amaçlıdır

📚 **Kullanım Alanları**

Matematik & algoritma eğitimi

Kaotik sistemlerin incelenmesi

Bitstream üretim deneyleri

Akademik sunumlar

📌 Lisans

Bu proje eğitim amaçlıdır ve serbestçe kullanılabilir.

---
