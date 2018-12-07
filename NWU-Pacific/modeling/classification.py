import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, roc_auc_score
import pickle
from matplotlib import pyplot as plt

def make_split(df, features, label, test_size=0.33, random_state=0):
    X = df[features]
    y = df[label]
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=test_size,
                                                        random_state=random_state)
    return X_train, X_test, y_train, y_test

def train(model, X, y, file=None):
    model.fit(X, y)
    if file != None:
        with open(file, 'w+') as f:
            pickle.dump(model, file)
    return model

def evaluate(model, X_train, y_train, X_test, y_test, output_dir='./'):
    """ calculates the roc and auc for a model, taking split up data as input
    saves the output to a specific directory. default directory is current
    """
    y_hat_test = model.predict_proba(X_test)[:,1]
    fpr_test, tpr_test, thresholds_test = roc_curve(y_test, y_hat_test)
    test_auc = roc_auc_score(y_test, y_hat_test)
    y_hat_train = model.predict_proba(X_train)[:,1]
    fpr_train, tpr_train, thresholds_train = roc_curve(y_train, y_hat_train)
    train_auc = roc_auc_score(y_train, y_hat_train)

    plt.figure(figsize=(10,7))
    plt.xlabel('False Positive Rate', fontsize=14)
    plt.ylabel('True Positive Rate', fontsize=14)
    plt.title('Receiver operating characteristic Random Forest\n' + label, fontsize=16)
    plt.plot(fpr_test, tpr_test, label='Test auc = {:.3f}'.format(test_auc))
    plt.plot(fpr_train, tpr_train, label='Train auc = {:.3f}'.format(train_auc))
    plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
    plt.savefig('{}roc.png'.format(output_dir))
    plt.close()
