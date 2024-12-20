from streamlit_lottie import st_lottie
import json

# JSONファイルを読み込む関数
def load_lottie(file_path):
        with open(file_path, "r") as f:
                return json.load(f)

# ローカルにあるJSONファイルのパスを指定
file_path = "AdventCalendar2024.json"

# ローカルにあるJSONファイルを読み込む
animation = load_lottie(file_path)

st_lottie(animation, width = 600, height = 400)