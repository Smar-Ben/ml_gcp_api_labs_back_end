from dataclasses import asdict
from google.cloud import translate_v2 as translate


class CloudTranslateUtils:
    """
    check_scenario: check if the first mission is possible,
    scenario : scenario of the mission has two dict pickup_zone for the pallet in the pickup_zone
                and drop_zone for the pallet in the drop_zone
    return a scenario Object if it's possible else return an empty string
    """

    @staticmethod
    def detected_language(translate_client, text: str):
        result = translate_client.detect_language(text)

        return result.get("language")
