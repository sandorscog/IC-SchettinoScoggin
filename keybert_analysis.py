from keybert import KeyBERT

class KeyBert(object):

    def __init__(self):
        self.kw_model = KeyBERT('neuralmind/bert-base-portuguese-cased')


    def keybertAnalysis(self, doc, min_words=1, max_words=2, num_terms=5):
        return self.kw_model.extract_keywords(doc, keyphrase_ngram_range=(min_words, max_words), stop_words=None,
                                  use_mmr=True, diversity=0.9, top_n = num_terms)
