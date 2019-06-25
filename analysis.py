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

# Counts how many bad emojis are in transaction text
def emoji_counter(clean):
	ALCOHOL_ALIAS = ["tropical_drink", "wine_glass", "beer", "cocktail", "beers", "sake"]
	DRUG_ALIAS = ["smoking", "no_smoking", "pill", "dash", "leaves", "mushroom", "ear_of_rice"]

	# running the emoji functions on these aliases
	alcohol_emojis = alias_translator(ALCOHOL_ALIAS)
	drug_emojis = alias_translator(DRUG_ALIAS)

	# Making a masterlist of sinful emojis
	ILLICIT_EMOJIS = alcohol_emojis + drug_emojis

	count = 0

	for character in clean:
		if character in ILLICIT_EMOJIS:
			count += 1
	return count


def phrase_counter(clean):
	# Lists of presumably bad words and their synonyms
	ALCOHOL_PHRASES = ["alc", "alcohol", "bubbly", "champagne", "drinks", "beer", "bud", "drank"]
	DRUG_PHRASES = ["weed", "pills", "ecstasy", "broccoli", "plug", "codeine", 
	"high", "buzzed", "stoned", "420", "smoke", "popper"]
	VAPE_PHRASES = ["pods", "pod", "juul", "suorin", "vape", "vaping", "vape"]
	BAD_BOIS = ALCOHOL_PHRASES + DRUG_PHRASES + VAPE_PHRASES

	count = 0 # Tally up how many sinful terms are in the transaction text list
	for word in clean:
		if word in BAD_BOIS:
			count += 1

	return count


# Takes in a cleaned list and apply all analysis functions to it
def analysis(clean_list):
	# Summing up the shadiness of the individual
	BAD_EMOJIS = emoji_counter(clean_list)
	BAD_WORDS = phrase_counter(clean_list)

	TOTAL_SIN = BAD_EMOJIS + BAD_WORDS
	return TOTAL_SIN 


