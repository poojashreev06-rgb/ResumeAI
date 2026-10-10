import streamlit as st
import pymupdf
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="ResumeAI",
    page_icon="📄",
    layout="wide"
)

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

st.title("📄 ResumeAI")
st.subheader("AI-Powered Resume Screening System")
st.write(
    "Upload a resume and a job description to compare skills "
    "and measure semantic similarity."
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste the Job Description",
    height=200
)

skills = [
    "Python", "SQL", "Excel", "Machine Learning",
    "Data Analysis", "Power BI", "Tableau",
    "Statistics", "Data Visualization", "R"
]

if st.button("Analyze Resume"):
    if uploaded_file is None:
        st.error("Please upload a resume PDF.")
    elif not job_description.strip():
        st.error("Please enter a job description.")
    else:
        try:
            pdf_bytes = uploaded_file.getvalue()
            resume_text = ""

            with pymupdf.open(stream=pdf_bytes, filetype="pdf") as document:
                for page in document:
                    resume_text += page.get_text()

            if not resume_text.strip():
                st.error(
                    "No selectable text found. This PDF may need OCR."
                )
            else:
                resume_lower = resume_text.lower()
                job_lower = job_description.lower()

                required_skills = [
                    skill for skill in skills
                    if skill.lower() in job_lower
                ]

                matched_skills = [
                    skill for skill in required_skills
                    if skill.lower() in resume_lower
                ]

                missing_skills = [
                    skill for skill in required_skills
                    if skill.lower() not in resume_lower
                ]

                st.subheader("Analysis Results")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("### ✅ Matched Skills")
                    if matched_skills:
                        st.write(", ".join(matched_skills))
                    else:
                        st.write("No listed skills matched.")

                with col2:
                    st.markdown("### ❌ Missing Skills")
                    if missing_skills:
                        st.write(", ".join(missing_skills))
                    else:
                        st.write("No missing skills from our list.")

                if required_skills:
                    skill_percentage = (
                        len(matched_skills) / len(required_skills)
                    ) * 100
                    st.metric(
                        "Required Skill Keyword Match",
                        f"{skill_percentage:.2f}%"
                    )
                else:
                    st.info(
                        "No supported skills were detected in the job "
                        "description. The skill list may need expanding."
                    )

                resume_embedding = model.encode([resume_text])
                job_embedding = model.encode([job_description])

                similarity = cosine_similarity(
                    resume_embedding,
                    job_embedding
                )[0][0]

                st.metric(
                    "AI Semantic Similarity",
                    f"{similarity * 100:.2f}%"
                )

                st.caption(
                    "These scores measure keyword overlap and semantic "
                    "similarity. They are not hiring probabilities or "
                    "proof of candidate proficiency."
                )

                with st.expander("View Extracted Resume Text"):
                    st.text(resume_text)

        except Exception as error:
            st.error("Could not analyze this PDF.")
            st.exception(error)
