__author__ = 'ahmaddorri'

from main_codes import get_input
###### function for project data ######


def projectData(trainSet_tags,
                testItemSet):

    ## get trainSet and project that with respect to testItemSet
    antecedent_set = []
    consequent_set = []

    for tSet in trainSet_tags:
        diff = list(set(tSet)-set(testItemSet))
        if 0 < len(diff) < len(tSet):
            consequent_set.append(diff)
            antecedent_set.append(list(set(tSet).intersection(testItemSet)))

    return antecedent_set ,consequent_set


############  association rule generator  #############

import itertools
def findsubsets_list(S):
    subsets = []

    for m in range(1,len(S)+1):
        sub=list(itertools.combinations(S, m))
        for s in sub:
            subsets.append(list(s))
    return subsets

#print(findsubsets_list(testDateSet[0]))


def associationRule(antecedent_set, consequent_set, confidence_min=0.01, sup_min=2):
    rules ={}
    cons_dict={}
    for ant ,cons in zip(antecedent_set,consequent_set):
        subsetlist = findsubsets_list(ant)
        for s in subsetlist:
            if frozenset(s) in cons_dict:
                cons_dict[frozenset(s)] += 1
            else:
                cons_dict[frozenset(s)] = 1
            for c in cons:
                if (frozenset(s),(c)) in rules:
                    rules[(frozenset(s),(c))] += 1
                else:
                    rules[(frozenset(s),(c))] = 1

    new_rules = {}
    for key, value in rules.items():
        if value >= sup_min:
            confidence = value/cons_dict[key[0]]
            if confidence >= confidence_min:
                new_rules[key] = confidence
    return new_rules

######################### model ##############################


def get_candidate_tag(initial_tags, trainDataSet_tags, confidence_min, sup_min):
    for test_tag_list in initial_tags:
        # i += 1
        # print("data number ",i, " read")
        antecedent_set, consequent_set = projectData(trainDataSet_tags, test_tag_list)
        rules = associationRule(antecedent_set, consequent_set,confidence_min,sup_min)
        ranked_candidate_tags_pair = get_ranked_candidate(rules)
    return ranked_candidate_tags_pair


def run_model(testDateSet,testDataSet_expected,trainDataSet):
    if not(len(testDateSet) == len(testDataSet_expected)):
        print("WARNING : length testData and expected not equal")
    else:
        print("train start")
    i=0
    for test_tag_list, expected_list in zip(testDateSet, testDataSet_expected):
        # i += 1
        # print("data number ",i, " read")
        antecedent_set, consequent_set = projectData(trainDataSet, test_tag_list)
        rules = associationRule(antecedent_set, consequent_set)
        ranked_candidate_tags_pair = get_ranked_candidate(consequent_set,rules)
        primary_evaluate(ranked_candidate_tags_pair, expected_list)
    print("finished")

    main_evaluate(len(testDateSet))

############################# elvaluate #######################

p_at5_sum = 0
MRR_sum = 0
def primary_evaluate(pair_ranked_list , expected_list):

    ######### p@5 ###########
    global p_at5_sum
    p_at5_sum +=p_at5(pair_ranked_list , expected_list)
    #print(p_at5_sum)
    global MRR_sum
    MRR_sum+=MRR(pair_ranked_list , expected_list)



def p_at5(pair_ranked_list , expected_list):
    relevant_num=0
    for i in range(0,5):
        if(pair_ranked_list[i][0] in expected_list):
            relevant_num+=1
    #print("..................")
    #print(ranked_list)
    #print(expected_list)
    #print("..................")
    return relevant_num/5

def MRR(ranked_list , expected_list):
    first_rel_index=0
    find = False
    for i in range(0,len(ranked_list)):
        if(ranked_list[i][0] in expected_list):
            first_rel_index=i
            find = True
            break
    if(find):
        return 1/(first_rel_index+1)
    else:
        return 0

def main_evaluate(len_testData):
    print("p@5 is : ",p_at5_sum / len_testData)
    print("MRR is : ",MRR_sum/len_testData)

###############  utils #################


def get_ranked_candidate(rules):

    """ return a list of tupel(pair) of candidate tag and the score of that  Example: [(t1, score),(t2, score)]"""
    candidates = set([x[1] for x in list(rules.keys())])
    candidate_tags_pair=[]
    for tag in candidates:
        score = calculate_score(rules, tag)
        candidate_tags_pair.append((tag, score))

    candidate_tags_pair.sort(key=lambda x: x[1],reverse=True)
    return candidate_tags_pair

def flat_consequent_set(consequent_set):
    flat_set=[]
    for cons in consequent_set:
        for tag in cons:
            flat_set.append(tag)
    return set(flat_set)


def calculate_score(rules, tag):

    score = 0.
    for key , value in rules.items():
        if(key[1]==tag):
            score += value
    return score

##########################################


# test_set, test_expected = get_input.test_set("SMALL")
# train_set = get_input.train_set("SMALL")
# run_model(test_set, test_expected, train_set)


# smallSetTrain=[[1 ,2 ,3 ,4 ,5],[3, 6, 7, 8],[6, 9, 8],[2, 10, 11, 12],[11 ,2, 1, 13]]
# smallSetTest=[[1,11,14]]
# smallSetTest_expected = [[3]]
#
# run_model(smallSetTest, smallSetTest_expected, smallSetTrain)




