# 🛡 PDF Security Manager v2.0

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**PDF Security Manager**, Python kullanılarak geliştirilmiş, PDF dosyalarını hızlı ve güvenli şekilde şifrelemek (encrypt) ve şifrelerini çözmek (decrypt) için tasarlanmış gelişmiş bir komut satırı aracıdır (CLI).

Bu proje; dosya işleme, hata yönetimi, kullanıcı etkileşimi ve harici kütüphane kullanımı açısından örnek bir uygulamadır.

---

## 🚀 Özellikler

* **📂 Akıllı Dosya Algılama:** Çalışılan dizindeki tüm `.pdf` dosyaları otomatik olarak taranır ve listelenir.
* **🔒 AES Şifreleme:** PDF’lerinizi güçlü şifreleme yöntemleriyle koruma altına alır.
* **🔓 Şifre Çözme:** Şifresi bilinen kilitli PDF dosyalarının kilidini kaldırır.
* **👀 Gizli Şifre Girişi:** Şifreler terminal üzerinde görünmeden (`getpass` modülü ile) güvenli bir şekilde alınır.
* **🔄 Döngüsel Menü:** İşlem sonrasında program kapanmaz, kullanıcı çıkış yapana kadar ana menüye döner.
* **🎨 Kullanıcı Dostu Arayüz:** Emoji destekli, sade ve anlaşılır CLI tasarımı.

---

## 🛠 Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### 1. Gereksinimler
* Python 3.x
* `PyPDF2` kütüphanesi

### 2. Projeyi İndirme

Terminal veya komut satırını açın ve projeyi klonlayın:

```bash
git clone [https://github.com/musayoncalik/-PDF-Security-Manager.git](https://github.com/musayoncalik/-PDF-Security-Manager.git)
cd -PDF-Security-Manager
3. Gerekli Kütüphaneleri Yükleme
Gerekli bağımlılıkları yüklemek için:

Bash

pip install -r requirements.txt
Alternatif olarak manuel yükleme:

Bash

pip install PyPDF2
💻 Kullanım
Proje klasörü içerisindeyken aşağıdaki komutu çalıştırarak uygulamayı başlatın:

Bash

python pdf_security_manager.py
🔧 İşleyiş Adımları
Program açıldığında bulunduğunuz klasördeki PDF dosyaları otomatik listelenir.

İşlem yapmak istediğiniz dosya numarasını seçin.

Yapmak istediğiniz işlemi seçin:

[1] Şifrele (Dosyayı kilitler)

[2] Şifreyi Çöz (Kilidi kaldırır)

Şifreyi girin (veya belirleyin).

Program orijinal dosyayı bozmaz, işlemin sonucunu yeni bir dosya olarak kaydeder:

dosyaadi_sifreli.pdf

dosyaadi_cozulmus.pdf

📷 Örnek Çıktı
Program çalıştırıldığında terminalde aşağıdaki gibi bir arayüz ile karşılaşırsınız:

Plaintext

******************************************
   🛡  PDF SECURITY MANAGER v2.0
******************************************

📂 MEVCUT PDF DOSYALARI
========================================
  [1] maas_bordrosu.pdf
  [2] odev_notlari.pdf
  [0] ÇIKIŞ

👉 Dosya numarasını girin: 1

----------------------------------------
📄 SEÇİLEN: maas_bordrosu.pdf
----------------------------------------
1. Şifrele (Kilitle)
2. Şifreyi Çöz (Kilidi Kaldır)
0. İptal / Ana Menüye Dön

👉 İşlem seçin (0-2): 1

🔒 'maas_bordrosu.pdf' şifreleniyor...
🔑 Oluşturulacak şifreyi girin: 

✅ BAŞARILI! Yeni dosya: maas_bordrosu_sifreli.pdf
📂 Proje Yapısı
Plaintext

pdf-security-manager/
├── pdf_security_manager.py       # Ana uygulama kaynak kodu
├── pdf_security_manager.ipynb    # Jupyter Notebook sürümü (Opsiyonel)
├── requirements.txt              # Proje bağımlılıkları
├── README.md                     # Proje dokümantasyonu
└── .gitignore                    # Gereksiz dosyaların takibini engelleme
