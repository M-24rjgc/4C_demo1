from flask import Flask, render_template
from datetime import datetime
import random
import os
import json
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('index.html', 
                         update_time=datetime.now().strftime('%H:%M:%S'),
                         cadence=180,
                         stride=1.2,
                         posture_score=92)

@app.route('/api/sample_data')
def get_sample_data():
    data_path = os.path.join(os.path.dirname(__file__), 'sample_data.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        return jsonify(json.load(f))

@app.route('/realtime-data')
def realtime_data():
    # 模拟实时传感器数据（后续替换为真实数据源）
    return {
        'timestamp': datetime.now().isoformat(),
        'acceleration_x': random.uniform(-2, 2),
        'pressure': random.uniform(0, 100),
        'gait_phase': random.choice(['stance', 'swing']),
        'error_type': random.choice(['overstride', 'cross_over', 'heel_strike']),
        'fatigue_index': round(random.uniform(0, 1), 2)
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)