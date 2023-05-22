import os, openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")
messages = [ {"role": "system", "content": "ChatGPT, deliver us your wisdom"} ]

def main():
    print("""
    Welcome to command line ChatGPT. To exit, please
    type in "exit" followed by the enter key.

    """)
    while True:
        message = input(">")
        if (message == "exit"):
            break
        if message:
            messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
        reply = chat.choices[0].message.content
        print(f"{reply}")
        messages.append({"role": "assistant", "content": reply})
    print("""
    Thank you for using my application :)
    
    """)

if __name__ == "__main__":
    main()