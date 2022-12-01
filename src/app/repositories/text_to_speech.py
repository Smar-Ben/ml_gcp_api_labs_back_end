from google.cloud import texttospeech
from fastapi.responses import FileResponse
from datetime import datetime

# from models.inferences import Inferences
# from utils.datastore_client import DatastoreClient


class TextToSpeechAPIRepositories:
    @staticmethod
    def convert_speech_to_text(text: str):
        """
        get_entities does an entities analysis with cloud natural language
        :param text: text to analyse
        :return: get the result of the entities analysis (with name, category, confidence..)
        """
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        today_str = datetime.today().strftime('%Y%m%d%H%M%S')

        # # The response's audio_content is binary.
        with open(f"src/file/output{today_str}.mp3", "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file "output.mp3"')
        return FileResponse(f"src/file/output{today_str}.mp3")
   