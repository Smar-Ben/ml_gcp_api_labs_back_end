import six
from google.cloud import translate_v2 as translate


translate_client = translate.Client()

results = translate_client.get_languages(target_language="fr")

for language in results:
    print("{name} ({language})".format(**language))
