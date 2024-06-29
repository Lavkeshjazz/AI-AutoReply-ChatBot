from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<Your Key Here>",
)

command = '''
[5:27 pm, 27/6/2024] ritwik ncc: tha
[5:27 pm, 27/6/2024] ritwik ncc: Pura india aj revenge lene ke mood me hai
[5:28 pm, 27/6/2024] ritwik ncc: Aur tm meet rakh dia
[5:28 pm, 27/6/2024] ritwik ncc: Har gaya na toh tera meet me ayega bhi nhi
[5:28 pm, 27/6/2024] ritwik ncc: Koi
[5:28 pm, 27/6/2024] Lavkesh Jaiswal: kitne baje se match start hai
[5:28 pm, 27/6/2024] ritwik ncc: 8
[5:28 pm, 27/6/2024] ritwik ncc: Se 11 30 tak
[5:28 pm, 27/6/2024] ritwik ncc: Chalta hai
[5:28 pm, 27/6/2024] Lavkesh Jaiswal: aacha theek hai bolte hai phele rakh dene ko
[5:29 pm, 27/6/2024] ritwik ncc: 8 se pehle kar le
[5:30 pm, 27/6/2024] Lavkesh Jaiswal: theek hai bolte hai
[9:34 pm, 27/6/2024] Lavkesh Jaiswal: woo resume wala glitch fix hogya
[9:34 pm, 27/6/2024] Lavkesh Jaiswal: call krna free rahoge tb to bata dege kaise hoga
[9:39 pm, 27/6/2024] Lavkesh Jaiswal: bhai koli out hogya?
'''

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named lavkesh who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Lavkesh"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)