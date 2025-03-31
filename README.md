---

# Program Python input otomatis dengan Selenium
![image](https://github.com/user-attachments/assets/7a699e4e-27a5-4782-bc16-35291df72086)

Program ini menggunakan library selenium untuk melakukan input dan submit otomatis sebuah form

---

## Persiapan

1. **Instal Selenium** : [https://pypi.org/project/selenium/](url)
2. **Unduh Browser Chrome** : [https://www.google.com/chrome/](url)
3. **Unduh Code Editor untuk memudahkan** : [https://code.visualstudio.com/](url)

## Cara Kerja Program

1. Program membuka halaman `https://demoqa.com/webtables`.
2. Program mengisi formulir dengan data yang sudah ditentukan:
   - Nama Depan
   - Nama Belakang
   - Email
   - Usia
   - Gaji
   - Departemen
3. Setelah data dimasukkan, program mengklik tombol "Submit" untuk mengirimkan formulir.
4. Proses ini diulang untuk setiap data dalam dictionary `Data_Registration`.

## Menjalankan Program

Jalankan skrip Python dengan perintah:

```bash
python nama_skrip.py
```

Program akan membuka browser dan mengisi formulir secara otomatis.

---

- Ok Gas
