from openai import OpenAI

# 初始化客户端
client = OpenAI(
    api_key="you api key",
    base_url="http://wwwsec-mistral.deno.dev/v1"
)

# 发送请求
response = client.chat.completions.create(
    model="mistral-tiny",
    messages=[
        {"role": "user", "content": "hi"}
    ]
)

print(response.choices[0].message.content)