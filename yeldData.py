import os
import codecs
import pandas as pd
import json
import itertools as it
import spacy


from gensim.models import Phrases
from gensim.models.word2vec import LineSentence




nlp = spacy.load('en')


# data_directory = os.path.join('data', 'dataset')

# businesses_filepath = os.path.join(data_directory,
#                                    'business.json')

# review_json_filepath = os.path.join(data_directory,
#                                     'review.json')

# restaurant_ids = set()

# # open the businesses file
# with codecs.open(businesses_filepath, encoding='utf_8') as f:
    
#     # iterate through each line (json record) in the file
#     for business_json in f:
        
#         # convert the json record to a Python dict
#         business = json.loads(business_json)
        
#         # if this business is not a restaurant, skip to the next one
#         if u'Restaurants' not in business[u'categories']:
#             continue
            
#         # add the restaurant business id to our restaurant_ids set
#         restaurant_ids.add(business[u'business_id'])

# # turn restaurant_ids into a frozenset, as we don't need to change it anymore
# restaurant_ids = frozenset(restaurant_ids)

# # print the number of unique restaurant ids in the dataset
# print ('{:,}'.format(len(restaurant_ids)), u'restaurants in the dataset.')


review_txt_filepath = os.path.join('review_text_all.txt')

# with codecs.open(review_txt_filepath, encoding='utf_8') as f:
#     sample_review = list(it.islice(f, 8, 9))[0]
#     sample_review = sample_review.replace('\\n', '\n')
        
# parsed_review = nlp(sample_review)

# for num, sentence in enumerate(parsed_review.sents):
#     print ('Sentence {}:'.format(num + 1))
#     print (sentence)
#     print ()


# for num, entity in enumerate(parsed_review.ents):
#     print ('Entity {}:'.format(num + 1), entity, '-', entity.label_)
#     print ()


#print(parsed_review.token.orth_)

# token_text = [token.orth_ for token in parsed_review]
# token_pos = [token.pos_ for token in parsed_review]

# d = zip(token_text, token_pos)

# #dataframe needs list type
# data = list(d)
# df = pd.DataFrame(data, columns=['token_text', 'part_of_speech'])

# print(df)

def punct_space(token):
    """
    helper function to eliminate tokens
    that are pure punctuation or whitespace
    """
    
    return token.is_punct or token.is_space

def line_review(filename):
    """
    generator function to read in reviews from the file
    and un-escape the original line breaks in the text
    """
    
    with codecs.open(filename, encoding='utf_8') as f:
        for review in f:
            yield review.replace('\\n', '\n')
            
def lemmatized_sentence_corpus(filename):
    """
    generator function to use spaCy to parse reviews,
    lemmatize the text, and yield sentences
    """
    
    for parsed_review in nlp.pipe(line_review(filename),
                                  batch_size=10000, n_threads=4):
        
        for sent in parsed_review.sents:
            yield u' '.join([token.lemma_ for token in sent
                             if not punct_space(token)])


unigram_sentences_filepath = os.path.join('unigram_sentences_all.txt')

# if 1 == 1:

#     with codecs.open(unigram_sentences_filepath, 'w', encoding='utf_8') as f:
#         for sentence in lemmatized_sentence_corpus(review_txt_filepath):
#             f.write(sentence + '\n')


unigram_sentences = LineSentence(unigram_sentences_filepath)



for unigram_sentence in it.islice(unigram_sentences, 230, 240):
    print (u' '.join(unigram_sentence))
    print (u'')

