from openai import OpenAI
from ..config import SCW_SECRET_KEY

client = OpenAI(
    base_url = "https://api.scaleway.ai/1bd896b3-3aab-4161-98b5-b3d525511efd/v1",
    api_key = SCW_SECRET_KEY
)


response = client.chat.completions.create(
    model="gpt-oss-120b",
    messages=[
        { "role": "system", "content": "You are a helpful assistant" },
        { "role": "user", "content": "" },
    ],
    max_tokens=512,
    temperature=1,
    top_p=1,
    presence_penalty=0,
    stream=True,
)


for chunk in response:
  if chunk.choices and chunk.choices[0].delta.content:
   print(chunk.choices[0].delta.content, end="", flush=True)