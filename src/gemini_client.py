"""
Gemini API Client Module
Handles all interactions with Google's Gemini Pro API
"""

import os
import time
from typing import List, Optional
import google.generativeai as genai
from dotenv import load_dotenv


class GeminiClient:
    """Client for interacting with Google Gemini Pro API"""
    
    def __init__(self, api_key: Optional[str] = None, model_name: str = "gemini-pro"):
        """
        Initialize Gemini client
        
        Args:
            api_key: Google API key. If None, will load from .env
            model_name: Name of the Gemini model to use
        """
        load_dotenv()
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        
        if not self.api_key:
            raise ValueError(
                "GEMINI_API_KEY not found. Please set it in .env file or pass it as parameter"
            )
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name)
        self.generation_config = None
    
    def generate_response(
        self, 
        prompt: str, 
        temperature: float = 1.0,
        max_retries: int = 3,
        retry_delay: float = 2.0
    ) -> str:
        """
        Generate a single response from Gemini
        
        Args:
            prompt: The prompt to send to Gemini
            temperature: Controls randomness (0.0 to 2.0)
            max_retries: Maximum number of retries on failure
            retry_delay: Delay between retries in seconds
            
        Returns:
            Generated response text
        """
        generation_config = genai.GenerationConfig(
            temperature=temperature
        )
        
        for attempt in range(max_retries):
            try:
                response = self.model.generate_content(
                    prompt,
                    generation_config=generation_config
                )
                return response.text
            except Exception as e:
                if attempt < max_retries - 1:
                    print(f"⚠️  Attempt {attempt + 1} failed: {e}. Retrying in {retry_delay}s...")
                    time.sleep(retry_delay)
                else:
                    raise Exception(f"Failed to generate response after {max_retries} attempts: {e}")
    
    def generate_multiple_responses(
        self,
        prompt: str,
        count: int,
        temperature: float = 1.0,
        delay: float = 0.5
    ) -> List[str]:
        """
        Generate multiple diverse responses for the same prompt
        
        Args:
            prompt: The prompt to send to Gemini
            count: Number of responses to generate
            temperature: Controls randomness
            delay: Delay between requests to avoid rate limiting
            
        Returns:
            List of generated responses
        """
        responses = []
        
        for i in range(count):
            print(f"🔄 Generating response {i + 1}/{count}...")
            response = self.generate_response(prompt, temperature)
            responses.append(response)
            
            # Add delay to avoid rate limiting
            if i < count - 1:
                time.sleep(delay)
        
        return responses
