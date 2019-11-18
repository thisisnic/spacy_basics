# Why not just match based on regex?
#  Compared to regular expressions, the matcher works with Doc and Token objects instead of only strings.
#  It's also more flexible: you can search for texts but also other lexical attributes.
#  You can even write rules that use the model's predictions.
#  For example, find the word "duck" only if it's a verb, not a noun.

# We can match on exact token texts:
# [{'TEXT': 'iPhone'}, {'TEXT': 'X'}]

# or match on lexical attributes, e.g. two tokens whose lowercase forms are "iphone" and "x"
# [{'LOWER': 'iphone'}, {'LOWER': 'x'}]

# we can also match based on attributes predicted by the model

# [{'LEMMA': 'buy'}, {'POS

import spacy

# Import the Matcher
from spacy.matcher import Matcher

# Load a model and create the nlp object
nlp = spacy.load('en_core_web_sm')

# Initialize the matcher with the shared vocab
matcher = Matcher(nlp.vocab)

# Add the pattern to the matcher
pattern = [{'TEXT': 'iPhone'}, {'TEXT': 'X'}]

# The parameters here are:
# 1) a unique ID to identify which pattern is matched
# 2) an optional callback
# 3) the pattern itself
matcher.add('IPHONE_PATTERN', None, pattern)

# Process some text
doc = nlp("New iPhone X release date leaked")

# Call the matcher on the doc
matches = matcher(doc)

# The matcher returns a list of tuples.  Each tuple consists of three values:
# 1) the match ID
# 2) the start index
# 3) the end index of the matched span.

# This means we can iterate over the matches and create a Span object: a slice of the doc at the start and end index.

# Call the matcher on the doc
doc = nlp("New iPhone X release date leaked")
matches = matcher(doc)


# When you call the matcher on a doc, it returns a list of tuples.
# Each tuple consists of three values: the match ID, the start index and the end index of the matched span.
# This means we can iterate over the matches and create a Span object: a slice of the doc at the start and end index.

# Iterate over the matches
for match_id, start, end in matches:
    # Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)

# Here's an example of a more complex pattern using lexical attributes.
# We're looking for five tokens:
# A token consisting of only digits.
# Three case-insensitive tokens for "fifa", "world" and "cup".
# And a token that consists of punctuation.
# The pattern matches the tokens "2018 FIFA World Cup:".

pattern = [
    {'IS_DIGIT': True},
    {'LOWER': 'fifa'},
    {'LOWER': 'world'},
    {'LOWER': 'cup'},
    {'IS_PUNCT': True}
]

doc = nlp("2018 FIFA World Cup: France won!")

matcher.add('WORLDCUP_PATTERN', None, pattern)

matches = matcher(doc)

matches

# We can also match other token attributes

love_pattern = [
    {'LEMMA': 'love', 'POS': 'VERB'},
    {'POS': 'NOUN'}
]

catdogdoc = nlp("I loved dogs but now I love cats more.")

matcher.add('LOVE_PATTERN', None, love_pattern)

matches = matcher(catdogdoc)

# We can use operators and quantifiers too

# Operators and quantifiers let you define how often a token should be matched. They can be added using the "OP" key.
# Here, the "?" operator makes the determiner token optional, so it will match a token with the lemma "buy",
# an optional article and a noun.

# "OP" can have one of four values:
#
# An "!" negates the token, so it's matched 0 times.
#
# A "?" makes the token optional, and matches it 0 or 1 times.
#
# A "+" matches a token 1 or more times.
#
# And finally, an "*" matches 0 or more times.
#
# Operators can make your patterns a lot more powerful, but they also add more complexity – so use them wisely.

buy_pattern = [
    {'LEMMA': 'buy'},
    {'POS': 'DET', 'OP': '?'},  # optional: match 0 or 1 times
    {'POS': 'NOUN'}
]

phone_doc = nlp("I bought a smartphone. Now I'm buying apps.")

matcher.add('BUY_PATTERN', None, buy_pattern)

matches = matcher(phone_doc)
