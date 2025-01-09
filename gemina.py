from openai import OpenAI

# 替换为您的Gemini API Key
api_key = "you api key"

# 创建OpenAI客户端
client = OpenAI(
    api_key=api_key,
    base_url="https://wwwsec.deno.dev/v1beta/openai/"
)

# 创建请求
response = client.chat.completions.create(
    model="gemini-1.5-flash",
    messages=[{"role": "user", "content": "hi."}]
)

# 输出响应内容
print(response)
