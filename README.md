# 中长跑实时指导系统使用说明书

## 1. 系统要求
- Python 3.8+
- TensorFlow Lite 2.16.1
- Flask 3.0.2

## 2. 安装步骤
```bash
# 激活虚拟环境
powershell -Command "cd c:\Users\52376\Desktop\4; .\venv\Scripts\Activate"

# 安装依赖
pip install -r requirements.txt
```

## 3. 启动Web界面
```bash
powershell -Command "cd c:\Users\52376\Desktop\4; .\venv\Scripts\Activate; python .\web_ui\app.py"
```

## 4. 核心功能说明
- 实时传感器数据显示：访问 http://localhost:5000
- 步态分析接口：POST /api/analyze
- 历史数据查询：GET /api/history

## 5. 硬件连接配置
1. 通过蓝牙5.0连接BMI270 IMU传感器
2. 确保足压传感器采样率设置为200Hz
3. 使用USB-C接口进行设备充电

## 6. 常见问题
Q: 如何更新AI模型？
A: 将新生成的.tflite模型文件替换edge_ai/models目录下的现有文件