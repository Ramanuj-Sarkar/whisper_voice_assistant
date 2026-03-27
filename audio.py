import sounddevice as sd
from scipy.io.wavfile import write
from pynput import keyboard as kb
import tempfile, numpy as np

SAMPLE_RATE = 16000
frames = []
recording = False

def record_while_held() -> str:
    global frames, recording
    frames = []
    recording = False

    print("Hold SPACE to speak...")

    def on_press(key):
        global recording
        if key == kb.Key.esc or key == kb.KeyCode.from_char('\x03'):
            raise SystemExit  # Ctrl+C inside listener
        elif key == kb.Key.space and not recording:
            recording = True
            print("Recording...")

    def on_release(key):
        if key == kb.Key.space:
            return False  # stops listener

    with kb.Listener(on_press=on_press, on_release=on_release) as listener:
        def callback(indata, *_):
            if recording:
                frames.append(indata.copy())
        with sd.InputStream(samplerate=SAMPLE_RATE, channels=1,
                            dtype="int16", callback=callback):
            listener.join()

    print("Done.")
    audio = np.concatenate(frames) if frames else np.zeros((1,1), dtype="int16")
    tmp = tempfile.mktemp(suffix=".wav")
    write(tmp, SAMPLE_RATE, audio)
    return tmp
