from flask import Flask, render_template, request, jsonify
from joblib.parallel import method
from train import train
from character_predict import predict

app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def send_predict():
    payload = request.json
    path = payload.get('img')
    ans = predict(path)
    res = {'ans': int(ans)}
    return jsonify(res)

if __name__ == '__main__':
    train()
    app.run()