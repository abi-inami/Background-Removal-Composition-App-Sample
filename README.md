# Background-Removal-Composition-App-Sample-
Streamlit + Rembg + Pillow で作成した画像の背景切り抜き＆合成アプリのサンプルです

# 環境構築

手順例
```bash
# Python 3.12で新しい仮想環境を作成
py -3.12 -m venv venv

# 仮想環境を有効化
venv\Scripts\activate

# 必要パッケージをインストール
pip install streamlit rembg pillow 
pip install onnxruntime
```

# 背景切り抜き＆合成アプリ
## 起動方法

```
streamlit run app.py
```
起動後、`http://localhost:8501` に画面が表示されます。

## 使い方
* 背景を切り抜きたい画像(人物・ペットなど)
* 合成したい画像(背景・フレームなど)

をそれぞれアップロードして実行ボタンを押下
