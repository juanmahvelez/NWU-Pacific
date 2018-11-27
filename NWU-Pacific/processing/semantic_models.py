from gensim import corpora, models
import random
from gensim.models import *
import pickle

random.seed(0)

def make_dictionary(texts, object_dir=None):
    dictionary = corpora.Dictionary(texts)
    if object_dir is not None:
        with open(object_dir + 'dictionary.pkl', 'w+') as f:
                pickle.dump(dictionary, f)
    return dictionary

def make_corpus(texts, dictionary, object_dir=None):
    corpus = [dictionary.doc2bow(text) for text in texts]
    if object_dir is not None:
        with open(object_dir + 'corpus.pkl', 'w+') as f:
            pickle.dump(corpus, f)
    return corpus

def make_tfidf(texts=None, corpus=None, dictionary=None, object_dir=None):
    # pass texts to run the whole pipeline
    if texts is not None:
        dictionary = make_dictionary(texts, object_dir)
        corpus = make_corpus(texts, dictionary, object_dir)
    tfidf = models.TfidfModel(corpus, dictionary)
    if object_dir is not None:
        with open(object_dir + 'nostop_tfidf.pkl', 'w+') as f:
            pickle.dump(tfidf, f)

    # output idf values to a csv
    with open(idf_out, 'w+') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(['id','word','idf'])
        for i in tfidf.id2word.keys():
            w.writerow([str(i), tfidf.id2word[i], str(tfidf.idfs[i])])

def split(corpus, training_frac):
    """
    return: corpus_training, corpus_evaluation
    params:
        corpus:
        training_frac:
    """
    # shuffle corpus
    cp = list(corpus)
    random.shuffle(cp)
    p = int(len(cp) * training_frac)
    corpus_training = cp[0:p]
    corpus_evaluation = cp[p:]
    return corpus_training, corpus_evaluation

def train(parameters, corpus_training, dictionary, k):
    """
    return: model
    params:
        parameters: | loaded from json config
        corpus_training:
    """
    supported_model_types = ['LdaModel',
                             'HdpModel']
    if parameters['model_type'] not in supported_model_types:
        raise ValueError, "Currently only supporting %s" % supported_model_types

    parameters['model_args']['id2word'] = dictionary
    parameters['model_args']['corpus'] = corpus_training

    if parameters['model_type'] == 'LdaModel':
        parameters['model_args']['num_topics']=k
        model = LdaModel(**parameters['model_args'])

    if parameters['model_type'] == 'HdpModel':
        #parameters['model_args']['K']=k
        model = HdpModel(**parameters['model_args'])

    with open(parameters['model_dir'] + parameters['model_name'] + '.pkl', 'w+') as f:
        pickle.dump(f, model)

    return model

def evaluate(parameters, corpus_evaluation, model):
    """
    return: log_perplexity
    params:
        parameters: | loaded from json config
        corpus_training:
    """
    supported_model_types = ['LdaModel']
    if parameters['model_type'] not in supported_model_types:
        print "Perplexity evaluation only supports %s" % supported_model_types
        return None
    else:
        return model.log_perplexity(corpus_evaluation)

def get_topics(dictionary, text):
    bow = corpora.Dictionary.doc2bow(dictionary,text)
    topics = list(model.inference([bow])[0][0])
    return topics