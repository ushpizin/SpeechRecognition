import random
import time
import speech_recognition as sr
#install pyaudio and SpeechRecognition for sr
import logging


def recognize_speech_from_mic(recognizer, microphone):
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":

    logging.basicConfig(filename='SpeechRecLog.log',format='%(asctime)s - %(message)s', level=logging.INFO)
    print(logging.getLoggerClass().root.handlers[0].baseFilename)
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print("Speak now.")
    guess = recognize_speech_from_mic(recognizer, microphone)
    while (True):
        if guess["transcription"]:
            # show the user the transcription
            timestr = time.strftime("%Y-%m-%d-%H%M%S")
            print(timestr+":{}".format(guess["transcription"]))
            logging.info(" {}".format(guess["transcription"]))
           # break
        if not guess["success"]:
            print("I didn't catch that. What did you say?\n")
            #break
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        guess = recognize_speech_from_mic(recognizer, microphone)


