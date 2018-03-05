__author__ = 'ahmaddorri'

import numpy as np
from main_codes import LATRE


def _sum(c, Io, l=1, train_set_tags=None):
    antecedent_set, consequent_set = LATRE.projectData(train_set_tags, Io)
    rules = LATRE.associationRule(antecedent_set, consequent_set)
    new_rules ={}
    for r in rules:
        if len(r[0]) <= l:
            new_rules[(r[0],r[1])]= rules[r]
    score = LATRE.calculate_score(new_rules, c)
    return score


def sum_plus(c, Io, kx, kc, kr, l=1, train_set=None):
    antecedent_set, consequent_set = LATRE.projectData(train_set, Io)
    rules = LATRE.associationRule(antecedent_set, consequent_set)
    stab1 = stab(c, kc, train_set)
    sum_score = 0
    sorted_rules = get_sorted_rules(rules)
    for x in Io:
        sum_val = 0
        for r in rules:
            if r[0] == frozenset({x}) and r[1] == c:
                sum_val = rules[r]
                break
        if sum_val > 0:
            rank_value = rank(c, x, kr, sorted_rules)
            stab2 = stab(x, kx, train_set)
            sum_score += sum_val*stab1*stab2*rank_value
    return sum_score


def vote(c, Io, train_set=None):
    antecedent_set, consequent_set = LATRE.projectData(train_set, Io)
    rules = LATRE.associationRule(antecedent_set, consequent_set)
    vote_score = 0
    for x in Io:
        j=0
        for r in rules:
            if r[0] == frozenset({x}) and r[1] == c:
                j = 1
                break
        if j > 0:
            vote_score += j

    return vote_score


def vote_plus(c, Io, kx, kc, kr, train_set=None):
    antecedent_set, consequent_set = LATRE.projectData(train_set, Io)
    rules = LATRE.associationRule(antecedent_set, consequent_set)
    stab1 = stab(c, kc, train_set)
    vote_score = 0
    sorted_rules = get_sorted_rules(rules)
    for x in Io:
        j=0
        for r in rules:
            if r[0] == frozenset({x}) and r[1] == c:
                j = 1
                break
        if j > 0:
            rank_value = rank(c, x, kr, sorted_rules)
            stab2 = stab(x, kx, train_set)
            vote_score += j*stab1*stab2*rank_value

    return vote_score


def rank(c, x, kr, sorted_rules):
    """
    :param c: candidate tag
    :param x: one of the initial tags
    :param kr: tune parameter
    :param rules: sorted rules tha generated from initial tags
    :return:
    """
    pos = 0
    for rule in sorted_rules:
        pos += 1
        if rule[0][0] == frozenset({x}) and rule[0][1] == c:
            break
    return kr/(kr+pos)


def stab(c, k, training_set):
    stab_val = 0
    for t in training_set:
        if c in t:
            stab_val += 1

    return k/(k + abs(k-stab_val))


def ts(c, obj_id,obj_set, title_set, description_set):
    ts_value = 0
    for obj, title, description in zip(obj_set, title_set, description_set):
        if obj == obj_id:
            if c in title:
                ts_value += 1
            if c in description:
                ts_value += 1
            break
    return ts_value


def ts_know_values(t, title, description):
    ts_value = 0
    if t in title:
        ts_value += 1
    if t in description:
        ts_value += 1
    return ts_value


def fis(f, obj_id, obj_set, title_set, description_set):
    fis_value = 0
    if f == "title":
        for obj, title, description in zip(obj_set, title_set, description_set):
            if obj == obj_id:
                for t in title:
                    fis_value += ts_know_values(t, title, description)/len(title)

                break

        return fis_value

    if f == "description":
        for obj, title, description in zip(obj_set, title_set, description_set):
            if obj == obj_id:
                for t in description:
                    fis_value += ts_know_values(t, title, description)/len(description)

                break

        return fis_value


def afs(f, obj_set, title_set, description_set):
    afs_value = 0
    if f == "title":
        for obj in obj_set:
            afs_value += fis("title", obj, obj_set, title_set, description_set)
            #print(afs_value)

        return afs_value/len(obj_set)

    if f == "description":
        for obj in obj_set:
            afs_value += fis("description", obj, obj_set, title_set, description_set)
            #print(afs_value)
        return afs_value/len(obj_set)


def wts(c, obj_id, object_set, title_set, description_set):
    wts_value = 0
    for obj, title, description in zip(object_set, title_set, description_set):
        if obj_id == obj:
            if c in title:
                #print("yes")
                wts_value += afs("title", object_set, title_set, description_set)
            if c in description:
                #print("... yy ...")
                wts_value += afs("description", object_set, title_set, description_set)

            return wts_value

def wts_know_values(c, title, description,object_set,title_set,description_set):
    wts_value = 0
    if c in title:
        #print("yes")
        wts_value += afs("title", object_set, title_set, description_set)
    if c in description:
        #print("... yy ...")
        wts_value += afs("description", object_set, title_set, description_set)

    return wts_value


def tf(c, obj_titles, obj_description):
    tf_value = 0
    for t in obj_titles:
        if c == t:
            tf_value += 1
    for t in obj_description:
        if c == t:
            tf_value += 1
    return tf_value


def wtf(c, obj_titles ,obj_description, obj_set, title_set, desc_set  ):
    wtf_value = 0
    tf_value = 0
    for t in obj_titles:
        if c == t:
            tf_value += 1
    wtf_value += tf_value*afs("title", obj_set, title_set, desc_set)

    tf_value = 0
    for t in obj_description:
        if c == t:
            tf_value += 1
    wtf_value += tf_value*afs("description", obj_set, title_set, desc_set)

    return wtf_value


def iff(c,tag_set):
    fc = 0
    for t in tag_set:
        if c in t:
            fc += 1
    return np.log((len(tag_set)+1) / (fc+1))


""" ######################    util    ########################### """



def get_sorted_rules(rules):
    import operator
    return sorted(rules.items(), key=operator.itemgetter(1), reverse=True)



# smallSetTrain=[[1 ,2 ,3 ,4 ,5],[3, 6, 7, 8],[6, 9, 8],[2, 10, 11, 12],[11 ,2, 1, 13]]
# smallSetTest=[[1,11,14]]
# smallSetTest_expected = [[3]]
#print(_sum(2,[1,11,14],l=2,train_set=smallSetTrain))
#print(sum_plus(2,[1,11,14],1,1,1,1,smallSetTrain))
#


# from main_codes import get_input
#
# train_set_object,train_set_tag, train_set_title, train_set_description = get_input.train_set("SMALL")
#
# objects = train_set_object[0:4]
# print("objects : ", objects)
# print("---------")
# titles = train_set_title[0:4]
# print("titles : ", titles)
# print("---------")
# tags = train_set_tag[0:4]
# print("tags : ", tags)
# print("---------")
# descs = train_set_description[0:4]
# print("description : ", descs)
#
# print(wts(15791,"gZYzE1HIUkQ",objects,titles,descs))



