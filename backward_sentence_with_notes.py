# Daniel Austin
# Begin Date: 6/14/2016
# Last Update: 6/14/2016


# This program takes a user provided sentence and returns it backwards
# letter by letter.
#
# For Example: "One two three." returns ".eerht owt enO"



# Into text, then User provides any sentence

print """
This program takes a user provided sentence and returns it backwards
letter by letter.

For Example: "One two three." returns ".eerht owt enO"

Let's begin:

"""

sentence = raw_input("Type any sentence here: ")

# Sentence is turned into a list to work with.

split_sentence = sentence.split()

# Words are taken from the split_sentence list and appended to backward_list
# in reverse order.

backward_list = []
for i in range(0, len(split_sentence)):
	popped_word = split_sentence.pop()
	backward_list.append(popped_word)

# This is the meat of the program. Step 1: The first word in the backwards
# list is examined. We run through the index of this word in reverse order
# and append each letter to a new list, called backwards_word since the letters
# are now backwards. Because this is a list we must now (join) the list to
# create a backwards word, here called joined_word. This backwards word is then
# appended to a second list holding all of the backwards words. After the first
# word we examine the second, split its letters in reverse, append them to a
# list, join the list, and again add the now-backwards word to our final list.
# We iterate this process for all words in our backwards_list.

backwards_words_list = []
for word in backward_list:
	backwards_word = []
	for i in range(0, len(word)):
		backwards_word.append(word[-1 - i])
	joined_word = ''.join(backwards_word)
	backwards_words_list.append(joined_word)

# Finally, we take our list of backwards words, join them using the ' ', and
# BINGO! The sentence has been reveresed. Now...

fully_backwards_sentence = ' '.join(backwards_words_list)

# ... to print the final product!

print fully_backwards_sentence
