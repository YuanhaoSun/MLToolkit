"""
======================================================
Grading - base on classification resuts
======================================================
Give grade on a url link or html file based on 
the coverage of topics using classification
"""

from sklearn.linear_model import RidgeClassifier
from sklearn.feature_extraction.text import Vectorizer

from sklearn.datasets import load_files
from sklearn.externals import joblib

import csv
from time import time

####################################################################
# Cutomized grading scheme
# 
# Default grading scheme:
# assume: E(topic)=1 if topic exists, or E(topic)=0 if it doesn not exist
# Grade = ( E(ads)+E(ca)+E(collect)+E(cookies)+E(security)+E(share)
#           +1.5*E(safeharbor)
#           +0.5*(E(change)+E(children)+E(contact)+E(location)+E(process)+E(retention)+E(truste))
#          )
# Grade = 10 if Grade > 10
# 

def grading(predicted_cate_names):
    
    # predefine the list of categories in three priorities for further grading
    high = ['SafeHarbor']
    medium = set(('Advertising', 'CA', 'Collect', 'Cookies', 'Security', 'Share'))
    low = set(('Change', 'Children', 'Contact', 'Location', 'Process', 'Retention', 'Truste'))

    grade = 0
    
    for item in predicted_cate_names:
        if item in high:
            grade += 1.5
        elif item in medium:
            grade += 1.0
        elif item in low:
            grade += 0.5
        else:
            print 'Error - found an unmatched name during grading:'
            print ('%s!')% item
    
    # deal with situation when grade > 10
    if grade > 10:
        grade = 10

    return grade


####################################################################
# Cutomized grading function using classification results
# gets a predicted_cate and cate_names, returns the grade
#
# parameters:
# predicted_cate: the predicted results on a given test item, List of numbers
# cate_names: standard categories from the train data
#

def grade_privacypolicy(predicted_cate, standard_cate_names):

    # remove duplications in predicted_cate list
    predicted_no_dup = list(set(predicted_cate))

    # get correct category names for predicted
    # using the standard_cate_names
    predicted_cate_names = []
    for item in predicted_no_dup:
        predicted_cate_names.append(standard_cate_names[item])

    # call the grading function to grade on predicted_cate_names
    grade = grading(predicted_cate_names)

    return (grade, predicted_cate_names)


####################################################################
# Cutomized filtering function to return the score for the decision
# given a decision_function and multi_label_threshold
# 
# parameters:
# multi_label_threshold: threshold to feedback 0-n labels, whatever bigger than threshold
# defaults is set to 111 as dummy value. Because False cannot be applied due to situation
# where False(==0) can be used as an actual threshold
# 

def filter_decision_multi(decision_function, multi_label_threshold=111):

    # Multi-label threshold
    if multi_label_threshold != 111:

        filtered_decision_function = []

        for decision_item in decision_function:

            # transfer decision_function to list of tuples -- (score, #)
            # '#' is for future reference of label
            decision_item_num = []
            for i in range(len(decision_item)):
                decision_item_num.append((decision_item[i], i))

            # sort base on score. # will not lost
            decision_item_sorted =  sorted(decision_item_num)
            decision_item_sorted.reverse()

            # filter by multi_label_threshold
            # using paradigm: li = [ x for x in li if condition(x)] to
            # filter base on a condition(x)
            decision_item_filtered = [ x for x in decision_item_sorted if x[0]>multi_label_threshold ]

            # append this item back to the filtered decision function
            filtered_decision_function.append(decision_item_filtered)

        # filtered_decision_function here is a list of list of tuple, 
        # e.g. in case of 3 paragraphs:
        # [
        #   [(score of first label,#), (score of second label,#), (score of third label,#)]
        #   [(score of first label,#), (score of second label,#)]
        #   [(score of first label,#), (score of second label,#), (score of third label,#)]
        # ]
        return filtered_decision_function


####################################################################
# Cutomized filtering function to return the score for the decision
# given a decision_function and one_class_threshold
# 
# parameters:
# one_class_threshold: threshold to filter the biggest label
# default is set to 111 as dummy value. Because False cannot be applied due to situation
# where False(==0) can be used as an actual threshold
# 

