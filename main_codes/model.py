__author__ = 'ahmaddorri'

from main_codes import get_input, LATRE, parameter_cal

import time
start_time = time.time()

validation_set_object, validation_set_tag, validation_set_tag_expected, validation_set_title, validation_set_description = get_input.validation_set("SMALL")
train_set_objects, train_set_tag, train_set_title, train_set_description =get_input.train_set("SMALL")

print(validation_set_tag_expected[0:10])
def compute_param_vector(candidate_tag, initial_tag,l=1,train_set_tag=None,kx=1,kc=1,kr=1,obj_id=None,object_set=None,title_set=None,description_set=None):
    sum_val1 = parameter_cal._sum(candidate_tag,initial_tag,l=l,train_set_tags=train_set_tag)
    sum_val2 = parameter_cal._sum(candidate_tag,initial_tag,l=l,train_set_tags=train_set_tag)
    sum_plus = parameter_cal.sum_plus(candidate_tag,initial_tag,kx,kc,kr,l,train_set=train_set_tag)
    vote_plus = parameter_cal.vote_plus(candidate_tag,initial_tag,kx,kc,kr,train_set_tag)

    ts = parameter_cal.ts_know_values(candidate_tag,obj_id,object_set,title_set,description_set)
    wts = parameter_cal.wts(candidate_tag,obj_id,object_set,title_set,description_set)


def generate_candidates(initial_tag, train_set_tag):
    return LATRE.get_candidate_tag([initial_tag], train_set_tag, confidence_min=0.01, sup_min=2)


def model(part_num, step_size):

    l1 = part_num*step_size
    l2 = (part_num+1)*step_size
    all_vectors = []
    j = l1 - 1
    for obj, initial_tag,expected, title, desc in zip(validation_set_object[l1:l2],
                                                      validation_set_tag[l1:l2],
                                                      validation_set_tag_expected[l1:l2],
                                                      validation_set_title[l1:l2],
                                                      validation_set_description[l1:l2]):
        candidates_pair = generate_candidates(initial_tag,train_set_tag)
        j += 1
        print(j,".......",candidates_pair)
        for c in candidates_pair:
            # vec = compute_param_vector(c[0], initial_tag, l=1,train_set_tag=train_set_tag,kx=1,kc=1, kr=1, obj_id=obj,
            #                            object_set=train_set_objects, title_set=train_set_title,
            #                            description_set=train_set_description)

            sum_val1 = parameter_cal._sum(c[0],initial_tag,l=1,train_set_tags=train_set_tag)
            sum_val2 = parameter_cal._sum(c[0],initial_tag,l=3,train_set_tags=train_set_tag)
            sum_plus_value = parameter_cal.sum_plus(c[0],initial_tag,kx=1,kc=1,kr=1,l=1,train_set=train_set_tag)
            vote = parameter_cal.vote(c[0],initial_tag,train_set=train_set_tag)
            vote_plus_value = parameter_cal.vote_plus(c[0],initial_tag,kx=1,kc=1,kr=1,train_set=train_set_tag)
            ts = parameter_cal.ts_know_values(c[0],title,desc)
            wts = parameter_cal.wts_know_values(c[0],title,desc,train_set_objects,train_set_title,train_set_description)
            tf = parameter_cal.tf(c[0],title,desc)
            wtf_value = parameter_cal.wtf(c[0],title,desc,train_set_objects,train_set_title,train_set_description)
            iff_value = parameter_cal.iff(c[0],train_set_tag)
            stab_value = parameter_cal.stab(c[0], k=1, training_set=train_set_tag)
            vec = (sum_val1,sum_val2, sum_plus_value, vote, vote_plus_value, ts, wts, tf, wtf_value, iff_value, stab_value)

            if c[0] in expected:
                all_vectors.append((1,c[0],(vec),obj))
                print("lable 1 :")
                print(all_vectors[len(all_vectors)-1])

            else:
                all_vectors.append((0,c[0],(vec),obj))

            if wts >0 or ts > 0:
                print("wts or ts > 0 :")
                print(all_vectors[len(all_vectors)-1])


            #print(all_vectors[len(all_vectors)-1])
    # print(all_vectors[0:10])
    print("--- %s seconds ---" % (time.time() - start_time))
    file_path = "outputs/out"+str(part_num)+".txt"
    text_file = open(file_path, "w")
    for vec in all_vectors:
        text_file.write(str(vec[0]))
        text_file.write(" qid:")
        text_file.write(str(vec[1]))
        i = 0
        for v in vec[2]:
            i += 1
            text_file.write(" ")
            text_file.write(str(i))
            text_file.write(":")
            text_file.write(str(v))
        text_file.write(" #")
        text_file.write(str(vec[3]))

        text_file.write("\n")
    text_file.close()


model(26,100)
model(27,100)
