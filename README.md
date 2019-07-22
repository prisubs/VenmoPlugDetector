# VenmoPlugDetector
Related article [here](https://medium.com/@prisubs/where-to-find-the-drug-dealers-ee6cbc48ab66).
<br>
<br>
Training data was pulled from [Vicemo](https://vicemo.com) and my own personal feed. The ratings are determined by a Naive Bayesian Classifier, as opposed to a logistic regression model, to accommodate the small training set. Additionally, there's support to count Unicode emojis in the calculations, thanks to the [emoji](https://pypi.org/project/emoji/) library for Python.
