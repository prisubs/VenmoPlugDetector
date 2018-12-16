# These scripts will form an analysis of a user's Venmo activity.
# Final output should be a whole number percentage, casted to String.

# Emoji functionality
import emoji

# Function that outputs a list of emoji objects, takes in a list of alias strings
def alias_translator(aliases):
	results = []
	BASE = ":"

	for alias in aliases:
		# The emojize function looks up an emoji by an english alias
		emo_boi = emoji.emojize(BASE + alias + BASE)
		# Creating a list of emoji objects
		results.append(emo_boi)

	return results

ALCOHOL_ALIAS = ["tropical_drink", "wine_glass", "beer", "cocktail", "beers", "sake"]
DRUG_ALIAS = ["smoking", "no_smoking", "pill", "dash", "leaves", "mushroom", "ear_of_rice"]

# running the emoji functions on these aliases
alcohol_emojis = alias_translator(ALCOHOL_ALIAS)
drug_emojis = alias_translator(DRUG_ALIAS)

# Making a masterlist of sinful emojis
ILLICIT_EMOJIS = alcohol_emojis + drug_emojis


