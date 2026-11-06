
import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="AI 리워드 광고 안심체크",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ AI 리워드 광고 안심체크")
st.write("리워드 광고 속 보상과 출금 조건을 확인해 보세요.")

st.info("광고 또는 리워드 앱 화면을 캡처해서 올려주세요.")

uploaded_file = st.file_uploader(
    "📷 광고·앱 화면 이미지 업로드",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    st.image(
        uploaded_file,
        caption="업로드한 이미지",
        width=350
    )

    if st.button("🤖 AI 분석하기", type="primary"):
        try:
            api_key = st.secrets["GEMINI_API_KEY"]
            client = genai.Client(api_key=api_key)

            image_bytes = uploaded_file.getvalue()

            if uploaded_file.type == "image/png":
                mime_type = "image/png"
            else:
                mime_type = "image/jpeg"

            prompt = """
당신은 리워드 광고의 보상 및 출금 조건을
분석하는 소비자 정보 안내 도우미입니다.

첨부된 이미지에서 확인할 수 있는 내용만
근거로 다음 항목을 한국어로 분석하세요.

1. 화면에 표시된 보상금액
2. 출금 가능 여부에 대한 안내
3. 추가 광고 시청, 레벨, 미션 등의 조건
4. 소비자가 주의해서 확인해야 할 사항
5. 이미지에서 확인할 수 없는 정보

중요 규칙:
- 화면에 표시된 금액을 실제 현금으로 단정하지 마세요.
- 특정 앱을 사기라고 단정하지 마세요.
- 이미지에 없는 내용을 만들어내지 마세요.
- 확인할 수 없는 사항은 '확인 불가'라고 표시하세요.
- 이해하기 쉬운 한국어로 설명하세요.
- 마지막에 간단한 종합 안내를 작성하세요.
"""

            with st.spinner("Gemini AI가 이미지를 분석하고 있습니다..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[
                        prompt,
                        types.Part.from_bytes(
                            data=image_bytes,
                            mime_type=mime_type
                        )
                    ]
                )

            st.subheader("🔍 AI 분석 결과")

            if response.text:
                st.markdown(response.text)
            else:
                st.warning("분석 결과가 비어 있습니다. 다시 시도해 주세요.")

        except KeyError:
            st.error(
                "Gemini API 키를 찾을 수 없습니다. "
                "Streamlit Secrets 설정을 확인해 주세요."
            )
        except Exception:
            st.error(
                "AI 분석을 완료하지 못했습니다. "
                "API 키, 무료 사용 한도 또는 모델 사용 가능 여부를 "
                "확인해 주세요."
            )

else:
    st.write("분석할 이미지 1장을 선택해 주세요.")

st.divider()
st.caption(
    "본 서비스는 참고용 정보를 제공하며, "
    "실제 리워드 지급이나 출금 가능 여부를 보증하지 않습니다."
)
