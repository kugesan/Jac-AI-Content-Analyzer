import streamlit as st
from analyzer import extract_info, generate_title, analyze_sentiment, ExtractedData

# --- Page Configuration ---
st.set_page_config(
    page_title="Jac AI Content Analyzer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar ---
st.sidebar.title("About")
st.sidebar.info(
    "This is a production-style application built with Streamlit and Jac. "
    "It uses a Large Language Model (LLM) to perform several text analysis tasks: "
    "data extraction, summarization, title generation, and sentiment analysis. "
    "All the AI-powered logic is handled by the `analyzer.jac` module."
)

# --- Main Application ---
st.title("Jac AI Content Analyzer")
st.write("Paste any text (like an article, report, or email) below to have an AI analyze it for you.")

# Sample text for the user
sample_text = """
Jac is a novel programming language designed to simplify the development of AI applications.
It seamlessly blends traditional programming constructs with AI-specific features, like the `by llm` syntax,
which allows developers to delegate complex tasks to Large Language Models directly within the code.
This approach, demonstrated in the official documentation, streamlines the creation of sophisticated,
multi-step AI pipelines, making it easier for developers like Sarah and Tom to build production-grade systems.
The community response has been overwhelmingly positive.
"""
print('sample_text', sample_text)  # Debugging line to check the sample text
# Text input area
user_input = st.text_area("Enter your text here:", height=250, value=sample_text)

# Analysis button
if st.button("Analyze Content", type="primary"):
    if user_input:
        print('user_input', user_input)  # Debugging line to check the user input
        with st.spinner("The AI is analyzing the text... Please wait."):
            # try:
                # --- Call the Jac functions ---
                # Use a single call to the most comprehensive function
                print('Calling extract_info with user_input')  # Debugging line before calling the function
                structured_data: ExtractedData = extract_info(user_input)
                print('structured_data',structured_data)  # Debugging line to check the structured data
                # Call the other functions for their specific tasks
                creative_title = generate_title(user_input)
                sentiment = analyze_sentiment(user_input)

                # --- Display the results ---
                st.header("Analysis Results")

                # Layout with columns for better presentation
                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Creative Title")
                    st.markdown(f"> {creative_title}")

                    st.subheader("Sentiment")
                    if sentiment == "Positive":
                        st.success(f"**{sentiment}**")
                    elif sentiment == "Negative":
                        st.error(f"**{sentiment}**")
                    else:
                        st.info(f"**{sentiment}**")

                with col2:
                    st.subheader("Key Topics")
                    st.write(", ".join(structured_data.key_topics))

                    st.subheader("Mentioned Entities")
                    st.write(", ".join(structured_data.mentioned_entities))

                st.subheader("Generated Summary")
                st.info(structured_data.summary)

            # except Exception as e:
            #     st.error(f"An error occurred during analysis: {e}")
    else:
        st.warning("Please enter some text to analyze.")
