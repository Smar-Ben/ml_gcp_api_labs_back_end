import six
from google.cloud import translate_v2 as translate


class CloudTranslateAPIRepositories:
    @staticmethod
    def translate_text(target_language: str, text: str):
        """
        translate_text translate a text into another languages
        :param target_language: language to translate the text
        :param text: text to analyse
        :return: get the text translate with target language
        """
        translate_client = translate.Client()

        if isinstance(text, six.binary_type):
            text = text.decode("utf-8")

        # Text can also be a sequence of strings, in which case this method
        # will return a sequence of results for each text.
        result = translate_client.translate(text, target_language=target_language)
        print(result)
        return {
            "text": result["input"],
            "translation": result["translatedText"],
            "language_detected": result["detectedSourceLanguage"],
        }
