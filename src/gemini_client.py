"""
GitHub Models API Client Module
Handles all interactions with GitHub Models API (compatible with Copilot)
"""

import os
import time
from typing import List, Optional
from openai import OpenAI
from dotenv import load_dotenv


class OpenAIClient:
    """Client for interacting with GitHub Models API"""
    
    def __init__(self, api_key: Optional[str] = None, model_name: str = "gpt-4o"):
        """
        Initialize GitHub Models client
        
        Args:
            api_key: GitHub Personal Access Token. If None, will load from .env
            model_name: Name of the model to use (gpt-4o, gpt-4o-mini, etc.)
        """
        load_dotenv()
        self.api_key = api_key or os.getenv("GITHUB_TOKEN")
        self.model_name = model_name
        
        if not self.api_key:
            raise ValueError(
                "GITHUB_TOKEN not found. Please set it in .env file or pass it as parameter"
            )
        
        # GitHub Models endpoint
        self.client = OpenAI(
            api_key=self.api_key,
            base_url="https://models.inference.ai.azure.com"
        )
    
    def generate_response(
        self, 
        prompt: str, 
        temperature: float = 1.0,
        max_retries: int = 5,
        retry_delay: float = 5.0
    ) -> str:
        """
        Generate a single response from OpenAI
        
        Args:
            prompt: The prompt to send to OpenAI
            temperature: Controls randomness (0.0 to 2.0)
            max_retries: Maximum number of retries on failure
            retry_delay: Delay between retries in seconds
            
        Returns:
            Generated response text
        """
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=temperature
                )
                return response.choices[0].message.content
            except Exception as e:
                error_str = str(e)
                if "429" in error_str or "rate_limit" in error_str.lower():
                    # Incremento exponencial del retardo para 429
                    current_delay = retry_delay * (2 ** attempt)
                    if attempt < max_retries - 1:
                        print(f"⚠️  Rate limit hit (429). Retrying in {current_delay}s... (Attempt {attempt + 1}/{max_retries})")
                        time.sleep(current_delay)
                        continue
                
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
            prompt: The prompt to send to OpenAI
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
