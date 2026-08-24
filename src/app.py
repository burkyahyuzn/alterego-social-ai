from flask import Flask, render_template, request, jsonify
import uuid

app = Flask(__name__)

# Kategoriler ve Kullanıcının Başlangıç Hedefi (Bilinçli Niyeti)
categories = ["Science", "Technology", "Education", "Entertainment", "Sports"]
intent_vector = {"Science": 0.25, "Technology": 0.25, "Education": 0.30, "Entertainment": 0.10, "Sports": 0.10}

# Aynı ağdan giren kullanıcıların (Yusuf Kaan, Alp vb.) durumlarını ayrı ayrı tutmak için sözlük
user_states = {}

def calculate_iai(intent, state):
    diff_sum = sum(abs(intent[cat] - state[cat]) for cat in categories)
    return max(0, 100 * (1 - (0.5 * diff_sum)))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/init_user', methods=['GET'])
def init_user():
    # Sayfaya her girene yeni bir kimlik ver
    user_id = str(uuid.uuid4())
    user_states[user_id] = {"Science": 0.25, "Technology": 0.25, "Education": 0.30, "Entertainment": 0.10, "Sports": 0.10}
    iai = calculate_iai(intent_vector, user_states[user_id])
    return jsonify({'user_id': user_id, 'iai': iai, 'state': user_states[user_id]})

@app.route('/interact', methods=['POST'])
def interact():
    data = request.get_json()
    user_id = data.get('user_id')
    category = data.get('category')

    if user_id not in user_states:
        return jsonify({'error': 'Kullanici bulunamadi'}), 400

    state = user_states[user_id]

    # Algoritmik Kayma (Drift) Simülasyonu
    for cat in categories:
        if cat == category:
            state[cat] += 0.10  # Tıklanan kategoriyi sert artır
        else:
            state[cat] -= 0.025 # Diğerlerini azalt
        state[cat] = max(0.0, state[cat]) # Eksiye düşmeyi engelle

    # Oranları tekrar %100'e (1.0) tamamla
    total = sum(state.values())
    if total > 0:
        for cat in categories:
            state[cat] /= total

    new_iai = calculate_iai(intent_vector, state)
    return jsonify({'new_iai': round(new_iai, 2), 'new_state': state})

if __name__ == '__main__':
    # host='0.0.0.0' sayesinde LAN (Yerel Ağ) üzerindeki telefonlar/PC'ler bağlanabilir
    app.run(host='0.0.0.0', port=5000, debug=True)