import os
from datetime import datetime
import openai
from record_audio import record_audio


def transcript_audio(nb_seconds=15, keep_records_transcripts=False):
    # names
    time_prefix = str(datetime.now())
    audio_name = time_prefix + "_audio_record_" + ".wav"
    transcription_name = time_prefix + "_transcription" + ".txt"
    # paths
    data_path = os.path.join(os.getcwd(), "data", "speech_to_text")
    os.makedirs(data_path)
    audio_path = os.path.join(data_path, audio_name)
    transcription_path = os.path.join(data_path, transcription_name)

    # Record the voice audio
    record_audio(audio_path, nb_seconds)

    # Transcription
    audio_file = open(audio_path, "rb")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    transcript_text = transcript["text"].replace(". ", ".\n")

    if keep_records_transcripts:
        # saving the transcription (audio is already saved)
        with open(transcription_path, 'w') as f:
            f.write(transcript_text)
    else:
        # deleting the audio (transcription was not saved)
        os.remove(audio_path)
    return transcript_text


if __name__ == '__main__':
    txt = transcript_audio()
    print(txt)

