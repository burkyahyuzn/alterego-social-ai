from flask import Flask, render_template, request, jsonify
import uuid
import random

app = Flask(__name__)

categories = ["Science", "Technology", "Education", "Entertainment", "Sports"]
intent_vector = {"Science": 0.25, "Technology": 0.25, "Education": 0.30, "Entertainment": 0.10, "Sports": 0.10}
user_states = {}

# Sahte İçerik Havuzu (Veritabanı Simülasyonu)
content_db = [
    {"id": 1, "cat": "Science", "title": "CERN'de yeni bir parçacık keşfi ihtimali!", "img": "https://picsum.photos/400/250?random=1", "engagement_score": 0.8},
    {"id": 2, "cat": "Technology", "title": "Yapay Zeka modelleri artık kendi kodlarını yazıyor.", "img": "https://picsum.photos/400/250?random=2", "engagement_score": 0.9},
    {"id": 3, "cat": "Education", "title": "Python ile Algoritma Geliştirme Eğitimi", "img": "https://picsum.photos/400/250?random=3", "engagement_score": 0.7},
    {"id": 4, "cat": "Entertainment", "title": "İnternetin en komik kedi videoları derlemesi 😹", "img": "https://picsum.photos/400/250?random=4", "engagement_score": 0.95},
    {"id": 5, "cat": "Sports", "title": "Şampiyonlar Ligi'nde inanılmaz geri dönüş!", "img": "https://picsum.photos/400/250?random=5", "engagement_score": 0.85},
    {"id": 6, "cat": "Entertainment", "title": "Ünlülerin şok eden makyajsız halleri!", "img": "https://picsum.photos/400/250?random=6", "engagement_score": 0.99},
    {"id": 7, "cat": "Science", "title": "James Webb Teleskobu'ndan yeni galaksi fotoğrafları", "img": "https://picsum.photos/400/250?random=7", "engagement_score": 0.75}
]

def calculate_iai(intent, state):
    diff_sum = sum(abs(intent[cat] - state[cat]) for cat in categories)
    return max(0, 100 * (1 - (0.5 * diff_sum)))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/init_user', methods=['GET'])
def init_user():
    user_id = str(uuid.uuid4())
    user_states[user_id] = {"Science": 0.25, "Technology": 0.25, "Education": 0.30, "Entertainment": 0.10, "Sports": 0.10}
    iai = calculate_iai(intent_vector, user_states[user_id])
    return jsonify({'user_id': user_id, 'iai': iai, 'state': user_states[user_id]})

@app.route('/get_feed', methods=['POST'])
def get_feed():
    data = request.get_json()
    user_id = data.get('user_id')
    if user_id not in user_states:
        return jsonify({'error': 'Kullanıcı bulunamadı'}), 400

    current_state = user_states[user_id]
    current_iai = calculate_iai(intent_vector, current_state)
    
    scored_feed = []
    for post in content_db:
        # PFI (Predicted Feed Impact) Simülasyonu
        simulated_state = current_state.copy()
        simulated_state[post['cat']] += 0.10
        total = sum(simulated_state.values())
        for c in categories: simulated_state[c] /= total
        
        future_iai = calculate_iai(intent_vector, simulated_state)
        
        # PAC (Personal Alignment Cost) = Eski IAI - Yeni IAI
        pac = max(0, current_iai - future_iai) / 100 
        
        # ARS (Alterego Recommendation Score) Formülü: İlgi - Sapma Maliyeti
        ars = post['engagement_score'] - (1.5 * pac) 
        
        scored_feed.append({
            "post": post,
            "ars": round(ars, 2),
            "pac": round(pac, 2),
            "impact": "Negatif" if pac > 0.05 else "Pozitif/Nötr"
        })
        
    # Akışı ARS puanına göre en yüksekten en düşüğe sırala
    scored_feed.sort(key=lambda x: x['ars'], reverse=True)
    return jsonify({'feed': scored_feed})

@app.route('/interact', methods=['POST'])
def interact():
    data = request.get_json()
    user_id = data.get('user_id')
    category = data.get('category')

    state = user_states[user_id]
    for cat in categories:
        if cat == category:
            state[cat] += 0.15 
        else:
            state[cat] -= 0.03 
        state[cat] = max(0.01, state[cat]) 

    total = sum(state.values())
    for cat in categories: state[cat] /= total

    new_iai = calculate_iai(intent_vector, state)
    return jsonify({'new_iai': round(new_iai, 2), 'new_state': state})

@app.route('/simulate_future', methods=['POST'])
def simulate_future():
    # Gelecek Simülasyonu (FAS - Future Alignment Score)
    data = request.get_json()
    user_id = data.get('user_id')
    state = user_states[user_id].copy()
    
    # 30 etkileşim boyunca rastgele ama ağırlıklı simülasyon
    for _ in range(30):
        # Mevcut durumda ne yüksekse ona tıklama ihtimali daha yüksek simüle edilir
        chosen_cat = random.choices(categories, weights=list(state.values()))[0]
        state[chosen_cat] += 0.10
        for c in categories:
            if c != chosen_cat: state[c] -= 0.02
            state[c] = max(0.01, state[c])
        total = sum(state.values())
        for c in categories: state[c] /= total
        
    fas = calculate_iai(intent_vector, state)
    return jsonify({'fas': round(fas, 2), 'future_state': state})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)