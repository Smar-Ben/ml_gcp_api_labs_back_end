from models.cnl_api import Inferences
from repositories.cnl_api import CloudNaturalLanguageAPIRepositories


class CloudNaturalLanguageAPIService:
    @staticmethod
    def entity(text: str):
        """ 
        does an entity analysis with cloud natural language
        :param text: text to analyse.
        """
        return CloudNaturalLanguageAPIRepositories.get_entities(text)

    @staticmethod
    def sentiment(text: str):
        """ 
        does an sentiment analysis with cloud natural language
        :param text: text to analyse.
        """
        return CloudNaturalLanguageAPIRepositories.get_sentiment(text)


    @staticmethod
    def classify(text: str):
        """ 
        does an analysis with cloud natural language to get the content category
        :param text: text to analyse.
        """
        return CloudNaturalLanguageAPIRepositories.get_classification(text)