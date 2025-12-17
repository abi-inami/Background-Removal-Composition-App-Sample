import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("背景切り抜き＆合成アプリ")

# 2つのカラムでファイルアップローダーを配置
col1, col2 = st.columns(2)

with col1:
    st.subheader("切り抜き対象の画像")
    uploaded_file = st.file_uploader(
        "切り抜きたい画像をアップロード",
        type=["png", "jpg", "jpeg"],
        key="main"
    )

with col2:
    st.subheader("背景画像")
    background_file = st.file_uploader(
        "背景画像をアップロード（オプション）",
        type=["png", "jpg", "jpeg"],
        key="background"
    )

# 画像プレビュー表示
if uploaded_file or background_file:
    col_preview1, col_preview2 = st.columns(2)
    
    with col_preview1:
        if uploaded_file:
            st.subheader("元画像")
            input_image = Image.open(uploaded_file)
            st.image(input_image, use_container_width=True)
    
    with col_preview2:
        if background_file:
            st.subheader("背景画像")
            background_preview = Image.open(background_file)
            st.image(background_preview, use_container_width=True)

if uploaded_file:
    input_image = Image.open(uploaded_file)

    if st.button("背景を切り抜く"):
        with st.spinner("処理中..."):
            # 背景を削除
            output_image = remove(input_image)

        col_result1, col_result2 = st.columns(2)
        
        with col_result1:
            st.subheader("切り抜き結果")
            st.image(output_image, use_container_width=True)

            # 切り抜き結果のダウンロード
            buf1 = io.BytesIO()
            output_image.save(buf1, format="PNG")
            st.download_button(
                "切り抜き画像をダウンロード",
                data=buf1.getvalue(),
                file_name="removed_bg.png",
                mime="image/png"
            )

        # 背景画像がアップロードされている場合は合成
        if background_file:
            with col_result2:
                st.subheader("背景と合成結果")
                
                background_image = Image.open(background_file).convert("RGB")
                
                # 切り抜き画像のサイズを背景画像に合わせる
                output_resized = output_image.resize(background_image.size, Image.Resampling.LANCZOS)
                
                # 背景画像に切り抜き画像を合成
                background_image.paste(output_resized, (0, 0), output_resized)
                
                st.image(background_image, use_container_width=True)
                
                # 合成画像のダウンロード
                buf2 = io.BytesIO()
                background_image.save(buf2, format="PNG")
                st.download_button(
                    "合成画像をダウンロード",
                    data=buf2.getvalue(),
                    file_name="composite.png",
                    mime="image/png"
                )

        