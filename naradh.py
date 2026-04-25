#!/usr/bin/env python3

import subprocess
import sys

def install(package):
    subprocess.check_call([
        sys.executable, "-m", "pip", "install",
        "--break-system-packages",
        package
    ])

try:
    from openai import OpenAI
except ImportError:
    print("importing required packages...")
    install("openai")
    from openai import OpenAI
import os

art = """
███╗   ██╗ █████╗ ██████╗  █████╗ ██████╗ ██╗  ██╗
████╗  ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║  ██║
██╔██╗ ██║███████║██████╔╝███████║██║  ██║███████║
██║╚██╗██║██╔══██║██╔══██╗██╔══██║██║  ██║██╔══██║
██║ ╚████║██║  ██║██║  ██║██║  ██║██████╔╝██║  ██║
╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝
"""
bot="""
      ╔═══════╗
      ║ ◉   ◉ ║
      ║  ▬▬▬  ║
╔═════╩═══════╩═════╗
║   [  CPU CORE  ]  ║
╚═════╦═══════╦═════╝
      ║  ███  ║
   ╔══╝       ╚══╗
  ║               ║
  ║               ║
   ╚══╗       ╔══╝
      ║       ║
     ═╩═     ═╩═
"""
print("\033[32m" + art + "\033[0m")
print("\033[36m" + bot + "\033[0m")
client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

print("Type 'exit' to stop\n")
messages=[
        {"role": "system", "content": "You are a helpful assistant. Speak naturally and remember context."},
        {"role": "system", "content": "You are a helpful assistant. If the user says something vague like hmm, ask a follow-up question."},
        {"role": "system", "content": "Speak in a friendly conversational way, show emotions and avoid repeating yourself."}
    ]
RED = "\033[92m"
BLUE = "\033[34m"
RESET = "\033[0m"
while True:
    user_input = input(BLUE+"User: "+RESET)

    if user_input.lower() == "exit":
        break
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=messages
)

    reply = response.choices[0].message.content
    print(RED+"Bot:", reply+RESET)

    messages.append({"role": "assistant", "content": reply})
