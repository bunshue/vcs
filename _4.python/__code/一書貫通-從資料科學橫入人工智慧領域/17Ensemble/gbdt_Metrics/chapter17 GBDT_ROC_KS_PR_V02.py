
# coding: utf-8

# In[1]:


from sklearn.cross_validation import train_test_split
import sklearn.tree as tree
import sklearn.ensemble as ensemble
import pandas as pd
import sklearn.metrics as metrics
from sklearn.model_selection import GridSearchCV
import os
os.chdir(r"D:\Python_book\17Ensemble\gbdt_Metrics")

# In[3]:


model_data = pd.read_csv("./broadband.csv")
model_data.head()


# In[4]:


target = model_data["BROADBAND"]
orgData1 = model_data.ix[ :,1:-2]


# In[5]:


from sklearn.metrics import confusion_matrix, roc_auc_score, roc_curve, precision_recall_curve, average_precision_score, precision_score, recall_score, auc
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.utils.multiclass import unique_labels
import itertools

def plot_confusion_matrix(y_true, y_pred, cmap='Blues', title="Confusion Matrix", title_fontsize="large", text_fontsize="medium"):
    '''
    args:
        y_true: target values in test
        y_pred: prediction values
    return:
        ax: matplotlib.axes._subplots.AxesSubplot
    '''
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    classes = unique_labels(y_true, y_pred)

    fig, ax = plt.subplots(1, 1, figsize=None)
    cm = confusion_matrix(y_true, y_pred)

    ax.set_title(title, fontsize=title_fontsize)
    # Display an image on the axes
    image = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.get_cmap(cmap))
    plt.colorbar(mappable=image)
    x_tick_marks = np.arange(len(classes))
    y_tick_marks = np.arange(len(classes))
    # Set the x ticks with list of ticks
    ax.set_xticks(x_tick_marks)
    # Set the x-tick labels with list of string labels
    ax.set_xticklabels(classes, fontsize=text_fontsize)
    ax.set_yticks(y_tick_marks)
    ax.set_yticklabels(classes, fontsize=text_fontsize)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if cm[i, j] != 0:
            ax.text(j, i, cm[i, j],
                    horizontalalignment="center",
                    verticalalignment="center",
                    fontsize=text_fontsize,
                    color="white" if cm[i, j] > thresh else "black")

    ax.set_ylabel('True label', fontsize=text_fontsize)
    ax.set_xlabel('Predicted label', fontsize=text_fontsize)
    return ax


def plot_roc_curve(y_true, y_probas, title='ROC Curves', title_fontsize="large", text_fontsize="medium"):
    '''
    args:
        y_true: target values in test
        y_probas: prediction probabilities
    return:
        ax: matplotlib.axes._subplots.AxesSubplot
    '''
    y_true = np.array(y_true)
    probas = np.array(y_probas)

    classes = np.unique(y_true)

    fig, ax = plt.subplots(1, 1, figsize=None)
    ax.set_title(title, fontsize=title_fontsize)

    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(len(classes)):
        print('{0}: {1}'.format(i, classes[i]))
        # pos_label: label considered as positive
        fpr[i], tpr[i], _ = roc_curve(y_true, probas[:, i], pos_label=classes[i])
        # compute the area under the curve
        roc_auc[i] = auc(fpr[i], tpr[i])
        ax.plot(fpr[i], tpr[i], lw=2, label='ROC curve of class {0} (area = {1:0.2f})'''.format(classes[i], roc_auc[i]))
    ax.plot([0, 1], [0, 1], 'k--', lw=2)
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.0])
    ax.set_xlabel('False Positive Rate', fontsize=text_fontsize)
    ax.set_ylabel('True Positive Rate', fontsize=text_fontsize)
    ax.tick_params(labelsize=text_fontsize)
    ax.legend(loc='lower right', fontsize=text_fontsize)
    return ax


def plot_pr_curve(y_true, y_probas, title='Precision-Recall Curves', title_fontsize="large", text_fontsize="medium"):
    '''
    args:
        y_true: target values in test
        y_probas: prediction probabilities
    return:
        ax: matplotlib.axes._subplots.AxesSubplot
    '''
    y_true = np.array(y_true)
    probas = np.array(y_probas)

    classes = np.unique(y_true)

    fig, ax = plt.subplots(1, 1, figsize=None)
    ax.set_title(title, fontsize=title_fontsize)

    precision_dict = dict()
    recall_dict = dict()
    
    for i in range(len(classes)):
        precision_dict[i], recall_dict[i], _ = precision_recall_curve(y_true, probas[:, i], pos_label=classes[i])
        ax.plot(recall_dict[i], precision_dict[i], lw=2,
                    label='Precision-recall curve of class {0} '.format(classes[i]))
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.0])
    ax.set_xlabel('Recall', fontsize=text_fontsize)
    ax.set_ylabel('Precision', fontsize=text_fontsize)
    ax.tick_params(labelsize=text_fontsize)
    ax.legend(loc='best', fontsize=text_fontsize)
    return ax


