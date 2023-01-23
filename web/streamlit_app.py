import streamlit as st
from simple_tfidf_japanese.tfidf import TFIDF

def render() -> None:
    st.title('サイト内の重要ワード(3つ)探索')

    url = st.text_input(label='参照するサイトのURL: ', value='')
    

    words_count = 3
    if st.button('参照開始'):
        try:
            tfidf = TFIDF.gen_web(url)

            st.write('重要ワードは降順で以下の通りです。')
            cnt = 0
            for key, value in tfidf:
                if cnt < words_count:
                    cnt += 1
                    st.write(str(cnt) + '. ' + key)
                else:
                    cnt = 0
                    break
                # print(key, value)
        except:
            st.write('ご指定のURLのサイトを参照できません。')

if __name__ == "__main__":
    render()
