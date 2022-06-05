import streamlit as st

from core.base64_converter import encode, decode

col1, col2 = st.columns(2)

with col1:
    st.title("编码：")
    text_input = st.text_area(label="原始文本")
    option1 = st.selectbox(
        '编码',
        ('utf-8', 'gb18030'),
        key=1
    )
    st.write("编码结果:")
    st.code(encode(text_input, option1), language='bash')

with col2:
    st.title("解码：")
    text_input = st.text_area(label="编码文本")
    text_input = text_input.replace('\n', '')
    option2 = st.selectbox(
        '编码',
        ('utf-8', 'gb18030'),
        key=2
    )
    st.write("原始本文:")
    st.code(decode(text_input, option2), language='bash')