def plot_ks_curve(y_true, y_probas, title='KS Curve', title_fontsize="large", text_fontsize="medium"):
    y_true = np.array(y_true)
    probas = np.array(y_probas)

    classes = np.unique(y_true)

    thresholds, pct1, pct2, ks_value, max_distance_at = ks_curve(y_true, probas[:, 1].ravel())
    
    fig, ax = plt.subplots(1, 1, figsize=None)

    ax.set_title(title, fontsize=title_fontsize)

    ax.plot(thresholds, pct1, lw=3, label='Class {}'.format(classes[0]))
    ax.plot(thresholds, pct2, lw=3, label='Class {}'.format(classes[1]))
    # get the index of max_distance_at
    idx = np.where(thresholds == max_distance_at)[0][0]
    # Add a vertical line across the axes
    ax.axvline(max_distance_at, *sorted([pct1[idx], pct2[idx]]),
               label='KS Statistic: {:.3f} at {:.3f}'.format(ks_value, max_distance_at),
               linestyle=':', lw=3, color='black')

    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.0])

    ax.set_xlabel('Threshold', fontsize=text_fontsize)
    ax.set_ylabel('Percentage below threshold', fontsize=text_fontsize)
    ax.tick_params(labelsize=text_fontsize)
    ax.legend(loc='lower right', fontsize=text_fontsize)

    return ax


def ks_curve(y_true, y_probas):
    y_true, y_probas = np.asarray(y_true), np.asarray(y_probas)
    idx = y_true == 0 # if target value is 0 then true else false
    data1 = np.sort(y_probas[idx]) # predicition probabilities which target value is 0
    data2 = np.sort(y_probas[np.logical_not(idx)]) # predicition probabilities which target value is 1

    ctr1, ctr2 = 0, 0
    thresholds, pct1, pct2 = [], [], []
    while ctr1 < len(data1) or ctr2 < len(data2):

        # Check if data1 has no more elements
        if ctr1 >= len(data1):
            current = data2[ctr2]
            while ctr2 < len(data2) and current == data2[ctr2]:
                ctr2 += 1

        # Check if data2 has no more elements
        elif ctr2 >= len(data2):
            current = data1[ctr1]
            while ctr1 < len(data1) and current == data1[ctr1]:
                ctr1 += 1

        else:
            if data1[ctr1] > data2[ctr2]:
                current = data2[ctr2]
                while ctr2 < len(data2) and current == data2[ctr2]:
                    ctr2 += 1

            elif data1[ctr1] < data2[ctr2]:
                current = data1[ctr1]
                while ctr1 < len(data1) and current == data1[ctr1]:
                    ctr1 += 1

            else:
                current = data2[ctr2]
                while ctr2 < len(data2) and current == data2[ctr2]:
                    ctr2 += 1
                while ctr1 < len(data1) and current == data1[ctr1]:
                    ctr1 += 1

        thresholds.append(current)
        pct1.append(ctr1)
        pct2.append(ctr2)

    thresholds = np.asarray(thresholds)
    pct1 = np.asarray(pct1) / float(len(data1)) # fpr
    pct2 = np.asarray(pct2) / float(len(data2)) # tpr

    if thresholds[0] != 0:
        thresholds = np.insert(thresholds, 0, [0.0])
        pct1 = np.insert(pct1, 0, [0.0])
        pct2 = np.insert(pct2, 0, [0.0])
    if thresholds[-1] != 1:
        thresholds = np.append(thresholds, [1.0])
        pct1 = np.append(pct1, [1.0])
        pct2 = np.append(pct2, [1.0])

    differences = pct1 - pct2
    # np.argmax: Returns the indices of the maximum values along an axis
    ks_value, max_distance_at = np.max(differences), thresholds[np.argmax(differences)]

    return thresholds, pct1, pct2, ks_value, max_distance_at


def print_classification_report(y_true, y_pred):
    '''
    args:
        y_true: target values in test
        y_probas: prediction values
    '''
    print(metrics.classification_report(y_true, y_pred))


# In[6]:


train_data, test_data, train_target, test_target = train_test_split(
    orgData1, target, test_size=0.4, train_size=0.6, random_state=12345)  #划分训练集和测试集


