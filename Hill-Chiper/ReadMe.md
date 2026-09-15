# Hill Cipher

Implementasi algoritma **Hill Cipher 2×2** menggunakan bahasa pemrograman C++. Program ini dibuat untuk memenuhi tugas praktikum Kriptografi Pertemuan 2.

## Identitas

* **Nama:** Ibnaty Farah Rabbany
* **NPM:** 140810240022
* **Mata Kuliah:** Kriptografi
* **Pertemuan:** 02
* **Algoritma:** Hill Cipher
* **Bahasa Pemrograman:** C++

---

## Deskripsi

Hill Cipher merupakan algoritma kriptografi yang menggunakan **matriks sebagai kunci** dan operasi **aritmatika modulo** dalam proses enkripsi dan dekripsi.

Program ini menggunakan matriks kunci berordo **2×2**, sehingga plaintext diproses dalam blok yang terdiri dari dua karakter.

Pemetaan karakter yang digunakan adalah:

```text
A = 0
B = 1
C = 2
...
Z = 25
```

Program memiliki tiga fitur utama:

1. Enkripsi Hill Cipher
2. Dekripsi Hill Cipher
3. Mencari kunci Hill Cipher

---

## Alur Program

### 1. Enkripsi

Proses enkripsi menggunakan rumus:

$$
C = K \times P \pmod{26}
$$

dengan:

* `C` = ciphertext
* `K` = matriks kunci
* `P` = plaintext

Tahapan proses:

1. Pengguna memilih menu **Enkripsi**.
2. Pengguna memasukkan matriks kunci berordo 2×2.
3. Pengguna memasukkan plaintext.
4. Plaintext dikonversi dari huruf menjadi angka 0–25.
5. Plaintext dibagi menjadi blok yang terdiri dari dua karakter.
6. Setiap blok dikalikan dengan matriks kunci.
7. Hasil perkalian dilakukan modulo 26.
8. Hasil angka dikonversi kembali menjadi huruf.
9. Program menampilkan ciphertext.

Contoh:

```text
Plaintext : KRIPTO

Kunci:
3 2
2 7

Ciphertext : MJCRHG
```

---

### 2. Dekripsi

Proses dekripsi menggunakan rumus:

$$
P = K^{-1} \times C \pmod{26}
$$

Sebelum melakukan dekripsi, program mencari invers dari matriks kunci.

Tahapannya:

1. Pengguna memilih menu **Dekripsi**.
2. Pengguna memasukkan matriks kunci.
3. Pengguna memasukkan ciphertext.
4. Program menghitung determinan matriks kunci.
5. Program mencari invers modulo dari determinan.
6. Program menentukan invers matriks kunci.
7. Ciphertext dikalikan dengan invers matriks kunci.
8. Hasil dilakukan modulo 26.
9. Angka dikonversi kembali menjadi huruf.
10. Program menampilkan plaintext.

Jika matriks kunci tidak memiliki invers modulo 26, proses dekripsi tidak dapat dilakukan.

---

### 3. Mencari Kunci

Program juga menyediakan fitur untuk mencari matriks kunci berdasarkan plaintext dan ciphertext yang diketahui.

Rumus yang digunakan:

$$
K = C \times P^{-1} \pmod{26}
$$

Tahapan proses:

1. Pengguna memilih menu **Mencari Kunci**.
2. Pengguna memasukkan plaintext.
3. Pengguna memasukkan ciphertext.
4. Plaintext dan ciphertext dikonversi menjadi angka.
5. Data disusun menjadi matriks.
6. Program mencari invers matriks plaintext.
7. Program menghitung perkalian:

$$
C \times P^{-1}
$$

8. Hasil dilakukan modulo 26.
9. Program menampilkan matriks kunci Hill Cipher.

Matriks plaintext harus memiliki invers modulo 26 agar kunci dapat ditemukan.

---

## Struktur Program

Program dibagi menjadi beberapa fungsi agar setiap proses lebih terstruktur.

| Fungsi            | Kegunaan                                          |
| ----------------- | ------------------------------------------------- |
| `mod()`           | Menghasilkan nilai modulo 26                      |
| `inverseMod()`    | Mencari invers modulo suatu bilangan              |
| `textToNumbers()` | Mengubah huruf menjadi angka 0–25                 |
| `numbersToText()` | Mengubah angka menjadi huruf                      |
| `multiply()`      | Melakukan perkalian matriks dengan blok plaintext |
| `inverseMatrix()` | Mencari invers matriks 2×2                        |
| `encrypt()`       | Melakukan proses enkripsi                         |
| `decrypt()`       | Melakukan proses dekripsi                         |
| `findKey()`       | Mencari matriks kunci                             |
| `main()`          | Menampilkan menu dan menerima input pengguna      |

---

## Cara Menjalankan Program

Pastikan compiler C++ seperti **g++/MinGW** telah terpasang.

Buka terminal pada folder tempat file `hillcipher.cpp` berada, kemudian jalankan:

```bash
g++ hillcipher.cpp -o hillcipher
```

Setelah proses kompilasi berhasil, jalankan program dengan:

### Windows PowerShell

```bash
.\hillcipher.exe
```

atau:

```bash
./hillcipher.exe
```

---

## Menu Program

Saat program dijalankan, pengguna akan mendapatkan tiga pilihan:

```text
=== HILL CIPHER ===
1. Enkripsi
2. Dekripsi
3. Mencari Kunci
Pilihan:
```

Pengguna dapat memilih menu sesuai kebutuhan.

---

## Contoh Running Program

### Enkripsi

Input:

```text
=== HILL CIPHER ===
1. Enkripsi
2. Dekripsi
3. Mencari Kunci
Pilihan: 1

Masukkan matriks kunci 2x2:
3 2
2 7

Masukkan teks: KRIPTO

Ciphertext: MJCRHG
```

### Dekripsi

Input:

```text
=== HILL CIPHER ===
1. Enkripsi
2. Dekripsi
3. Mencari Kunci
Pilihan: 2

Masukkan matriks kunci 2x2:
3 2
2 7

Masukkan teks: MJCRHG

Plaintext: KRIPTO
```

### Mencari Kunci

Input:

```text
=== HILL CIPHER ===
1. Enkripsi
2. Dekripsi
3. Mencari Kunci
Pilihan: 3

Masukkan plaintext minimal 4 karakter: FRIDAY
Masukkan ciphertext: PQCFKU
```

Output berupa matriks kunci yang diperoleh dari perhitungan:

$$
K=C\times P^{-1}\pmod{26}
$$

---

## Screenshot Running Program

### 1. Screenshot Enkripsi


```text
screenshots/enkripsi.png
```

### 2. Screenshot Dekripsi


```text
screenshots/dekripsi.png
```

### 3. Screenshot Mencari Kunci

```text
screenshots/mencari-kunci.png
```

---


## Kesimpulan

Program Hill Cipher ini mengimplementasikan tiga proses utama, yaitu **enkripsi, dekripsi, dan pencarian kunci** menggunakan matriks berordo 2×2 dan aritmatika modulo 26.

Pada proses enkripsi, plaintext dikalikan dengan matriks kunci. Pada proses dekripsi, ciphertext dikalikan dengan invers matriks kunci. Sementara itu, proses pencarian kunci dilakukan dengan menggunakan plaintext dan ciphertext yang diketahui melalui persamaan:

$$
K = C \times P^{-1} \pmod{26}
$$

Dengan demikian, program dapat digunakan untuk memahami penerapan operasi matriks dalam algoritma Hill Cipher.
