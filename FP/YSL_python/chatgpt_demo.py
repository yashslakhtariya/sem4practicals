import openai
import subprocess

openai.api_key = "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"
model_engine = "text-davinci-003"

qry = input("Enter your query to search ChatGPT : ")

ans = openai.Completion.create(
    engine=model_engine,
    prompt=qry,
    max_tokens=3897,
    n=1,
    stop=None,
    temperature=0.5,
)

print(ans.choices[0].text)
