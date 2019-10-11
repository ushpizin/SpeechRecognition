#!/usr/bin/env python3
import logging
import speech_recognition as sr


# Setup logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter(
    '%(asctime)s - [%(levelname)s] %(message)s'))
logger.addHandler(console_handler)


def recognize(recognizer, source):
    logger.info('Listening...')
    audio = recognizer.listen(source)

    logger.info('Recognizing...')
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return None


def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            transcription = recognize(recognizer, source)
            if transcription:
                logger.info(transcription)
            else:
                logger.info('I didn\'t catch that. What did you say?')


if __name__ == "__main__":
    main()
