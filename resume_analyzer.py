from pyexpat import model
from socket import timeout
import streamlit as st
import PyPDF2
from langchain_ollama import OllamaLLM

st.set_page_config(page_title="Resume Analyzer", page_icon="📄")
st.title("📄ResumeSense")
st.write("Upload your resume to analyze it!")
uploaded_resume=st.file_uploader("Upload your resume", type="pdf")


if uploaded_resume:
    st.write("Resume uploaded successfully!")
    pdf_reader=PyPDF2.PdfReader(uploaded_resume)
    resume_text=" ".join(page.extract_text() for page in pdf_reader.pages)
    st.text_area("Resume Text Preview",resume_text,height=300)

    llm = OllamaLLM(model="deepseek-coder", temperature=0.2, timeout=60)
    if st.button("Analyze Resume"):
        with st.spinner("Analyzing..."):
            prompt=prompt = f"""
You are an expert resume evaluator. Analyze the following resume text and provide a structured assessment.also Provide a final score at last out of 5 and tips to improve further

### Resume Text:
{resume_text}

### Instructions:
1. Identify key details (Name, Profession).
2. Extract work experience (Roles, Companies, Achievements).
3. Identify skills (Technical & Soft).
4. Highlight education details (Degree, University).
5. Assess strengths and areas for improvement.
6. Provide suggestions to enhance resume quality.

Ensure the response follows this structured format:
- **Candidate Overview:** [...]
- **Strengths:** [...]
- **Areas for Improvement:** [...]
- **Final Assessment:** [...]

Be precise,short,crisp and avoid unnecessary information.
"""
            response=llm.invoke(prompt) 
            st.write("Analysis result: ")
            st.write(response)





# import streamlit as st
# import PyPDF2
# import re
# from langchain_ollama import OllamaLLM

# st.set_page_config(page_title="Resume Analyzer", page_icon="📄")
# st.title("📄 Resume Analyzer")
# st.write("Upload your resume to analyze it!")

# uploaded_resume = st.file_uploader("Upload your resume", type="pdf")

# if uploaded_resume:
#     st.write("✅ Resume uploaded successfully!")

#     # Extract text from PDF
#     pdf_reader = PyPDF2.PdfReader(uploaded_resume)
#     resume_text = " ".join(page.extract_text() or "" for page in pdf_reader.pages)

#     # Display preview of extracted text
#     st.text_area("📜 Resume Text Preview", resume_text, height=300)

#     llm = OllamaLLM(model="deepseek-coder", temperature=0.2, timeout=60)

#     if st.button("🔍 Analyze Resume"):
#         with st.spinner("Analyzing... ⏳"):
#             prompt = f"""
# You are an expert resume evaluator. Analyze the following resume text and provide a structured assessment.
# Also, provide a final score out of 5 and improvement tips.

# ### Resume Text:
# {resume_text}

# ### Instructions:
# - Use the exact section titles below in your response to maintain structure.
# - Each section should be clearly separated for easy parsing.

# **Candidate Overview:** [...]
# **Work Experience:** [...]
# **Skills:** [...]
# **Education Details:** [...]
# **Strengths:** [...]
# **Areas for Improvement:** [...]
# **Final Assessment:** Final Score: X/5 Suggestions: [...]
# """
#             response = llm.invoke(prompt)

#             # Extracting sections using regex
#             def extract_section(title, text):
#                 match = re.search(rf"\*\*{title}:\*\*\s*(.+?)(?=\*\*|$)", text, re.DOTALL)
#                 return match.group(1).strip() if match else "Not available"

#             analysis_dict = {
#                 "📌 Candidate Overview": extract_section("Candidate Overview", response),
#                 "💼 Work Experience": extract_section("Work Experience", response),
#                 "🛠 Skills": extract_section("Skills", response),
#                 "🎓 Education Details": extract_section("Education Details", response),
#                 "✅ Strengths": extract_section("Strengths", response),
#                 "⚠️ Areas for Improvement": extract_section("Areas for Improvement", response),
#                 "📊 Final Assessment": extract_section("Final Assessment", response),
#             }

#             st.subheader("📊 Resume Analysis Result")

#             # Display each section separately
#             for title, content in analysis_dict.items():
#                 with st.expander(title):
#                     st.write(content)
