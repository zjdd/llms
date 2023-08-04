import os
os.environ['OPENAI_API_KEY']="sk-111111111111111111111111111111111111111111111111"
os.environ['OPENAI_API_BASE']="http://0.0.0.0:5001/v1"
import openai
import sys

response = openai.ChatCompletion.create(
  model="x",
  messages = [{ 'role': 'system', 'content': "Answer in a consistent style." },
    {'role': 'user', 'content': "Teach me about patience."},
    {'role': 'assistant', 'content': "The river that carves the deepest valley flows from a modest spring; the grandest symphony originates fr        om a single note; the most intricate tapestry begins with a solitary thread."},
    {'role': 'user', 'content': "Teach me about the ocean."},
  ],
  stream=True
)

for i in response:
    print(i['choices'][0]['message']['content'], end='')
    sys.stdout.flush()