def filter_decision_one(decision_function, one_label_threshold=111):

    # One-label threshold
    if one_label_threshold != 111:

        filtered_decision_function = []

        for decision_item in decision_function:

            # transfer decision_function to list of tuples -- (score, #)
            # '#' is for future reference of label
            decision_item_num = []
            for i in range(len(decision_item)):
                decision_item_num.append((decision_item[i], i))

            # sort base on score. # will not lost
            decision_item_sorted =  sorted(decision_item_num)
            decision_item_sorted.reverse()

            # get the top tuple with highest score
            decision_item_top_tuple = decision_item_sorted[0]

            # if the score of the top tuple is bigger than threshold, add to list
            if decision_item_top_tuple[0] >= one_label_threshold:
                filtered_decision_function.append(decision_item_top_tuple)
            # else, it is smaller, add a sign the means no label is marked    
            else:
                filtered_decision_function.append((0, 99)) #99 will be a signal for no label

        # filtered_decision_function here is a list of tuple, 
        # e.g. in case of 3 paragraphs, if their top labels all bigger than the threshold
        # [(score of top label,#), (score of top label,#), (score of top label,#)]
        return filtered_decision_function





# categories = ['Advertising','CA', 'Collect', 'Cookies']
categories = ['Advertising','CA', 'Collect', 'Cookies', 'Security', 'Share', 
            'SafeHarbor','Truste', 'Change', 'Location', 'Children', 'Contact', 
            'Process', 'Retention']


# Load all training datasets
print "Loading privacy policy datasets..."
data_train = load_files('Privacypolicy/raw', categories = categories,
                        shuffle = True, random_state = 42)
print 'Data loaded!'
print

standard_cate_names = data_train.target_names

# load models from pickle files
clf = joblib.load('models/classifier_Ridge.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')


# csvWriter = csv.writer(open("h2t0_classi_0.csv","wb"))
# csvWriter = csv.writer(open("h2t5_classi_0.csv","wb"))
# csvWriter = csv.writer(open("lxml_classi_0.csv","wb"))
# csvWriter = csv.writer(open("h2t0_classi_0.5.csv","wb"))
# csvWriter = csv.writer(open("h2t5_classi_0.5.csv","wb"))
# csvWriter = csv.writer(open("lxml_classi_0.5.csv","wb"))
csvWriter = csv.writer(open("h2t0_classi_0.25.csv","wb"))
# csvWriter = csv.writer(open("h2t5_classi_0.25.csv","wb"))
# csvWriter = csv.writer(open("lxml_classi_0.25.csv","wb"))
# csvWriter = csv.writer(open("h2t0_classi_0.75.csv","wb"))
# csvWriter = csv.writer(open("h2t5_classi_0.75.csv","wb"))
# csvWriter = csv.writer(open("lxml_classi_0.75.csv","wb"))
#########################################################
# Adapt input for getting input from from 1-796.txt:
t0 = time()

for i in range(1, 797):

    print i

    try:
        f = open('txtout_h2t0/'+str(i)+'.txt', 'rb')
        # f = open('txtout_h2t5/'+str(i)+'.txt', 'rb')
        # f = open('txtout_lxml5/'+str(i)+'.txt', 'rb')
        text = f.read()

        if len(text) != 0:

            docs_new = text.split('\n')

            X_new = vectorizer.transform(docs_new)

            ####################################################
            # Predict

            # get decision_function
            pred_decision = clf.decision_function(X_new)

            # predict with one_label_threshold
            # The highest score label in each prediction for one paragraph will
            # be stored only if it is bigger than the threshold
            # predicted = filter_decision_one(pred_decision, one_label_threshold=0)
            predicted = filter_decision_one(pred_decision, one_label_threshold=0.25)
            # predicted = filter_decision_one(pred_decision, one_label_threshold=0.5)
            # predicted = filter_decision_one(pred_decision, one_label_threshold=0.75)


            ####################################################
            # Grading

            # get the number-only list of categories for grading
            predicted_cate = []
            for item in predicted:
                # only add # (i.e. item[1]) into the list
                # also remove the signal '99' for 'no label'
                if item[1] != 99:
                    predicted_cate.append(item[1])

            # get grading result -- (grade, [covered topics])
            result = grade_privacypolicy(predicted_cate, standard_cate_names)

            # decide which topics are not covered
            full_cate_list = data_train.target_names
            full_cate_list.append('Unidentified')
            full_cate_set = set(full_cate_list)
            covered_set = set(result[1])
            uncovered_cate = list(full_cate_set.difference(covered_set))
            
            grade = result[0]

            csvWriter.writerow([i, grade])
        
        # in case when content is empty
        else:
            csvWriter.writerow([i, ' '])
    
    except:
        csvWriter.writerow([i, ' '])
        continue

print "done in %fs" % (time() - t0)