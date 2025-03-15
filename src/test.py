
from audio_recorder import AudioToTextRecorder
import multiprocessing
import os
import logging

def main():
    recorder = AudioToTextRecorder(
        model_path="./models/sensevoice_small",
        enable_realtime_transcription=True,
        silero_use_onnx=True,
        silero_deactivity_detection=True,
        level=logging.DEBUG
    )

    recorder.start()

if __name__ == '__main__':
    multiprocessing.freeze_support()  # Windows에서 필요
    main()

