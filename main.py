import os
from audio import record_while_held
from transcribe import transcribe
from llm import chat
from tts import speak

conversation = []

print("Whisper Voice Assistant — hold SPACE to talk, Ctrl+C to quit\n")

try:
    while True:
        wav_path = record_while_held()
        user_text = transcribe(wav_path)
        os.remove(wav_path)

        if not user_text:
            continue

        print(f"You: {user_text}")
        conversation.append({"role": "user", "content": user_text})

        reply = chat(conversation)
        conversation.append({"role": "assistant", "content": reply})

        print(f"Claude: {reply}\n")
        speak(reply)
except KeyboardInterrupt:
    print("\nGoodbye! (keyboard interrupt)")
except SystemExit:
    print("\nGoodbye! (system exit)")
