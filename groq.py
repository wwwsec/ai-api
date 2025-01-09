from openai import OpenAI

client = OpenAI(
    base_url="http://wwwsec-groq.deno.dev/openai/v1",
    api_key="you api key"  # replace with your API key
)

response = client.chat.completions.create(
    model="llama3-8b-8192",  # or any other Groq model
    messages=[
        {
            "role": "user",
            "content": "hello,how are you"
        }
    ]
)

print(response.choices[0].message.content)