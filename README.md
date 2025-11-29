🛡 PDF Security Manager v2.0

PDF Security Manager, Python kullanılarak geliştirilmiş, PDF dosyalarını hızlı ve güvenli şekilde şifrelemek (encrypt) ve şifrelerini çözmek (decrypt) için tasarlanmış gelişmiş bir komut satırı aracıdır (CLI).
Bu proje; dosya işleme, hata yönetimi, kullanıcı etkileşimi ve harici kütüphane kullanımı açısından örnek bir uygulamadır.

🚀 Özellikler

📂 Akıllı Dosya Algılama
Çalışılan dizindeki tüm .pdf dosyaları otomatik olarak listelenir.

🔒 AES Şifreleme
PDF’lerinizi güçlü şifreleme yöntemiyle korur.

🔓 Şifre Çözme
Şifresi bilinen kilitli PDF’leri açabilir.

👀 Gizli Şifre Girişi
Şifreler getpass ile gizli şekilde alınır.

🔄 Döngüsel Menü
İşlem sonrasında program kapanmaz, ana menüye döner.

🎨 Kullanıcı Dostu Arayüz
Emoji destekli sade ve anlaşılır CLI tasarımı.

🛠 Kurulum
1. Gereksinimler

Python 3.x

PyPDF2 kütüphanesi

2. Projeyi İndirme
git clone https://github.com/musayoncalik/-PDF-Security-Manager.git
cd -PDF-Security-Manager

3. Gerekli Kütüphaneyi Yükleme
pip install PyPDF2


Alternatif:

pip install -r requirements.txt

💻 Kullanım

Proje klasörüne girerek programı başlatın:

python pdf_security_manager.py

🔧 İşleyiş Adımları

Program açıldığında klasördeki PDF dosyaları listelenir.

İşlem yapılacak dosyanın numarası seçilir.

[1] Şifrele veya [2] Şifreyi Çöz işlemlerinden biri seçilir.

Şifre girilir.

Program, orijinal dosyayı değiştirmez; yeni bir dosya üretir:

_sifreli.pdf

_cozulmus.pdf

📷 Örnek Çıktı
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
pdf-security-manager/
├── pdf_security_manager.py         # Ana uygulama
├── pdf_security_manager.ipynb      # Jupyter Notebook sürümü
├── requirements.txt                # Gerekli kütüphaneler
├── README.md                       # Proje dokümantasyonu
└── .gitignore                      # Gereksiz dosyaların engellenmesi
