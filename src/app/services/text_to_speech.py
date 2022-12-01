from repositories.text_to_speech import TextToSpeechAPIRepositories


class TextToSpeechAPIService:
    @staticmethod
    def convert_speech_to_text(text: str):
        """
        does an entity analysis with cloud natural language
        :param text: text to analyse.
        """
        return TextToSpeechAPIRepositories.convert_speech_to_text(text)