from openai import OpenAI
from openai import RateLimitError, OpenAIError


class LLM:
    """
    Hybrid LLM:
    - Uses OpenAI if quota is available
    - Falls back to local stub if quota is exceeded
    """

    def __init__(self):
        try:
            self.client = OpenAI()
            self.enabled = True
        except OpenAIError:
            self.enabled = False

    def generate(self, prompt: str) -> str:
        if not self.enabled:
            return f"[LLM Stub] {prompt}"

        try:
            response = self.client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content

        except RateLimitError:
            return "[LLM Stub] API quota exceeded. Using local response."

        except OpenAIError as e:
            return f"[LLM Stub] LLM unavailable ({str(e)})"
