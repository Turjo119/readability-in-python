from cs50 import get_string

# Function to count total number of letters
def count_letters(n, string):
    # Counter for letters
    l = 0
    for i in range(0, n, 1):
        if str.isalpha(string[i]):
            l += 1

    return l

# Count for total number of words
def count_words(n, string):
    #Counter for words
    w = 0
    if str.isalpha(string[0]):
        w += 1

    for j in range (0, n, 1):
        if str.isspace(string[j]):
            w += 1

# Function to count total number of sentences
def count_sentences(n, string):
    # Counter for sentences
    s = 0
    for k in range(0, n, 1):
         if string[k] == '.' or string[k] == '!' or string[k] == '?':
             s += 1
    return s

# Enter text
text = get_string("Text: ")
# Length of text
t = len(text)

#Pass through function that counts total number of letters
count_letters(t,text)

#Pass through function that counts the total number of words
count_words(t, text)

# Pass through function that counts the total number of sentences
count_sentences(t, text)

#Average letters per 100 words
L = (count_letters(t,text) / count_words(t,text)) * 100

#Average sentences per 100 words
S = (count_sentences(t,text) / count_words(t,text)) * 100

#Coleman-Liau index
CLI = int(0.0588 * L - 0.296 * S - 15.8)

# Determine reading level
if CLI < 1:
    print("Before Grade 1")

elif CLI >= 1 and CLI <= 16:
    print(f"Grade {CLI}")

else:
    print("Grade 16+")
