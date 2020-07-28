import requests
from time import sleep

end_points = ['http://staging-api.padma.io/dictionary_lookup?query=པདྨ་འབྱུང་གནས་',
              'http://staging-api.padma.io/search_texts?query=པདྨ་འབྱུང་གནས་',
              'http://staging-api.padma.io/find_similar?query=པདྨ་འབྱུང་གནས་',
              'http://staging-api.padma.io/word_statistics?query=པདྨ་',
              'http://staging-api.padma.io/tokenize?query=པདྨ་འབྱུང་གནས་',
              'http://staging-api.padma.io/render_text?title=Terdzo-ZI-052&start=2&end=4']

for end_point in end_points:

    r = requests.get(end_point, timeout=30)

    if r.status_code != 200:
        print("ERROR: the request " + end_point + " failed with status code" + str(r.status_code))
        raise ValueError
