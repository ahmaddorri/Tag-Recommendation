__author__ = 'ahmaddorri'

import numpy as np
import pandas as pd
import random




# ###----------------------------####  read Data  ####----------------------------### Block1

FILE_NAME = "/Users/ahmaddorri/Desktop/tag recommendation/data/mixed/youtube/features_part"

small_down_boundary = 2
medium_down_boundary = 6
large_down_boundary = 10
up_boundary = 74  # youtube


small_subset_obj = []
medium_subset_obj = []
large_subset_obj = []

small_subset_tags = []
medium_subset_tags = []
large_subset_tags = []

small_subset_titles = []
medium_subset_titles = []
large_subset_titles = []

small_subset_descriptions = []
medium_subset_descriptions = []
large_subset_descriptions = []

all_obj = []
all_tags = []
all_titles = []
all_descriptions = []


def cell_splitter(cell):
        cell = cell.strip()
        split_cell = cell.split(" ")
        items_of_cell = [int(x) for x in split_cell[1:]]
        # print(items_of_cell)
        return items_of_cell

for i in range(0, 5):
    df = pd.read_csv(FILE_NAME + str(i), header=None, sep="|")

    df = df.iloc[:, 0:4]  # last column is NAN always so omit it
    # print(df.head())

    obj_column = df[0]
    tags_column = df[2]
    title_column = df[1]
    description_column = df[3]
    # print(all_tags.head())

    for obj, tags, title, description in zip(obj_column, tags_column, title_column, description_column):
        """
        1. obj_id = cell_splitter(obj)
        because cell_splitter cast to int it not work for obj ids
        the format of the list that contain obj_id is like ['BglyyN8YjWg','v0eWb_2CCGw',...]
        not like other ones [['BglyyN8YjWg'],['v0eWb_2CCGw'],...]

        """
        obj = obj.strip()
        split_obj = obj.split(" ")
        obj_id = split_obj[1]
        all_obj.append(obj_id)

        """ 1. """

        tag_numbers = cell_splitter(tags)
        all_tags.append(tag_numbers)

        title_numbers = cell_splitter(title)
        all_titles.append(title_numbers)

        description_numbers = cell_splitter(description)
        all_descriptions.append(description_numbers)

        """ 2. partition to small set , medium set and large set using the boundary define in top """
        if small_down_boundary <= len(tag_numbers) < medium_down_boundary:
            small_subset_tags.append(tag_numbers)
            small_subset_titles.append(title_numbers)
            small_subset_descriptions.append(description_numbers)
            small_subset_obj.append(obj_id)

        if medium_down_boundary <= len(tag_numbers) < large_down_boundary:
            medium_subset_tags.append(tag_numbers)
            medium_subset_titles.append(title_numbers)
            medium_subset_descriptions.append(description_numbers)
            medium_subset_obj.append(obj_id)

        if large_down_boundary <= len(tag_numbers) <= up_boundary:
            large_subset_tags.append(tag_numbers)
            large_subset_titles.append(title_numbers)
            large_subset_descriptions.append(description_numbers)
            large_subset_obj.append(obj_id)
        """ 2. """


# #############  sample from each partition ############## #

def get_sample_3d(data1,data2,data3, data4,sample_size):
    idx = np.random.choice(np.arange(len(data1)), sample_size, replace=False)
    sample_data1 = [data1[j] for j in idx]
    sample_data2 = [data2[j] for j in idx]
    sample_data3 = [data3[j] for j in idx]
    sample_data4 = [data4[j] for j in idx]
    return sample_data1, sample_data2, sample_data3, sample_data4

small_tags_sample, small_titles_sample, small_descriptions_sample, small_obj_sample = get_sample_3d(small_subset_tags
                                                                                  , small_subset_titles
                                                                                  , small_subset_descriptions
                                                                                  , small_subset_obj
                                                                                  , 20000)

med_tags_sample, med_titles_sample, med_descriptions_sample, med_obj_sample = get_sample_3d(medium_subset_tags
                                                                            , medium_subset_titles
                                                                            , medium_subset_descriptions
                                                                            , medium_subset_obj
                                                                            , 20000)

large_tags_sample, large_titles_sample, large_descriptions_sample, large_obj_sample = get_sample_3d(large_subset_tags
                                                                                  , large_subset_titles
                                                                                  , large_subset_descriptions
                                                                                  , large_subset_obj
                                                                                  , 20000)


del small_subset_tags,medium_subset_tags,large_subset_tags
del small_subset_titles,medium_subset_titles,large_subset_titles
del small_subset_descriptions,medium_subset_descriptions,large_subset_descriptions

##############  creat test and train set 1/5 data going to test and 1/5 going to validation and 3/5 for train ########## block2


def get_Test_Tarin_Collection(data):
    test_collection = data[:int(len(data)/5)]
    validation_collection = data[int(len(data)/5):2*(int(len(data)/5))]
    train_collection= data[2*(int(len(data)/5)):]
    return train_collection, test_collection, validation_collection

smallSetTrain_tag, smallSetTest_tag, smallSetValidation_tag = get_Test_Tarin_Collection(small_tags_sample)
smallSetTrain_title, smallSetTest_title, smallSetValidation_title = get_Test_Tarin_Collection(small_titles_sample)
smallSetTrain_desc, smallSetTest_desc, smallSetValidation_desc = get_Test_Tarin_Collection(small_descriptions_sample)
smallSetTrain_obj, smallSetTest_obj, smallSetValidation_obj = get_Test_Tarin_Collection(small_obj_sample)


