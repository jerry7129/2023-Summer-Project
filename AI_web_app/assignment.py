from api.AI import AIAPI
import streamlit as st
from PIL import Image

@st.cache_resource
def get_api():
    return AIAPI(font="resources/malgun.ttf")


def main():
    col1, col2 = st.columns([1,1])
    
    with col1 :

        api = get_api()

        st.title("책 읽어주는 인공지능")
        st.header("컴퓨터소프트웨어학부 22학번 김승관")

        # Image2Text API 활용
        query = st.file_uploader('책 이미지 입력')
        if query is not None:
            st.image(query)
    

    with col2 :
        if query is not None:
            response = api.query_image2text(query, key='image2text')
            st.header("OCR 결과")
            st.text(response)
            title, summery = api.query_text2text(response)
            st.header("요약 결과")
            st.subheader(title)
            st.markdown(summery)


if __name__ == '__main__':
    main()




