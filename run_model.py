from analysis import *
from scraping import *
from pandas import Series

def generate_output(username):
    payment_text = payment_box_list(username)
    predictions = unlabeled_runner(payment_text)

    print(payment_text)
    print(predictions)

    if sum(predictions) == 0:
        pmt_conclusion = "{0} probably isn't up to anything shady.".format(username)
        p1 = payment_text[0].lower()
        p2 = payment_text[1].lower()
        pmt_recent = "They recently paid for {0} and {1}.".format(p1, p2)
    else:
        bad_payments = extract_bad(payment_text, predictions)
        bad_payments = format_unknown_length(bad_payments)
        pmt_conclusion = "{0} might be up to something!".format(username)
        pmt_recent = "We found {0}.".format(bad_payments)

    return pmt_conclusion, pmt_recent

def extract_bad(pmts, predictions):
    res = []
    for i in range(len(predictions)):
        if predictions[i] == 1:
            res.append(pmts[i])
    return res

def format_unknown_length(strings):
    result = ""
    for s in strings:
        s = s.lower()
        result += "{0}, ".format(s)
    return result[0:-2]
