import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB

import _pickle as cPickle

bag_of_words = ["alc", "alcohol", "bubbly", "champagne", "drinks", "beer", "bud", "drank", "weed", "pills", "ecstasy", "broccoli", "plug", "codeine", "high", "buzzed", "stoned", "420", "smoke", "popper", "pods", "pod", "juul", "suorin", "vape", "vaping", "vape"]

bad_fp = "data/illicit.txt"
good_fp = "data/clean.txt"

MODEL_FP = "bayesianNB.pkl"

'''
[INPUT] list of unlabeled observations
[OUTPUT] list of data to render on website
'''
def unlabeled_runner(observations):
	features = bow_featurizer(observations)
	model = retrieve_model(MODEL_FP)
	predictions = model.predict(features)
	return predictions

'''
[INPUT] filepath to where model should be pickled
[OUTPUT] none, writes a pickled logistic regression model
'''
def model_runner(filepath):
	df = read_training_data(bad_fp, good_fp)
	X, Y = training_pipeline(df)
	model = generate_model(X, Y)
	write_model(model, filepath)

'''
[INPUT] filepaths of illicit and clean newline-delimited training data
[OUTPUT] dataframe containing payment texts and labels
'''
def read_training_data(bad_filepath, good_filepath):
	bad_data = pd.read_csv(bad_filepath, sep="\n", header=None)
	good_data = pd.read_csv(good_filepath, sep="\n", header=None)
	bad_data["label"] = pd.Series([1] * len(bad_data))
	good_data["label"] = pd.Series([0] * len(good_data))

	df = pd.concat([bad_data, good_data])
	df = df.rename({0: "payment_text"}, axis=1)
	return df

'''
[INPUT] labeled, textual training data
[OUTPUT] train_test split data ready to be put into a model
'''
def training_pipeline(labeled_data):
	X = bow_featurizer(labeled_data["payment_text"])
	Y = labeled_data["label"]
	return X, Y

'''
[INPUT] list of payment texts
[OUTPUT] bag of words, transposed and returned as a df
'''
def bow_featurizer(payment_text_array):
	vectorizer = CountVectorizer()
	vectorizer.fit(bag_of_words)
	bow_ohe = vectorizer.transform(payment_text_array).toarray()

	features = pd.DataFrame(bow_ohe)
	return features

'''
[INPUT] list of payment box texts from scraping.py
[OUTPUT] feature matrix to run model.predict() on
'''
def testing_pipeline(unlabeled_data):
	feature_matrix = bow_featurizer(unlabeled_data)
	return feature_matrix

'''
[INPUT] feature matrix with labels
[OUTPUT] sklearn Model object to be serialized
'''
def generate_model(X_train, Y_train):
	model = GaussianNB()
	model.fit(X_train, Y_train)
	return model

'''
[INPUT] filepath to a serialized model
[OUTPUT] a model to use for predicting on unlabeled data
'''
def retrieve_model(filepath):
	with open(filepath, 'rb') as fid:
		model_loaded = cPickle.load(fid)
	return model_loaded

'''
[INPUT] sklearn Model object to be pickled, filepath to pickle
[OUTPUT] none
[EFFECT] writes a serialized model to specified filepath
'''
def write_model(model, fp):
	with open(fp, 'wb') as fid:
		cPickle.dump(model, fid)


bad_aliases = ["tropical_drink", "wine_glass", "beer", "cocktail", "beers", "sake", "smoking", "no_smoking", "pill", "dash", "leaves", "mushroom", "ear_of_rice"]
model_runner(MODEL_FP)



