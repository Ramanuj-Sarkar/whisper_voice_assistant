import whisper

model = whisper.load_model("base")  # or "small", "medium"


def transcribe(wav_path: str) -> str:
    result = model.transcribe(wav_path)
    return result["text"].strip()
