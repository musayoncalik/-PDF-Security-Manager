 PDF Security Manager v2.0

PDF Security Manager, Python kullanılarak geliştirilmiş, PDF dosyalarını hızlı ve güvenli bir şekilde şifrelemek (encrypt) ve 
şifrelerini çözmek (decrypt) için tasarlanmış gelişmiş bir komut satırı (CLI) aracıdır.

Bu proje; dosya işleme, kullanıcı etkileşimi, hata yönetimi ve harici kütüphane kullanımı konularında pratik bir örnek teşkil eder.


🚀 Özellikler

📂 Akıllı Dosya Algılama: Program, çalıştığı dizindeki .pdf dosyalarını otomatik olarak tarar ve listeler. Dosya ismini elle yazmanıza gerek kalmaz.

🔒 AES Şifreleme: PDF dosyalarınızı güçlü bir şifreleme standardı ile koruma altına alır.

🔓 Şifre Çözme: Şifresi bilinen kilitli dosyaların korumasını kaldırır.

👀 Güvenli Giriş: Şifre girişleri sırasında karakterler ekranda gizlenir (getpass modülü ile), böylece yanınızdaki kişi şifrenizi göremez.

🔄 Döngüsel Menü: İşlem bittikten sonra program kapanmaz, ana menüye döner. Çoklu işlem yapmak için idealdir.

🎨 Kullanıcı Dostu Arayüz: Emojiler ve temiz menü tasarımı ile kolay kullanım sağlar.



🛠 Kurulum

Bu projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin.

1. Gereksinimler

Python 3.x

PyPDF2 kütüphanesi

2. Projeyi İndirme

git clone [https://github.com/musayoncalik/-PDF-Security-Manager.git](https://github.com/musayoncalik/-PDF-Security-Manager.git)
cd -PDF-Security-Manager


3. Kütüphaneyi Yükleme

pip install PyPDF2


(Alternatif olarak pip install -r requirements.txt komutunu kullanabilirsiniz.)

💻 Kullanım

Terminal veya komut satırında proje klasörüne gidin ve programı başlatın:

python pdf_security_manager.py


Adım Adım İşleyiş:

Program açıldığında klasördeki PDF dosyaları numaralandırılmış bir liste olarak gelir.

İşlem yapmak istediğiniz dosyanın numarasını girin.

[1] Şifrele veya [2] Şifreyi Çöz seçeneğini seçin.

Şifrenizi belirleyin (veya girin).

Program, orijinal dosyayı bozmadan _sifreli.pdf veya _cozulmus.pdf uzantılı yeni bir dosya oluşturur.

📷 Ekran Görüntüsü (Örnek)

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
├── pdf_security_manager.py   # Ana uygulama kodu
├── pdf_security_manager.ipynb   # Ana uygulama jupiter notebook kodu
├── requirements.txt          # Gerekli kütüphaneler (PyPDF2)
├── README.md                 # Proje dokümantasyonu
└── .gitignore                # Gereksiz dosyaların yüklenmesini engeller
