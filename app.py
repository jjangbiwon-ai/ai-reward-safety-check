
import streamlit as st

st.set_page_config(
    page_title="AI 리워드 광고 안심체크",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ AI 리워드 광고 안심체크")
st.write("리워드 광고 속 보상과 출금 조건을 확인해 보세요.")

st.info(
    "광고 또는 리워드 앱 화면을 캡처해서 올려주세요."
)

uploaded_file = st.file_uploader(
    "📷 광고·앱 화면 이미지 업로드",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="업로드한 이미지")

    if st.button("🤖 AI 분석하기", type="primary"):
        st.warning(
            "AI 분석 기능은 다음 단계에서 연결할 예정입니다."
        )
else:
    st.write("분석할 이미지 1장을 선택해 주세요.")

st.divider()
st.caption(
    "본 서비스는 참고용 정보를 제공하며, "
    "실제 리워드 지급이나 출금 가능 여부를 보증하지 않습니다."
)
