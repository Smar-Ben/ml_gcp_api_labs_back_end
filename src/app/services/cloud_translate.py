from repositories.cloud_translate import CloudTranslateAPIRepositories


class TextToSpeechAPIService:
    @staticmethod
    def translate(target_language: str, text: str):
        """
        translate_text translate a text into another languages
        :param target_language: language to translate the text
        :param text: text to analyse
        :return: get the text translate with target language
        """
        return CloudTranslateAPIRepositories.translate_text(target_language, text)
