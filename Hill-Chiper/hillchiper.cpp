/*
Nama Program : Algoritma Hill Chiper
Nama         : Ibnaty Farah Rabbany
NPM          : 140810240022
Tanggal      : 15 September 2026
*/

#include <iostream>
#include <string>
#include <cctype>
using namespace std;

const int MOD = 26;

int mod(int x) {
    return (x % MOD + MOD) % MOD;
}

int inverseMod(int a) {
    a = mod(a);

    for (int i = 1; i < MOD; i++)
        if (mod(a * i) == 1)
            return i;

    return -1;
}

void textToNumbers(string text, int num[]) {
    int j = 0;

    for (char c : text) {
        if (isalpha(c)) {
            num[j++] = toupper(c) - 'A';
        }
    }
}

string numbersToText(int num[], int n) {
    string result;

    for (int i = 0; i < n; i++)
        result += char(num[i] + 'A');

    return result;
}

void multiply(int K[2][2], int P[2], int C[2]) {
    C[0] = mod(K[0][0] * P[0] + K[0][1] * P[1]);
    C[1] = mod(K[1][0] * P[0] + K[1][1] * P[1]);
}

bool inverseMatrix(int K[2][2], int Inv[2][2]) {
    int det = mod(K[0][0] * K[1][1] - K[0][1] * K[1][0]);
    int invDet = inverseMod(det);

    if (invDet == -1)
        return false;

    Inv[0][0] = mod(invDet * K[1][1]);
    Inv[0][1] = mod(-invDet * K[0][1]);
    Inv[1][0] = mod(-invDet * K[1][0]);
    Inv[1][1] = mod(invDet * K[0][0]);

    return true;
}

string encrypt(string text, int K[2][2]) {
    int n = 0;

    for (char c : text)
        if (isalpha(c))
            n++;

    int *P = new int[n];
    int *C = new int[n];

    textToNumbers(text, P);

    for (int i = 0; i < n; i += 2) {
        int block[2] = {P[i], P[i + 1]};
        int result[2];

        multiply(K, block, result);

        C[i] = result[0];
        C[i + 1] = result[1];
    }

    string result = numbersToText(C, n);

    delete[] P;
    delete[] C;

    return result;
}

string decrypt(string text, int K[2][2]) {
    int Inv[2][2];

    if (!inverseMatrix(K, Inv))
        return "Kunci tidak memiliki invers modulo 26.";

    return encrypt(text, Inv);
}

void findKey(string plaintext, string ciphertext) {
    int Pnum[100], Cnum[100];

    textToNumbers(plaintext, Pnum);
    textToNumbers(ciphertext, Cnum);

    // Mengambil dua blok pertama plaintext
    int P[2][2] = {
        {Pnum[0], Pnum[2]},
        {Pnum[1], Pnum[3]}
    };

    // Mengambil dua blok pertama ciphertext
    int C[2][2] = {
        {Cnum[0], Cnum[2]},
        {Cnum[1], Cnum[3]}
    };

    int PInv[2][2];

    if (!inverseMatrix(P, PInv)) {
        cout << "\nMatriks plaintext tidak memiliki invers modulo 26.\n";
        cout << "Kunci tidak dapat ditemukan.\n";
        return;
    }

    int K[2][2];

    // K = C x P^-1
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            K[i][j] = mod(
                C[i][0] * PInv[0][j] +
                C[i][1] * PInv[1][j]
            );
        }
    }

    cout << "\nKunci Hill Cipher:\n";
    cout << "[ " << K[0][0] << " " << K[0][1] << " ]\n";
    cout << "[ " << K[1][0] << " " << K[1][1] << " ]\n";

    // Verifikasi kunci
    string hasil = encrypt(plaintext, K);

    cout << "\nVerifikasi:\n";
    cout << "Ciphertext hasil : " << hasil << endl;
    cout << "Ciphertext input : " << ciphertext << endl;

    if (hasil == ciphertext)
        cout << "Kunci valid.\n";
    else
        cout << "Kunci tidak sesuai dengan ciphertext.\n";
}

int main() {
    int pilihan;

    cout << "=== HILL CIPHER ===\n";
    cout << "1. Enkripsi\n";
    cout << "2. Dekripsi\n";
    cout << "3. Mencari Kunci\n";
    cout << "Pilihan: ";
    cin >> pilihan;

    if (pilihan == 1 || pilihan == 2) {
        int K[2][2];
        string text;

        cout << "\nMasukkan matriks kunci 2x2:\n";
        cin >> K[0][0] >> K[0][1];
        cin >> K[1][0] >> K[1][1];

        cout << "Masukkan teks: ";
        cin >> text;

        if (text.length() % 2 != 0) {
            cout << "Jumlah karakter harus genap.\n";
            return 0;
        }

        if (pilihan == 1)
            cout << "\nCiphertext: " << encrypt(text, K) << endl;
        else
            cout << "\nPlaintext: " << decrypt(text, K) << endl;
    }
    else if (pilihan == 3) {
        string plaintext, ciphertext;

        cout << "\nMasukkan plaintext minimal 4 karakter: ";
        cin >> plaintext;

        cout << "Masukkan ciphertext: ";
        cin >> ciphertext;

        if (plaintext.length() != ciphertext.length() ||
            plaintext.length() < 4 ||
            plaintext.length() % 2 != 0) {
            cout << "Panjang plaintext dan ciphertext harus sama, ";
            cout << "genap, dan minimal 4 karakter.\n";
            return 0;
        }

        findKey(plaintext, ciphertext);
    }
    else {
        cout << "Pilihan tidak valid.\n";
    }

    return 0;
}