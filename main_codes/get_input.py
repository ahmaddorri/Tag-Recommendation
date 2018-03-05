__author__ = 'ahmaddorri'


import pickle


def train_set(partition):
    pickle_file = 'train.pickle'
    with open(pickle_file, 'rb') as f:
        save = pickle.load(f)
        if partition == "SMALL":
            train_set_tag = save['smallSetTrain_tag']
            train_set_title = save['smallSetTrain_title']
            train_set_description = save['smallSetTrain_desc']
            train_set_objects = save['smallSetTrain_obj']


        if partition == "MEDIUM":
            train_set_tag = save['mediumSetTrain_tag']
            train_set_title = save['mediumSetTrain_title']
            train_set_description = save['mediumSetTrain_desc']
            train_set_objects = save['mediumSetTrain_obj']



        if partition == "LARGE":
            train_set_tag = save['largeSetTrain_tag']
            train_set_title = save['largeSetTrain_title']
            train_set_description = save['largeSetTrain_desc']
            train_set_objects = save['largeSetTrain_obj']


        del save  # hint to help gc free up memory
    return train_set_objects, train_set_tag, train_set_title, train_set_description

def test_set(partition):

    pickle_file = 'test.pickle'
    with open(pickle_file, 'rb') as f:
        save = pickle.load(f)
        if partition == "SMALL":
            test_set_tag = save['smallSetTest_tag']
            test_set_tag_expected = save['smallSetTest_tag_expected']
            test_set_title = save['smallSetTest_title']
            test_set_description = save['smallSetTest_desc']
            test_set_objects = save['smallSetTest_obj']

        if partition == "MEDIUM":
            test_set_tag = save['mediumSetTest_tag']
            test_set_tag_expected = save['mediumSetTest_tag_expected']
            test_set_title = save['mediumSetTest_title']
            test_set_description = save['mediumSetTest_desc']
            test_set_objects = save['mediumSetTest_obj']

        if partition == "LARGE":
            test_set_tag = save['largeSetTest_tag']
            test_set_tag_expected = save['largeSetTest_tag_expected']
            test_set_title = save['largeSetTest_title']
            test_set_description = save['largeSetTest_desc']
            test_set_objects = save['largeSetTest_obj']

        del save  # hint to help gc free up memory
    return test_set_objects, test_set_tag, test_set_tag_expected, test_set_title, test_set_description

def validation_set(partition):

    pickle_file = 'validation.pickle'
    with open(pickle_file, 'rb') as f:
        save = pickle.load(f)
        if partition == "SMALL":
            validation_set_tag = save['smallSetValidation_tag']
            validation_set_tag_expected = save['smallSetValidation_tag_expected']
            validation_set_title = save['smallSetValidation_title']
            validation_set_description = save['smallSetValidation_desc']
            validation_set_object = save['smallSetValidation_obj']

        if partition == "MEDIUM":
            validation_set_tag = save['mediumSetValidation_tag']
            validation_set_tag_expected = save['mediumSetValidation_tag_expected']
            validation_set_title = save['mediumSetValidation_title']
            validation_set_description = save['mediumSetValidation_desc']
            validation_set_object = save['mediumSetValidation_obj']

        if partition == "LARGE":
            validation_set_tag = save['largeSetValidation_tag']
            validation_set_tag_expected = save['largeSetValidation_tag_expected']
            validation_set_title = save['largeSetValidation_title']
            validation_set_description = save['largeSetValidation_desc']
            validation_set_object = save['largeSetValidation_obj']


        del save  # hint to help gc free up memory
    return validation_set_object, validation_set_tag, validation_set_tag_expected, validation_set_title, validation_set_description