"""
run.py
"""
import os
import argparse
import json
from time import time
import pickle
from model import *

def main():
    t0 = time()
    parser = argparse.ArgumentParser()
    parser.add_argument('-c',
                        '--config_path',
                        help='path for user configurations file')

    parser.add_argument('-k',
                        '--num_topics',
                        help='number of topics used for LDA')

    args = parser.parse_args()

    # load parameters from config file
    with open(args.config_path, 'r') as config:
        parameters = json.load(config)

    if not os.path.exists(parameters['log_dir']):
        os.makedirs(parameters['log_dir'])
    if not os.path.exists(parameters['model_dir']):
        os.makedirs(parameters['model_dir'])

    parameters['model_name'] = '_'.join([parameters['model_type'],
                                         args.num_topics,
                                         'topics'])

    # create log file to save parameters and results
    log_file = parameters['log_dir'] + parameters['model_name'] + '.txt'
    f = open(log_file, 'w', buffering=0)
    f.write("****** %s ******\n" % parameters['model_name'])
    f.write("====================================\n\n")

    f.write("PARAMETERS\n----\n")
    for parameter in sorted(parameters.keys()):
        f.write("%s: %s \n" % (parameter, parameters[parameter]))
    f.write("\n")


    f.write("RUN LOGS\n----\n")
    with open(parameters['object_dir'] + 'corpus.pkl','r') as g:
        corpus = pickle.load(g)
    t1 = time()
    f.write("Corpus loaded in %s seconds\n" % round(t1-t0))
    f.write("%s documents in corpus\n" % len(corpus))

    with open(parameters['object_dir'] + 'dictionary.pkl','r') as g:
        dictionary = pickle.load(g)
    t2 = time()
    f.write("Dictionary loaded in %s seconds\n" % round(t2-t1))
    f.write("%s words in dictionary\n" % len(dictionary))

    # split corpus
    print "Splitting training / evaluation data ..."
    corpus_training, corpus_evaluation = split(corpus, parameters['training_frac'])
    t3 = time()
    f.write("Corpus split in %s seconds\n" % round(t3-t2))
    print "Complete"

    # train model
    k = int(args.num_topics)
    if parameters['model_args']['alpha'] == 'k/50':
        parameters['model_args']['alpha'] = float(k)/50
    print "Training model ..."
    model = train(parameters=parameters,
                  corpus_training=corpus_training,
                  dictionary=dictionary,
                  k=k)
    t4 = time()
    f.write("Model trained in %s seconds\n" % round(t4-t3))
    print "Complete"

    # evaluate model
    print "Evaluating model ..."
    evaluation = evaluate(parameters=parameters,
                          corpus_evaluation=corpus_evaluation,
                          model=model)
    t5 = time()
    f.write("Model evaluated in %s seconds\n\n" % round(t5-t4))
    print "Complete"

    f.write("PERFORMANCE\n----\n")
    f.write('Log Perplexity: %s\n\n' % evaluation)

    f.write("SAMPLE TOPICS\n----\n")
    for topic in model.show_topics(min(k, 50)):
        f.write("%s\n" % topic)

    f.close()
if __name__ == '__main__':
    main()