# --- Extracting text from PDF
from pathlib import Path
import pypdf
from io import StringIO
import streamlit as st

st.set_page_config(page_title="Converting PDF → TXT", layout="centered")

st.title("📄 PDF to Text Converter")
st.markdown("""
            ---
This app converts a PDF file into a plain text (.txt) file.
It was created to simplify the work of professionals (healthcare or otherwise) who need to extract raw text from PDF files.

** 🛠️ Made by Rodrigo Higashi **
[GitHub](https://github.com/rodrigohigashi) | [LinkedIn](https://www.linkedin.com/in/rodrigohigashi/)
            ---
""")

# Upload PDF File
file_pdf = st.file_uploader("Add PDF upload here", type=["pdf"])

if file_pdf is not None:
    reader_pdf = pypdf.PdfReader(file_pdf)
    
    full_text = ""
    for i, page in enumerate(reader_pdf.pages, 1):
        text_page = page.extract_text()
        full_text += f"\n\n--- Page {i} ---\n\n{text_page or ''}"

    st.subheader("📄 Text extracted:")
    st.text_area("PDF content extracted", full_text, height=300)

    # Generate TXT file for download
    content_txt = StringIO(full_text)
    st.download_button(
        label="📥 Download as .txt",
        data=content_txt.getvalue(),
        file_name="text_extracted.txt",
        mime="text/plain"
    )

    


    