from keybert_analysis import *
from string_manipulation import *
from vocab import *

def read_user_story():
    return 'como usuario eu desejo fazer o cadastro de coisas na loja'


def user_story_analysis(key_bert, user_story, stop_words):

    cleansed_story = remove_stop_words(user_story, stop_words)
    aux = contains_create(cleansed_story)

    if aux != '':
        keyterms_list = key_bert.keybertAnalysis(cleansed_story, 3, 3, 5)
        keyterms_list.sort(key=lambda a: a[1], reverse=True)
        keyterms_string_list = [i[0] for i in keyterms_list]

    str = main_object(contains_term(keyterms_string_list, aux[0]), aux[0])

    palavras = str.split(' ')
    return palavras
