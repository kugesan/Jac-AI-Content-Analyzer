# Jac-AI-Content-Analyzer

This is a production-style Streamlit application that demonstrates the power of the Jac programming language for building multi-step AI pipelines. The application takes any unstructured text as input and uses a Large Language Model (LLM) to perform a comprehensive analysis.
This project showcases how Jac's by llm feature can be used to call an LLM for different tasks like
- structured data extraction,
- summarization,
- title generation, and
- sentiment analysis,
- all orchestrated within a simple and readable codebase.
<img width="1897" height="1059" alt="image" src="https://github.com/user-attachments/assets/a9a19ed2-fdb3-444b-ba88-fb80f912be9f" />


### Features
With a single click, the application will:
- Extract Key Information: Pulls structured data like key topics and mentioned entities (names, places) from the text.
- Generate a Summary: Creates a concise, two-sentence summary of the content.
- Suggest a Creative Title: Generates a new, catchy headline for the text.
- Analyze Sentiment: Determines if the overall sentiment is Positive, Negative, or Neutral.

### How It Works
The application is split into two key files:
1. analyzer.jac: The core Jac module containing all the AI logic. It defines multiple functions, each powered by the `by llm();` feature, to perform a specific analysis task
2. app.py: A Python script that builds the user interface with Streamlit. It imports the functions from analyzer.jac and calls them to process the user's input and display the results in a clean, organized layout.

### How to Run
Follow these steps to get the application running on your local machine.
1. Install Jac and Required Libraries
You will need the Jac language, Streamlit, and the mtllm
  `pip install jaclang, streamlit, mtllm`
2. Set Up Your API Key:
   `export GEMINI_API_KEY=......`
3. Run the Streamlit App:
   `streamlit run app.py`
