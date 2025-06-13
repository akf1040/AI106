# 🔬 Yıldız Sınıflandırma API

Bu proje, yıldızların özelliklerine göre sınıflandırılmasını yapan bir Flask API'sidir. Veri bilimi ve yapay zeka alanında temel makine öğrenmesi ve derin öğrenme tekniklerini uygulamak amacıyla hazırlanmıştır.

## 🎯 Proje Aşamaları

- 📥 Veri yükleme ve analiz
- 🧹 Veri temizleme ve ön işleme
- 🏷 Etiket kodlama ve özellik mühendisliği
- 🔎 Eğitim ve test setlerine ayırma
- 🤖 Model oluşturma ve eğitimi
- 📊 Model performans değerlendirmesi
  - Doğruluk (Accuracy)
  - Kesinlik (Precision)
  - Duyarlılık (Recall)
  - F1 Skoru
  - Kayıp (Loss)
  - Karışıklık Matrisi (Confusion Matrix)

## ⚙ Özellikler

- TensorFlow modeli kullanarak yıldız sınıflandırması
- RESTful API endpoint'i
- CORS desteği

## 🛠 Gereksinimler

- Python 3.x
- Flask
- TensorFlow
- NumPy
- scikit-learn (joblib için)
- Pandas
- Matplotlib & Seaborn

## 📦 Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install flask tensorflow numpy scikit-learn flask-cors pandas matplotlib seaborn
```

2. Model dosyalarını (`star_model.h5` ve `scaler.pkl`) projenin kök dizinine yerleştirin.

3. Uygulamayı çalıştırın:
```bash
python app.py
```

## 📡 API Kullanımı

POST isteği `/predict` endpoint'ine gönderilmelidir. İstek gövdesi şu formatta olmalıdır:

```json
{
    "alpha": float,
    "delta": float,
    "u": float,
    "g": float,
    "r": float,
    "i": float,
    "z": float,
    "redshift": float
}
```

## 📌 Not

Projelerimde kullanılan yöntemler, hem sınıflandırma hem de regresyon problemleri için uyarlanabilir. Model seçimleri, problem türüne ve veri setine göre farklılık gösterebilir.

## 📄 Lisans

MIT
