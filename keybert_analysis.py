from keybert import KeyBERT

class KeyBert(object):

    kw_model = KeyBERT('neuralmind/bert-base-portuguese-cased')

    def __init__(self):
        return


    def keybertAnalyses(doc, min_words, max_words, num_terms):
        keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(min_words, max_words), stop_words=None,
                                  use_mmr=True, diversity=0.9, top_n = num_terms)
