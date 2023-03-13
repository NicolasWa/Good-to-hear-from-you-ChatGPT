import os
import openai
from audio_transcription import transcript_audio
from google_tts import synthesize_text

# For now, the audio is only of a fixed size length. Adjust this variable according to your needs
NB_SECONDS_TO_SPEAK = 10

# API key retrieval.
# To get yours, create an openai account and put your API key as an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

print("> When you're done, simply say 'Stop. (followed by silence)'")
print(f"> Say/ask anything to ChatGPT (you have {NB_SECONDS_TO_SPEAK} to speak): ")

# Using Whisper to convert the audio into text
user_message = transcript_audio(NB_SECONDS_TO_SPEAK)
print(user_message)

# messages_history keeps track of the conversation's context
# Important, as we don't want ChatGPT to forget previous prompts
messages_history = [{"role": "user", "content": user_message}]
while user_message != "Stop.":
    # Using ChatGPT to converse with
    assistant_response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages_history)
    # saving assistant (ChatGPT) message
    messages_history.append(assistant_response.choices[0].message)
    # printing assistant (ChatGPT) message
    print(assistant_response.choices[0].message["content"].replace(". ", ".\n"))
    # Using Google Cloud's Text-to-Speech to read the assistant message

    synthesize_text(assistant_response.choices[0].message["content"])

    print("> Your turn to speak: ")
    # Saving user message
    user_message = transcript_audio(NB_SECONDS_TO_SPEAK)
    print(user_message)
    # saving user message
    messages_history.append({"role": "user", "content": user_message})

print("---- Conversation ended ----")