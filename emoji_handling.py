import emoji

BAD_ALIASES = ["tropical_drink", "wine_glass", "beer", "cocktail",
               "beers", "sake", "smoking", "no_smoking", "pill", "dash",
               "leaves", "mushroom", "ear_of_rice"]


'''
[INPUT] original, unicode-encoded payment text
[OUTPUT] demojized, split array to perform counts on
'''
def process_text(text):
    text = emoji.demojize(text)
    text = text.split(" ")
    return text

'''
[INPUT] original, unicode-encoded payment text
[OUTPUT] ratio of emojis to characters in the text
'''
def emoji_ratio(text):
    text = process_text(text)
    total_count = 0
    for alias in BAD_ALIASES:
        if alias in text:
            total_count += 1
    return total_count/len(text)


'''
[INPUT] original, unicode-encoded payment text
[OUTPUT] 0 or 1 indicating presence of a bad emoji
'''
def emoji_ohe(text):
    text = process_text(text)
    for alias in BAD_ALIASES:
        if text.count(alias) > 0:
            return True
    return False
