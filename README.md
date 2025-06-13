# Yıldız Sınıflandırma API

Bu proje, yıldızların özelliklerine göre sınıflandırılmasını yapan bir Flask API'sidir.

## Özellikler

- TensorFlow modeli kullanarak yıldız sınıflandırması
- RESTful API endpoint'i
- CORS desteği

## Gereksinimler

- Python 3.x
- Flask
- TensorFlow
- NumPy
- scikit-learn (joblib için)

## Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install flask tensorflow numpy scikit-learn flask-cors
```

2. Model dosyalarını (`star_model.h5` ve `scaler.pkl`) projenin kök dizinine yerleştirin.

3. Uygulamayı çalıştırın:
```bash
python app.py
```

## API Kullanımı

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

## Lisans

MIT 