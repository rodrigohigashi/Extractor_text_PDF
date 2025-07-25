# --- Extraindo texto de PDF
from pathlib import Path
import pypdf
from io import StringIO
import streamlit as st

st.set_page_config(page_title="Conversor PDF → TXT", layout="centered")

st.title("📄 Conversão de PDF para TXT")
st.write("Este aplicativo recebe um arquivo PDF, extrai o texto e gera um arquivo .txt.")
st.markdown("---")
st.markdown("🛠️ **Desenvolvido por Rodrigo Higashi**  \n📬 _Contato:_ rockigo@email.com  \n🔗 [Meu LinkedIn](https://www.linkedin.com/in/rodrigohigashi/)")
st.markdown("---")

# Upload do arquivo PDF
arquivo_pdf = st.file_uploader("Faça upload do PDF", type=["pdf"])

if arquivo_pdf is not None:
    leitor_pdf = pypdf.PdfReader(arquivo_pdf)
    
    texto_completo = ""
    for i, pagina in enumerate(leitor_pdf.pages, 1):
        texto_pagina = pagina.extract_text()
        texto_completo += f"\n\n--- Página {i} ---\n\n{texto_pagina or ''}"

    st.subheader("📄 Texto extraído:")
    st.text_area("Conteúdo do PDF extraído", texto_completo, height=300)

    # Geração do arquivo TXT para download
    conteudo_txt = StringIO(texto_completo)
    st.download_button(
        label="📥 Baixar como .txt",
        data=conteudo_txt.getvalue(),
        file_name="texto_extraido.txt",
        mime="text/plain"
    )

    


    