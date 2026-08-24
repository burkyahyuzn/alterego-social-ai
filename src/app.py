from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Kategoriler ve Başlangıç Durumları
categories = ["Science", "Technology", "Education", "Entertainment", "Sports"]

intent_vector = {"Science": 0.25, "Technology": 0.25, "Education": 0.30, "Entertainment": 0.10, "Sports": 0.10}
algorithmic_state = {"Science": 0.20, "Technology": 0.25, "Education": 0.25, "Entertainment": 0.20, "Sports": 0.10}

def calculate_iai(intent, state):
    diff_sum = sum(abs(intent[cat] - state[cat]) for cat in categories)
    return 100 * (1 - (0.5 * diff_sum))

@app.route('/')
def index():
    # Sayfa ilk yüklendiğinde mevcut skoru hesapla
    current_iai = calculate_iai(intent_vector, algorithmic_state)
    return render_template('index.html', current_iai=current_iai, state=algorithmic_state)

@app.route('/interact', methods=['POST'])
def interact():
    global algorithmic_state
    data = request.get_json()
    category = data.get('category')

    # Kullanıcı bir içeriğe tıkladığında çalışan basit algoritmik kayma (Drift)
    for cat in categories:
        if cat == category:
            algorithmic_state[cat] += 0.10  # Tıklananı artır
        else:
            algorithmic_state[cat] -= 0.025 # Diğerlerini azalt (Toplamı 1 tutmak için basitleştirilmiş mantık)
            
    # Değerlerin 0'ın altına düşmesini engelle
    for cat in categories:
        algorithmic_state[cat] = max(0, algorithmic_state[cat])

    new_iai = calculate_iai(intent_vector, algorithmic_state)
    
    return jsonify({'new_iai': round(new_iai, 2), 'new_state': algorithmic_state})

if __name__ == '__main__':
    app.run(debug=True)