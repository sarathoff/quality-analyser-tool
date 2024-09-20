import streamlit as st
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="Content Quality Analyzer",
    page_icon=":mag:",
    layout="wide",
)

# Directly set the API key here (not recommended for production)
GOOGLE_API_KEY = "AIzaSyCO7WIRmXTQUPeiARLTklKLufkZRfjfg4U"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Streamlit app layout
st.title("Content Quality Analyzer")

# User input
user_content = st.text_area("Paste your full content here", height=300)

# Function to generate the analysis report
def generate_report(content):
    prompt = f"""
    Analyze the following content and provide a comprehensive report:

    Content:
    {content}

    Please provide a detailed analysis covering the following aspects:
    1. Overall Content Quality Score (out of 100)
    2. SEO Analysis
       - Headline effectiveness
       - Keyword usage and density
       - Internal linking suggestions
    3. High CPC Keyword Suggestions
    4. Storytelling Elements
       - Hook effectiveness
       - Introduction analysis
       - Conclusion strength
    5. AI vs Human Writing Detection
    6. Suggestions for Improvement
       - What to include
       - What to remove
       - Areas to enhance
    
    Format the report with clear headings and bullet points for easy readability.
    Start with the Overall Content Quality Score in large text.
    """
    
    response = model.generate_content([prompt])
    return response.text

# Analyze button
if st.button("Analyze Content"):
    if user_content:
        with st.spinner("Analyzing content..."):
            analysis_report = generate_report(user_content)
        
        # Display the analysis report
        st.subheader("Content Analysis Report")
        
        # Extract and display the overall score
        score_line = analysis_report.split('\n')[0]
        if "Overall Content Quality Score" in score_line:
            score = score_line.split(':')[-1].strip()
            st.markdown(f"<h1 style='text-align: center;'>Score: {score}</h1>", unsafe_allow_html=True)
        
        # Display the rest of the report
        st.markdown(analysis_report)
    else:
        st.warning("Please enter some content to analyze.")

# Add some spacing
st.write("\n\n")

# Additional information or instructions
st.info("This tool uses AI to analyze your content and provide suggestions for improvement. The analysis covers various aspects including SEO, storytelling, and overall quality. Use the insights to enhance your content strategy.")