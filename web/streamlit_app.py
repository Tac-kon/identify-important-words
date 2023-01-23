import streamlit as st
from simple_tfidf_japanese.tfidf import TFIDF

WORDS_COUNT = 3

def render() -> None:
    st.title('サイト内の主要ワード (' + str(WORDS_COUNT) +'選) 調査')

    url = st.text_input(label='サイトのURL: ', value='')
    
    if st.button('調査'):
        try:
            tfidf = TFIDF.gen_web(url)

            st.subheader('主要なワードは以下の通りです。')
            cnt = 0
            for key, value in tfidf:
                if cnt < WORDS_COUNT:
                    cnt += 1
                    st.write(str(cnt) + '. ' + key)
                else:
                    cnt = 0
                    break
        except:
            st.write('URL先のサイトを参照できません。')

if __name__ == "__main__":
    render()
