import json

from ..models import EmergencySignal, LLMResponse
from openai import OpenAI
from src.config import SCW_SECRET_KEY


async def verificate_signal(signal: EmergencySignal):
    response = await get_llm_response(signal.text)
    result = LLMResponse(
        category=response['category'],
        confidence=response['confidence'],
        explanation=response['explanation'],
    )
    return result


async def verify_for_broadcasting(text: str):
    return True


async def get_llm_response(text: str):
    """Verify via LLM classification."""

    client = OpenAI(
        base_url="https://api.scaleway.ai/1bd896b3-3aab-4161-98b5-b3d525511efd/v1",
        api_key=SCW_SECRET_KEY,
    )

    prompt = (
        "You are an assistant that classifies emergency messages.\n"
        "Respond as JSON with fields: category, confidence (0-1), explanation.\n"
        f"Message: '{text}'\n"
        "Categories: medical, fire, flood, earthquake, violence, accident, false, ambiguous, other."
        "If there no emergency at all category must be false"
    )

    response = client.chat.completions.create(
        model="gemma-3-27b-it",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=512,
        temperature=1,
        top_p=0.95,
        presence_penalty=0,
    )
    content = response.choices[0].message.content.replace('```json', '').replace('```', '').strip()
    parsed = json.loads(content)
    print(parsed)
    return parsed
