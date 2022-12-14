from google.cloud import language_v1

# from models.inferences import Inferences
# from utils.datastore_client import DatastoreClient


class CloudNaturalLanguageAPIRepositories:
    @staticmethod
    def get_entities(text: str):
        """
        get_entities does an entities analysis with cloud natural language
        :param text: text to analyse
        :return: get the result of the entities analysis (with name, category, confidence..)
        """
        # Init client for Cloud Natural language
        client = language_v1.LanguageServiceClient()
        # Available types: PLAIN_TEXT, HTML
        type_ = language_v1.Document.Type.PLAIN_TEXT
        # Optional. If not specified, the language is automatically detected.
        # For list of supported languages:
        # https://cloud.google.com/natural-language/docs/languages
        # language = "fr"
        document = {"content": text, "type_": type_}
        # Available values: NONE, UTF8, UTF16, UTF32
        encoding_type = language_v1.EncodingType.UTF8
        response = client.analyze_entities(
            request={"document": document, "encoding_type": encoding_type}
        )
        # Get the language detected by CNL API
        language_detected = response.language
        # List of entities that we will return
        list_of_entites = []
        # Loop through entitites returned from the API
        for entity in response.entities:
            wikipedia_url = ""
            for metadata_name, metadata_value in entity.metadata.items():
                if "wikipedia" in metadata_name.lower():
                    wikipedia_url = metadata_value
            entity_dict = {
                "name": entity.name,
                "type": language_v1.Entity.Type(entity.type_).name,
                "score": float(entity.salience),
                "language": language_detected,
                "wikipedia_url": wikipedia_url,
            }
            list_of_entites.append(entity_dict)
        return list_of_entites

    @staticmethod
    def get_sentiment(text):
        """
        get_sentiment does an sentiment analysis with cloud natural language
        :param text: text to analyse
        :return: get the result of the sentiment analysis (with name, score, magnitude..)
        """
        # Init client for Cloud Natural language
        client = language_v1.LanguageServiceClient()
        # Available types: PLAIN_TEXT, HTML
        type_ = language_v1.Document.Type.PLAIN_TEXT
        # Optional. If not specified, the language is automatically detected.
        # For list of supported languages:
        # https://cloud.google.com/natural-language/docs/languages
        # language = "en"
        document = {"content": text, "type_": type_}
        # Available values: NONE, UTF8, UTF16, UTF32
        encoding_type = language_v1.EncodingType.UTF8
        response = client.analyze_sentiment(
            request={"document": document, "encoding_type": encoding_type}
        )
        sentiment_result = {
            "text": text,
            "score": float(response.document_sentiment.score),
            "magnitude": float(response.document_sentiment.magnitude),
            "language": response.language,
        }
        return sentiment_result

    @staticmethod
    def get_classification(text):
        """
        get_classification give the three possible content category of a text
        :param text: text to analyse
        :return: get the three most possible content category for a text
        """
        client = language_v1.LanguageServiceClient()
        # Available types: PLAIN_TEXT, HTML
        type_ = language_v1.Document.Type.PLAIN_TEXT
        # Optional. If not specified, the language is automatically detected.
        # For list of supported languages:
        # https://cloud.google.com/natural-language/docs/languages
        document = {"content": text, "type_": type_}
        content_categories_version = (
            language_v1.ClassificationModelOptions.V2Model.ContentCategoriesVersion.V2
        )
        response = client.classify_text(
            request={
                "document": document,
                "classification_model_options": {
                    "v2_model": {
                        "content_categories_version": content_categories_version
                    }
                },
            }
        )
        all_category = []
        # Get the first three category of the text return by the cloud natural language
        for idx, category in enumerate(response.categories):
            if idx >= 3:
                break
            else:
                # get all api result
                category_dict = {
                    "name": category.name,
                    "confidence": float(category.confidence),
                }
                all_category.append(category_dict)
        return all_category
