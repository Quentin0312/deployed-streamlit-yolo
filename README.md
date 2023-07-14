# Brief S6_yolo

## "Prototype de détection d'objet par ordinateur"

Détection et reconnaissance de cartes classiques sur image drag & drop ou photos via la webcam.

Compatible mobile.

### Install dependancies

```sh
python -m venv .venv
pip install -r requirements.txt
```

### Docker usage

```sh
docker build -t poker-cards .
```

```sh
docker run -p 8501:8501 poker-cards
```

## Technos

- Streamlit
- Yolov8
