# รักษาความต่อเนื่องในการสนทนา
import os
from groq import Groq

os.environ['GROQ_API_KEY'] = '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'

client = Groq()

def generate_content(messages):
    response = client.chat.completions.create(
        messages=messages,
        model='llama-3.1-70b-versatile'
    )
    return response

conversation_history = []

# conversation_history = [
#     {"role": "system", "content": "กรุณาตอบคำถามด้วยภาษาไทยหรือภาษาอังกฤษเท่านั้น"}
# ]

try:
    while True:
        user_input = input("กรุณาใส่คำถามของคุณ (พิมพ์ 'exit' เพื่อออก): ")
        if user_input.lower() == 'exit':
            print("ออกจากโปรแกรม")
            break
        
        # เพิ่มข้อความของผู้ใช้ลงในประวัติการสนทนา
        conversation_history.append({"role": "user", "content": user_input})
        
        output = generate_content(conversation_history)
        content = output.choices[0].message.content
        
        conversation_history.append({"role": "assistant", "content": content})
        
        print(content)

finally:
    # ลบประวัติการสนทนาเมื่อออกจากโปรแกรม
    conversation_history = []
    print('ลบประวัติเรียบร้อย')
