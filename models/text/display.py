import itertools
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score, precision_score, recall_score, classification_report

def plot_confusion_matrix(cm, classes,
                          normalize = False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.figure(figsize=(8,8))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = np.around(cm.astype('float') / cm.sum(axis=1)[:, np.newaxis], decimals = 2)
        plt.title("Normalized Confusion Matrix")
    else:
        plt.title('Confusion Matrix')

    # print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    # plt.savefig('cm.png')

def display_results(y_test, pred_probs, norm = False):
    emotion_keys = ['Angry', 'Disgust', 'Fear', 'Happiness', 'Neutral', 'Sadness', 'Surprise']
    pred = np.argmax(pred_probs, axis=-1)
    print('Test Set Accuracy =  {0:.3f}'.format(accuracy_score(y_test, pred)))
    print('Test Set F-score =  {0:.3f}'.format(f1_score(y_test, pred, average='weighted', labels=np.unique(pred))))
    print('Test Set Precision =  {0:.3f}'.format(precision_score(y_test, pred, average='weighted', labels=np.unique(pred))))
    print('Test Set Recall =  {0:.3f}'.format(recall_score(y_test, pred, average='weighted')))
    print()
    print(classification_report(y_test, pred, labels=np.unique(pred)))
    print()
    # set norm = True to normalize confusion matrix
    plot_confusion_matrix(confusion_matrix(y_test, pred), classes=emotion_keys, normalize = norm)