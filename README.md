<div align="center">
  <h1>🚀 ALTEREGO</h1>
  <h3>Gelecekteki Akışını Gösteren Yapay Zekâ Destekli Sosyal Medya Platformu</h3>
  <p><i>TEKNOFEST 2026 - NSosyal İnovasyon Yarışması Projesi</i></p>
</div>

---

## 📌 Problem Nedir?
Geleneksel sosyal medya algoritmaları yalnızca **anlık etkileşime** (tıklama, izleme süresi, beğeni) odaklanır. Bu durum, kullanıcıları zamanla kendi bilinçli hedeflerinden uzaklaştırarak "Algoritmik Kayma" (Algorithmic Drift) yaşamalarına, yankı odalarına hapsolmalarına ve dijital yorgunluk çekmelerine neden olur.

## 💡 ALTEREGO Yaklaşımı
ALTEREGO, bir içeriği yalnızca "kullanıcının beğenme ihtimaline" göre önermez. Arka planda bir **Kişisel Dijital İkiz** çalıştırarak, o içeriğin kullanıcının **gelecekteki algoritmik profiline** ve akışına nasıl etki edeceğini simüle eder.

Sistem kullanıcıyı 4 farklı katmanda nitelendirir:
1. 🧠 **Bilinçli Ben (Intended Me):** Kullanıcının platformda görmek istediğini belirttiği ideal içerik oranları.
2. 🖱️ **Davranışsal Ben (Behavioral Me):** Gerçek etkileşimlerden (beğeni/tıklama) doğan profil.
3. 🤖 **Algoritmik Ben (Algorithmic Me):** Platformun kullanıcıyı şu an nasıl modellediği.
4. 🔮 **Gelecekteki Ben (Future Me):** Mevcut etkileşimler devam ederse algoritmanın kullanıcıyı sürükleyeceği nokta.

## ⚙️ Çekirdek Metriklerimiz
Sistemimiz arka planda çalışan matematiksel bir öneri motoru barındırır:
* 🎯 **IAI (Intent Alignment Index - Niyet Uyum İndeksi):** Kullanıcının bilinçli hedefi ile mevcut algoritmik akışı arasındaki uyum (0-100).
* 🌊 **PFI (Predicted Feed Impact - Tahmini Akış Etkisi):** Tek bir içeriğin gelecekteki içerik dağılımını ne kadar değiştireceğinin vektörel tahmini.
* ⚖️ **PAC (Personal Alignment Cost - Kişisel Sapma Maliyeti):** Kullanıcının ana hedeflerinden sapmasının matematiksel maliyeti.
* ✨ **ARS (ALTEREGO Recommendation Score):** Etkileşim ihtimali ile sapma maliyetini (PAC) harmanlayan yeni nesil, dinamik öneri puanı.
* 🔭 **FAS (Future Alignment Score - Gelecek Uyum Skoru):** "30 Günlük Geleceğimi Gör" simülasyonu sonucunda ortaya çıkan, gelecekteki olası uyum puanı.

## 🛠️ Kurulum ve Çalıştırma (v0.4)
Prototipi kendi yerel ağınızda (LAN) test etmek için aşağıdaki adımları izleyebilirsiniz.

```bash
# 1. Repoyu bilgisayarınıza klonlayın
git clone [https://github.com/burkyahyuzn/alterego-social-ai.git](https://github.com/burkyahyuzn/alterego-social-ai.git)

# 2. Proje dizinine ve kaynak kod klasörüne girin
cd alterego-social-ai/src

# 3. Gerekli Flask kütüphanesini kurun
pip install flask

# 4. Sunucuyu başlatın
python app.py