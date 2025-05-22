import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io

# PDF 파일 경로
PDF_PATH = "Y62.pdf"

# 문제집 쪽수 → PDF 페이지 매핑 함수
def get_pdf_page(문제지쪽수):
    if 8 <= 문제지쪽수 < 17:
        return 2
    elif 17 <= 문제지쪽수 < 30:
        return 3
    elif 30 <= 문제지쪽수 < 41:
        return 4
    elif 42 <= 문제지쪽수 < 52:
        return 5
    elif 53 <= 문제지쪽수 < 59:
        return 6
    elif 62 <= 문제지쪽수 < 78:
        return 7
    elif 78 <= 문제지쪽수 <= 79:
        return 8
    else:
        return None

# 앱 시작
st.set_page_config(page_title="정답 자동 뷰어", layout="centered")
st.title("📘 문제집 정답 자동 보기")
st.caption("원하는 쪽수를 입력하면 해당 정답이 바로 보여집니다.")

# 사용자 입력
user_page = st.number_input("📄 문제집 쪽수를 입력하세요:", min_value=1, max_value=100, step=1)

# PDF 페이지 찾기
pdf_page = get_pdf_page(user_page)

if pdf_page:
    st.success(f"✅ PDF 파일의 {pdf_page}페이지를 보여드릴게요.")
    
    try:
        doc = fitz.open(PDF_PATH)
        page = doc.load_page(pdf_page - 1)
        pix = page.get_pixmap(dpi=150)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        st.image(img, caption=f"📄 PDF {pdf_page}페이지", use_column_width=True)
    except Exception as e:
        st.error(f"PDF를 여는 데 문제가 발생했어요: {e}")
else:
    st.warning("해당 쪽수의 정답 페이지가 없어요. 다시 확인해 주세요.")
