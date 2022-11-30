from models.cnl_api import Inferences
from repositories.cnl_api import CloudNaturalLanguageAPIRepositories


class CloudNaturalLanguageAPIService:
    @staticmethod
    def entity(text: str):
        """ "
        save object detected for each inference
        :param inference_results: api input.
        """
        return CloudNaturalLanguageAPIRepositories.get_entities(text)

    @staticmethod
    def sentiment(text: str):
        """ "
        fetch inference object detected for each image
        """
        return CloudNaturalLanguageAPIRepositories.get_sentiment(text)


    @staticmethod
    def classify(text: str):
        """ "
        fetch inference object detected for each image
        """
        return CloudNaturalLanguageAPIRepositories.get_classification(text)