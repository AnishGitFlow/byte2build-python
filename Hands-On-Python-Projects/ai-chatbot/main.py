import os
from openai import OpenAI

def get_completion(client, messages, message):
    try:
        messages.append({"role": "user", "content": message})
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="gpt-4o"
        )
        response = chat_completion.choices[0].message.content
        messages.append({"role": "assistant", "content": response})
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Please set the OPENAI_API_KEY environment variable.")
        return

    client = OpenAI(api_key=api_key)
    messages = []
    print("Jarvis: Hi I am Jarvis, How may I help you")

    while True:
        user_question = input("User: ")
        response = get_completion(client, messages, user_question)
        if response:
            print(f"Jarvis: {response}")

if __name__ == "__main__":
    main()