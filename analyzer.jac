import from mtllm.llm { Model }

# Initialize a global LLM instance.
# Ensure your API key (e.g., GEMINI_API_KEY) is set in your environment.
glob llm = Model(model_name="gemini/gemini-2.0-flash");

# Define a Pydantic model for structured data extraction.
# This tells the LLM the exact format we want the output in.
obj ExtractedData {
   has  key_topics: list[str],
        mentioned_entities: list[str],
        summary: str;
}

sem ExtractedData.key_topics = """
    Extract key topics or keywords from the text.
    Return them as a list of strings.
    """;

sem ExtractedData.mentioned_entities = """
    Extract names, places, or organizations mentioned in the text.
    Return them as a list of strings.
    """;

sem ExtractedData.summary = """
    Provide a concise, two-sentence summary of the text.
    """; 

# 1. Define a function to extract structured data using the LLM.
# The return type hint `-> ExtractedData` guides the LLM to output in that Pydantic model format.
def extract_info(text_block: str) -> ExtractedData by llm();

# 2. Define a function to generate a creative title.
def generate_title(text_block: str) -> str by llm();

# 3. Define a function to analyze the sentiment of the text.
def analyze_sentiment(text_block: str) -> str by llm();


# --- Semantic Prompts for each 'def' function ---

# Prompt for the data extraction function.
sem extract_info = """
    Analyze the following text and extract the required information.
    Format your response as a JSON object that matches the provided schema.

    Text to analyze:
    {text_block}
    """;

# Prompt for the title generation function.
sem generate_title = """
    Based on the following text, create a short, catchy, and creative headline that captures the essence of the content.

    Original Text:
    {text_block}
    """;

# Prompt for the sentiment analysis function.
sem analyze_sentiment = """
    Analyze the sentiment of the following text.
    Respond with only a single word: Positive, Negative, or Neutral.

    Text:
    {text_block}
    """;
