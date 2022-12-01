from repositories.text_to_speech import TextToSpeechAPIRepositories


class TextToSpeechAPIService:
    @staticmethod
    def convert_speech_to_text(text: str):
        """
        transform a text into a speec
        :param text: text to transform.
        """
        return TextToSpeechAPIRepositories.convert_speech_to_text(text)