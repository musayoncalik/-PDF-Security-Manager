

import os
import getpass
from PyPDF2 import PdfReader, PdfWriter



def dosya_sec():
    """Klasördeki PDF dosyalarını listeler ve kullanıcıya seçtirir."""
    while True:
        # Sadece .pdf ile biten dosyaları bul
        dosyalar = [f for f in os.listdir() if f.lower().endswith('.pdf')]
        
        print("\n" + "="*40)
        print("📂 MEVCUT PDF DOSYALARI")
        print("="*40)

        if not dosyalar:
            print("❌ Bu klasörde hiç PDF dosyası yok!")
            print("  [0] ÇIKIŞ")
        else:
            for i, dosya in enumerate(dosyalar, 1):
                print(f"  [{i}] {dosya}")
            print("  [0] ÇIKIŞ")
        
        try:
            secim_input = input("\nDosya numarasını girin: ")
            
            # Boş enter'a basılırsa hata vermesin diye kontrol
            if not secim_input.strip():
                continue
                
            secim = int(secim_input)

            if secim == 0:
                return "CIKIS"
            
            if 1 <= secim <= len(dosyalar):
                return dosyalar[secim - 1]
            else:
                print("⚠️ Geçersiz numara, listedeki numaralardan birini girin.")
        except ValueError:
            print("⚠️ Lütfen sadece sayı girin.")

def pdf_kilitle(dosya_yolu):
    try:
        reader = PdfReader(dosya_yolu)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        print(f"\n🔒 '{dosya_yolu}' şifreleniyor...")
        sifre = getpass.getpass("Oluşturulacak şifreyi girin: ")
        
        if not sifre: # Şifre boş girilirse iptal et
            print("⚠️ İşlem iptal edildi (Şifre boş olamaz).")
            return

        writer.encrypt(sifre)
        yeni_dosya = dosya_yolu.replace(".pdf", "_sifreli.pdf")

        with open(yeni_dosya, "wb") as f:
            writer.write(f)
        
        print(f"✅ BAŞARILI! Yeni dosya: {yeni_dosya}")

    except Exception as e:
        print(f"❌ HATA: {e}")

def pdf_kilit_ac(dosya_yolu):
    try:
        reader = PdfReader(dosya_yolu)
        
        if reader.is_encrypted:
            print(f"\n🔑 '{dosya_yolu}' kilidi açılıyor...")
            sifre = getpass.getpass("Dosyanın şifresini girin: ")
            
            try:
                reader.decrypt(sifre)
                writer = PdfWriter()

                for page in reader.pages:
                    writer.add_page(page)

                yeni_dosya = dosya_yolu.replace(".pdf", "_cozulmus.pdf")

                with open(yeni_dosya, "wb") as f:
                    writer.write(f)
                
                print(f"✅ BAŞARILI! Şifre kaldırıldı: {yeni_dosya}")
            except:
                print("❌ HATA: Girdiğiniz şifre YANLIŞ!")
        else:
            print("⚠️ Bu dosya zaten şifreli değil.")

    except Exception as e:
        print(f"❌ HATA: {e}")

def baslat():
    print("\n******************************************")
    print("   🔒 AKILLI PDF GÜVENLİK MERKEZİ v2.0")
    print("******************************************")
    
    while True:
        # 1. Dosya seçimi (veya Çıkış)
        secilen_dosya = dosya_sec()
        
        if secilen_dosya == "CIKIS":
            print("\n👋 Programdan çıkılıyor. İyi günler!")
            break
        
        # Dosya seçildiyse işlem menüsüne gir
        print("-" * 40)
        print(f"SEÇİLEN: {secilen_dosya}")
        print("-" * 40)
        print("1. Şifrele (Kilitle)")
        print("2. Şifreyi Çöz (Kilidi Kaldır)")
        print("0. İptal / Ana Menüye Dön")
        
        islem = input("\nİşlem seçin (0-2): ")

        if islem == '1':
            pdf_kilitle(secilen_dosya)
        elif islem == '2':
            pdf_kilit_ac(secilen_dosya)
        elif islem == '0':
            print("Ana menüye dönülüyor...")
            continue
        else:
            print("⚠️ Geçersiz seçim.")
        
        # İşlem bitince kullanıcıya okuması için biraz zaman tanıyalım
        input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    try:
        baslat()
    except KeyboardInterrupt:
        # Ctrl+C ile zorla kapatılırsa temiz çıkış yap
        print("\n\n👋 Program kapatıldı.")