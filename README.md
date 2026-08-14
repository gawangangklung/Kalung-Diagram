# Kalung-Diagram

Aplikasi sederhana untuk menerjemahkan nomor Angklung ke semua nada dasar.

Kebutuhan minimum: Python 3.9+.

## Menjalankan aplikasi

```bash
python angklung_translator.py --source C "1 2 3 4 5 6 7"
```

Output akan menampilkan terjemahan ke 12 nada dasar.
Jika Anda memakai penanda oktaf (`+1`, `-1`, dst.), hasil akan mengikuti posisi oktaf relatif pada nada dasar tujuan.

### Contoh terjemahan ke satu nada dasar

```bash
python angklung_translator.py --source C --target D "1 2 3 4 5 6 7"
```
