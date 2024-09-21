from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5173", "http://localhost:5173"]}})

socketio = SocketIO(app, cors_allowed_origins=["http://127.0.0.1:5173", "http://localhost:5173"])

# Stock trading routes
@app.route('/buy', methods=['POST'])
def buy_stock():
    data = request.json
    return jsonify({"message": "Stock bought successfully"})

@app.route('/sell', methods=['POST'])
def sell_stock():
    data = request.json
    return jsonify({"message": "Stock sold successfully"})

@app.route('/portfolio/<int:user_id>', methods=['GET'])
def get_portfolio(user_id):
    return jsonify({"portfolio": []})

# WebSocket connection handler
@socketio.on('connect')
def handle_connection():
    emit('message', {'data': 'Connected to stock market simulator!'})

# Simulate and emit stock price updates
def update_stock_prices():
    while True:
        price_changes = {symbol: round(random.uniform(-1, 1), 2) for symbol in ['AAPL', 'GOOGL', 'AMZN']}
        socketio.emit('stock_update', price_changes)
        socketio.sleep(5)

# Start background task for stock price updates
socketio.start_background_task(update_stock_prices)

@app.after_request
def apply_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:5173'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    return response

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000)
