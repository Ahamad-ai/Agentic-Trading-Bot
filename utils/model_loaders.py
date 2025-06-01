import os
from dotenv import load_dotenv
from config.config_loader import load_config
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

class ModelLoader:
    """
    A Utility class to load embedding models and LLM models.
    """

    def __init__(self):
        load_dotenv()
        self._validate_env()
        self.config=load_config()

    def _validate_env(self):
        """
        Validate necessary environment variables
        """
        required_vars=["GOOGLE_API_KEY"]
        missing_vars= [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            raise EnvironmentError(f"Missing environment variables: {missing_vars}")

    def load_embeddings(self):
        """
        Load and return the embedding model
        """
        print("Loading Embedding model")
        model_name=self.config["embedding_model"]["model_name"]
        return GoogleGenerativeAIEmbeddings(model=model_name)

    def load_llm(self):
        """
        Load and return the LLM Model
        """
        print("LLM Loading ...")
        model_name=self.config["llm"]["model_name"]
        gemini_model=ChatGoogleGenerativeAI(model=model_name)

        return gemini_model


