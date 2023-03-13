from google.cloud import texttospeech
from playsound import playsound
from datetime import datetime
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google_credentials.json"

def synthesize_text(text, language="en-US", name_voice="en-US-Studio-M", speed=1.15, keep_audio=False):
    """Synthesizes speech from the input string of text."""
    # name
    file_name = str(datetime.now()) + "_voice.mp3"
    # paths
    data_path = os.path.join(os.getcwd(), "data", "text_to_speech")
    os.makedirs(data_path)
    file_path = os.path.join(data_path, file_name)

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(language_code=language,
                                              name=name_voice,
                                              )

    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3,
                                            speaking_rate=speed)

    response = client.synthesize_speech(request={"input": input_text, "voice": voice, "audio_config": audio_config})

    # The response's audio_content is binary.
    with open(file_path, "wb") as out:
        out.write(response.audio_content)
    playsound(file_path)

    if not keep_audio:
        os.remove(file_path)


if __name__ == "__main__":
    # Small test to see if you are succeeded to connect to google's API
    txt = "Hey, my name is Bryan, I come from Massachussets"
    synthesize_text(txt)