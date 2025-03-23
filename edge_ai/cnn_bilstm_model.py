import tensorflow as tf
from tensorflow.keras import layers

class RunningAnalyzer:
    def build_model(self, input_shape):
        """
        构建CNN-BiLSTM混合模型
        输入形状：(time_steps, 9) 9轴IMU数据
        """
        model = tf.keras.Sequential([
            layers.Input(shape=input_shape),
            layers.Conv1D(16, 3, activation='relu'),
            layers.MaxPooling1D(2),
            layers.Bidirectional(layers.LSTM(32, return_sequences=True)),
            layers.Bidirectional(layers.LSTM(16)),
            layers.Dense(64, activation='relu'),
            layers.Dense(3, activation='linear')  # 输出：步频、步幅、姿态评分
        ])
        return model

    def convert_to_tflite(self, model):
        """将Keras模型转换为TensorFlow Lite格式"""
        converter = tf.lite.TFLiteConverter.from_keras_model(model)
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        tflite_model = converter.convert()
        return tflite_model