mediumSetTrain_tag, mediumSetTest_tag, mediumSetValidation_tag = get_Test_Tarin_Collection(med_tags_sample)
mediumSetTrain_title, mediumSetTest_title, mediumSetValidation_title = get_Test_Tarin_Collection(med_titles_sample)
mediumSetTrain_desc, mediumSetTest_desc, mediumSetValidation_desc = get_Test_Tarin_Collection(med_descriptions_sample)
mediumSetTrain_obj, mediumSetTest_obj, mediumSetValidation_obj = get_Test_Tarin_Collection(med_obj_sample)


largeSetTrain_tag, largeSetTest_tag, largeSetValidation_tag = get_Test_Tarin_Collection(large_tags_sample)
largeSetTrain_title, largeSetTest_title, largeSetValidation_title = get_Test_Tarin_Collection(large_titles_sample)
largeSetTrain_desc, largeSetTest_desc, largeSetValidation_desc = get_Test_Tarin_Collection(large_descriptions_sample)
largeSetTrain_obj, largeSetTest_obj, largeSetValidation_obj = get_Test_Tarin_Collection(large_obj_sample)


del small_tags_sample
del med_tags_sample
del large_tags_sample


def golden_reformat(collection):

    testSet = []
    testSetExpected = []
    for t in collection:
        random.shuffle(t)
        testSet.append(t[:int(len(t)/2)])
        testSetExpected.append(t[int(len(t)/2):])
    return testSet, testSetExpected

smallSetTest_tag, smallSetTest_tag_expected = golden_reformat(smallSetTest_tag)
mediumSetTest_tag, mediumSetTest_tag_expected = golden_reformat(mediumSetTest_tag)
largeSetTest_tag, largeSetTest_tag_expected = golden_reformat(largeSetTest_tag)

smallSetValidation_tag, smallSetValidation_tag_expected = golden_reformat(smallSetValidation_tag)
mediumSetValidation_tag, mediumSetValidation_tag_expected = golden_reformat(mediumSetValidation_tag)
largeSetValidation_tag, largeSetValidation_tag_expected = golden_reformat(largeSetValidation_tag)

import pickle

pickle_file = 'train.pickle'

try:
    f = open(pickle_file, 'wb')
    save = {
        'smallSetTrain_tag': smallSetTrain_tag,
        'smallSetTrain_title': smallSetTrain_title,
        'smallSetTrain_desc': smallSetTrain_desc,
        'smallSetTrain_obj': smallSetTrain_obj,

        'mediumSetTrain_tag': mediumSetTrain_tag,
        'mediumSetTrain_title': mediumSetTrain_title,
        'mediumSetTrain_desc': mediumSetTrain_desc,
        'mediumSetTrain_obj': mediumSetTrain_obj,

        'largeSetTrain_tag': largeSetTrain_tag,
        'largeSetTrain_title': largeSetTrain_title,
        'largeSetTrain_desc': largeSetTrain_desc,
        'largeSetTrain_obj': largeSetTrain_obj,


        }
    pickle.dump(save, f, pickle.HIGHEST_PROTOCOL)
    f.close()
except Exception as e:
    print('Unable to save data to', pickle_file, ':', e)
    raise

del smallSetTrain_tag, smallSetTrain_title, smallSetTrain_desc
del mediumSetTrain_tag, mediumSetTrain_title, mediumSetTrain_desc
del largeSetTrain_tag, largeSetTrain_title, largeSetTrain_desc


pickle_file = 'test.pickle'

try:
    f = open(pickle_file, 'wb')
    save = {
        'smallSetTest_tag': smallSetTest_tag,
        'smallSetTest_tag_expected': smallSetTest_tag_expected,
        'smallSetTest_title': smallSetTest_title,
        'smallSetTest_desc': smallSetTest_desc,
        'smallSetTest_obj': smallSetTest_obj,



        'mediumSetTest_tag': mediumSetTest_tag,
        'mediumSetTest_tag_expected': mediumSetTest_tag_expected,
        'mediumSetTest_title': mediumSetTest_title,
        'mediumSetTest_desc': mediumSetTest_desc,
        'mediumSetTest_obj': mediumSetTest_obj,


        'largeSetTest_tag': largeSetTest_tag,
        'largeSetTest_tag_expected': largeSetTest_tag_expected,
        'largeSetTest_title': largeSetTest_title,
        'largeSetTest_desc': largeSetTest_desc,
        'largeSetTest_obj': largeSetTest_obj,

        }
    pickle.dump(save, f, pickle.HIGHEST_PROTOCOL)
    f.close()
except Exception as e:
    print('Unable to save data to', pickle_file, ':', e)
    raise

del smallSetTest_tag, smallSetTest_tag_expected, mediumSetTest_tag, mediumSetTest_tag_expected, largeSetTest_tag
del largeSetTest_tag_expected

pickle_file = 'validation.pickle'

try:
    f = open(pickle_file, 'wb')
    save = {
        'smallSetValidation_tag': smallSetValidation_tag,
        'smallSetValidation_tag_expected': smallSetValidation_tag_expected,
        'smallSetValidation_title': smallSetValidation_title,
        'smallSetValidation_desc': smallSetValidation_desc,
        'smallSetValidation_obj': smallSetValidation_obj,

        'mediumSetValidation_tag': mediumSetValidation_tag,
        'mediumSetValidation_tag_expected': mediumSetValidation_tag_expected,
        'mediumSetValidation_title': mediumSetValidation_title,
        'mediumSetValidation_obj': mediumSetValidation_obj,

        'largeSetValidation_tag': largeSetValidation_tag,
        'largeSetValidation_tag_expected': largeSetValidation_tag_expected,
        'largeSetValidation_title': largeSetValidation_title,
        'largeSetValidation_obj': largeSetValidation_obj,
        }
    pickle.dump(save, f, pickle.HIGHEST_PROTOCOL)
    f.close()
except Exception as e:
    print('Unable to save data to', pickle_file, ':', e)
    raise