# In[7]:


#决策树算法
param_grid = {
    'criterion':['entropy','gini'],
    'max_depth':[2,3,4,5,6,7,8],
    'min_samples_split':[4,8,12,16,20,24,28] 
}
clf = tree.DecisionTreeClassifier()
clfcv = GridSearchCV(estimator=clf, param_grid=param_grid, scoring='roc_auc', cv=4)
clfcv.fit(train_data, train_target)

test_est = clfcv.predict(test_data)
y_predicted_probas = clfcv.predict_proba(test_data)
print("decision tree accuracy:")
print(metrics.classification_report(test_target,test_est))
print("decision tree AUC:")
fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, y_predicted_probas[:, 1])
print('AUC = %.4f' %metrics.auc(fpr_test, tpr_test))


# In[8]:


plot_confusion_matrix(test_target, test_est)
plot_roc_curve(test_target, y_predicted_probas)
plot_pr_curve(test_target, y_predicted_probas)
plot_ks_curve(test_target, y_predicted_probas)


# In[9]:


#GBDT
param_grid = {
    'loss':['deviance','exponential'],
    'learning_rate':[0.1,0.3,0.5,0.7,1],
    'n_estimators':[10,15,20,30],  #决策树个数-GBDT特有参数
    'max_depth':[1,2,3],  #单棵树最大深度-GBDT特有参数
    'min_samples_split':[2,4,8,12,16,20] 
    
}

gbc = ensemble.GradientBoostingClassifier()
gbccv = GridSearchCV(estimator=gbc, param_grid=param_grid, scoring='roc_auc', cv=4)
gbccv.fit(train_data, train_target)
test_est = gbccv.predict(test_data)
y_predicted_probas = gbccv.predict_proba(test_data)
print("gradient boosting accuracy:")
print(metrics.classification_report(test_target,test_est))
print("gradient boosting AUC:")
fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, y_predicted_probas[:, 1])
print('AUC = %.4f' %metrics.auc(fpr_test, tpr_test))


# In[10]:


gbccv.best_params_


# In[11]:


plot_confusion_matrix(test_target, test_est)
plot_roc_curve(test_target, y_predicted_probas)
plot_pr_curve(test_target, y_predicted_probas)
plot_ks_curve(test_target, y_predicted_probas)


# In[19]:


# Adaboost算法
param_grid = {
    #'base_estimator':['DecisionTreeClassifier'],
    'learning_rate':[0.1,0.3,0.5,0.7,1]
}
abc = ensemble.AdaBoostClassifier(n_estimators=100,algorithm='SAMME')
abccv = GridSearchCV(estimator=abc, param_grid=param_grid, scoring='roc_auc', cv=4)
abccv.fit(train_data, train_target)
test_est = abccv.predict(test_data)
y_predicted_probas = abccv.predict_proba(test_data)
print("abc classifier accuracy:")
print(metrics.classification_report(test_target,test_est))
print("abc classifier AUC:")
fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, y_predicted_probas[:, 1])
print('AUC = %.4f' %metrics.auc(fpr_test, tpr_test))


# In[20]:


abccv.best_params_


# In[21]:


plot_confusion_matrix(test_target, test_est)
plot_roc_curve(test_target, y_predicted_probas)
plot_pr_curve(test_target, y_predicted_probas)
plot_ks_curve(test_target, y_predicted_probas)


# In[22]:


# 随机森林
param_grid = {
    'criterion':['entropy','gini'],
    'max_depth':[7,8,10,12],
    'n_estimators':[11,13,15],  #决策树个数-随机森林特有参数
    'max_features':[0.2,0.3,0.4,0.5], #每棵决策树使用的变量占比-随机森林特有参数
    'min_samples_split':[4,8,12,16] 
}

rfc = ensemble.RandomForestClassifier()
rfccv = GridSearchCV(estimator=rfc, param_grid=param_grid, scoring='roc_auc', cv=4)
rfccv.fit(train_data, train_target)
test_est = rfccv.predict(test_data)
y_predicted_probas = rfccv.predict_proba(test_data)
print("random forest accuracy:")
print(metrics.classification_report(test_target, test_est))
print("random forest AUC:")
fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, y_predicted_probas[:, 1])
print('AUC = %.4f' %metrics.auc(fpr_test, tpr_test))


# In[23]:


rfccv.best_params_


# In[24]:


plot_confusion_matrix(test_target, test_est)
plot_roc_curve(test_target, y_predicted_probas)
plot_pr_curve(test_target, y_predicted_probas)
plot_ks_curve(test_target, y_predicted_probas)

#%%