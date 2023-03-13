# Good-to-hear-from-you-ChatGPT
This small project integrates 3 AI models in order to have an oral conversation with ChatGPT: 
- one model to convert speech into text (Whisper), 
- a conversational agent (ChatGPT), 
- and a final model to generate speech from text (Google Could Text-to-Speech)

The main file to run is talk_with_chatGPT.py.
The current version does not stop automatically the recording once the user has stopped talking. Instead, the user has a certain number of seconds to speak (can be changed by choosing another value for NB_SECONDS_TO_SPEAK).

/!\ Known bug: 
- For Mac users (not tested on Windows or Linux), the audio recording only works with the built-in microphone. Do not connect headphones, otherwise the program will throw an error.
