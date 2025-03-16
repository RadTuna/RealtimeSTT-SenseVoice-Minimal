
from audio_recorder import AudioToTextRecorder
import multiprocessing
import os
import logging

recorder: AudioToTextRecorder | None = None

def main():
    recorder = AudioToTextRecorder(
        model_path="./models/sensevoice_small",
        silero_use_onnx=True,
        silero_deactivity_detection=True,
    )

    while True:
       text = recorder.text()
       print(f"ASR: {text}")


if __name__ == '__main__':
    multiprocessing.freeze_support()  # Windows에서 필요
    main()

