import streamlit as st

from PIL import Image

# from utils import makePrediction
from ultralytics import YOLO

# import cv2


# def makePrediction(image):
#     # Modèle (déjà entrainé)
#     model = YOLO("./best.pt")

#     # Prédiction
#     result = model(image)

#     # Get result image
#     result_array = result[0].plot()
#     # Fix BGR2RGB issue
#     result_rgb = cv2.cvtColor(result_array, cv2.COLOR_BGR2RGB)
#     # Save image to PIL format
#     result_image = Image.fromarray(result_rgb)

#     return result_image


st.title("Card detection")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

captured_image = st.camera_input("Take picture of card(s)")

if uploaded_file or captured_image:
    if uploaded_file:
        image = Image.open(uploaded_file)
    else:
        image = Image.open(captured_image)

    # result_image = makePrediction(image)

    st.image(
        # result_image,
        image,
        caption="result image with bounding boxes",
        use_column_width=True,
    )

    st.text("To retry click 'x Clear photo'")
