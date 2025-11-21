import streamlit as st
import google.generativeai as genai

# --- Configure Gemini ---
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# --- App Title ---
st.title("🎓 AI Career Counselling App")
st.markdown("**An interactive AI-powered tool that analyzes your interests, education, skills, and personality to suggest the most suitable career paths for you.**")


# --- 1️⃣ Personal Details ---
st.header("👤Personal Details")
name = st.text_input("Your Name")
age = st.slider("Your Age", 13, 60, 18)
gender = st.radio("Gender", ["Female", "Male", "Prefer not to say"])
location = st.text_input("🌍 Current City")

# --- 2️⃣ Education Section ---
st.header("🎓 Education Details")
education = st.selectbox(
    "Current Education Level",
    ["High School", "Undergraduate", "Graduate", "Postgraduate", "Other"]
)
field_of_study = st.text_input("Field of Study / Major (if any)")
performance = st.text_input("Academic Performance (CGPA / Marks / Percentage)")

# --- 3️⃣ Interests & Subjects ---
st.header("💡 Interests and Subjects")

subjects = st.text_area(
    "Write your favourite subjects (comma-separated):",
    placeholder="Example: Mathematics, English, Computer Science"
)

interests = st.multiselect(
    "Which fields excite you?",
    ["Technology", "Data & Analytics", "Design", "Marketing", "Finance", "Healthcare",
     "Education", "Law", "Public Service", "Writing & Communication", "Entrepreneurship", 
     "Media & Journalism", "Other"]
)

# --- 4️⃣ Personality & Work Style ---
st.header("🧭 Personality and Work Preferences")
motivation = st.selectbox(
    "What motivates you the most?",
    ["Helping others", "Building things", "Solving problems", "Creativity",
     "Leadership", "Stability", "Learning new things"]
)

work_style = st.multiselect(
    "Preferred Work Style",
    ["Team-based", "Independent work", "Field work", "Office-based", "Remote / Flexible"]
)

hobbies = st.multiselect(
    "What do you enjoy doing in your free time?",
    ["Reading", "Photography", "Gaming", "Cooking", "Music", "Sports", 
     "Traveling", "Volunteering", "Other"]
)

# --- 5️⃣ Career Preferences ---
st.header("🎯 Career Goals and Preferences")
goal = st.selectbox(
    "Current Career Goal",
    ["Still exploring", "Want to find my passion", 
     "Looking for job roles", "Planning higher studies", 
     "Want to switch careers"]
)

preferred_industry = st.selectbox(
    "Preferred Industry or Domain",
    ["Technology", "Healthcare", "Arts & Design", "Finance", "Education",
     "Law", "Public Sector", "Media", "Research", "Open to any"]
)

depth = st.radio("How detailed should the advice be?", ["Brief Summary", "Detailed Roadmap"])
include_courses = st.radio("Would you like online course recommendations?", ["Yes", "No"])

# --- Submit Button ---
if st.button("🚀 Get AI Career Guidance"):
    if not subjects.strip() and not interests:
        st.warning("⚠️ Please enter favourite subjects OR choose interests.")
    else:
        with st.spinner("Analyzing your responses..."):
            prompt = f"""
            You are a professional career counsellor and mentor.
            Based on the details below, give personalized career suggestions.

            User Details:
            Name: {name}
            Age: {age}
            Gender: {gender}
            Location: {location}
            Education Level: {education}
            Field of Study: {field_of_study}
            Academic Performance: {performance}
            Favorite Subjects: {subjects}
            Interests: {', '.join(interests)}
            Motivation: {motivation}
            Work Style: {', '.join(work_style)}
            Hobbies: {', '.join(hobbies)}
            Career Goal: {goal}
            Preferred Industry: {preferred_industry}

            Provide your advice as a {depth.lower()}.
            Include online course recommendations: {include_courses}.

            Structure:
            1️⃣ Top 3 Recommended Career Paths
            2️⃣ Why these fit the user's profile
            3️⃣ Important Skills & Certifications to learn
            4️⃣ Online courses (if applicable)
            5️⃣ Motivational Advice
            """

            response = model.generate_content(prompt)

        st.success("✅ AI Career Guidance Ready!")
        st.subheader("💼 Personalized Career Suggestions")
        st.write(response.text)


