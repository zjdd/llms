import os
os.environ['OPENAI_API_KEY']="sk-111111111111111111111111111111111111111111111111"
os.environ['OPENAI_API_BASE']="http://0.0.0.0:5001/v1"
import openai
import sys

instuction = '''\
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. The answer always been translate into Chinese language.
If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
The answer always been translate into Chinese language.
'''

response = openai.ChatCompletion.create(
  model="Llama2-Chinese-7b-Chat",
messages = [{ 'role': 'system', 'content': instuction},
      {'role': 'user', 'content': "你好呀"},
  ],
  stream=True,
  temparature=0
)

for i in response:
    print(i['choices'][0]['message']['content'], end='')
    sys.stdout.flush()