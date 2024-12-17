from streamlit_lottie import st_lottie
import json

# lottieJSONファイルを読み込む関数
def load_lottie(file_path):
        with open(file_path, "r") as f:
                return json.load(f)

# ローカルにあるlottieJSONファイルのパスを指定
santa_file_path = "presentbox_open.json"

# ローカルにあるlottieファイルを読み込む
santa_animation = load_lottie(santa_file_path)

st_lottie(santa_animation, speed = 1, width = 600, height = 400)