# ALTEREGO v0.1 - Çekirdek Algoritma Simülasyonu

categories = ["Science", "Technology", "Education", "Entertainment", "Sports"]

# 1. Intent Vector (Kullanıcının feed'inde görmek istediği ideal oranlar)
intent_vector = {
    "Science": 0.25, 
    "Technology": 0.25, 
    "Education": 0.30, 
    "Entertainment": 0.10, 
    "Sports": 0.10
}

# 2. Algorithmic State (Klasik algoritmanın kullanıcının tıklamalarına göre oluşturduğu mevcut durum)
algorithmic_state = {
    "Science": 0.20, 
    "Technology": 0.25, 
    "Education": 0.25, 
    "Entertainment": 0.20, 
    "Sports": 0.10
}

def calculate_iai(intent, state):
    """Intent Alignment Index (IAI) hesaplar: 0 ile 100 arası."""
    diff_sum = sum(abs(intent[cat] - state[cat]) for cat in categories)
    return 100 * (1 - (0.5 * diff_sum))

if __name__ == "__main__":
    print("--- ALTEREGO v0.1 Çekirdek Simülasyonu Başlıyor ---\n")
    
    iai_score = calculate_iai(intent_vector, algorithmic_state)
    print(f"[BAŞLANGIÇ] Kullanıcının İdeali ile Algoritma Uyumu (IAI): {iai_score:.2f} / 100")

    # 3. İçerik Etkileşimi Simülasyonu (Kullanıcı peş peşe 3 Eğlence videosuna tıklar/izlerse)
    print("\n[!] Kullanıcı 3 adet 'Entertainment' (Eğlence) videosu izledi...")
    
    # Klasik algoritma hemen eğlence oranını artırır (Algorithmic Drift)
    algorithmic_state["Entertainment"] += 0.15
    algorithmic_state["Education"] -= 0.05
    algorithmic_state["Science"] -= 0.05
    algorithmic_state["Technology"] -= 0.05

    yeni_iai = calculate_iai(intent_vector, algorithmic_state)
    print(f"\n[YENİ DURUM] Güncel Uyum Skoru (IAI): {yeni_iai:.2f} / 100")
    
    pac_score = iai_score - yeni_iai
    print(f"-> Sapma Maliyeti (PAC - Personal Alignment Cost): {pac_score:.2f} Puan")

    print("\n[SONUÇ]")
    print("Normal algoritma etkileşim arttı diye eğlence önermeye devam eder.")
    print("ALTEREGO ise IAI'deki bu düşüşü fark eder ve akışı kullanıcının ilk hedefine doğru düzeltir!")