import re
import nltk
#import spacy
from string import punctuation
from getTranscript import get_transcript

# summarizer based on Frequency of words
def nltk_summerizer(treanscript, percent=30):
    
    from nltk.corpus import stopwords # stopwords to remove from sentences
    from nltk.tokenize import word_tokenize, sent_tokenize # to divide text into sentences and words
    from nltk.probability import FreqDist # to get the frequency of each word
    from heapq import nlargest # to get the first n number of elements with largest values from a list

    stop_words = nltk.corpus.stopwords.words('english')
    tokens = word_tokenize(treanscript)
    tokens = [token.lower() for token in tokens if token not in punctuation and token not in stop_words]
    freq = FreqDist(tokens)
    max_freq = max(freq.values())

    # normalize the frequencies
    for word in freq.keys():
        freq[word] = (freq[word]/max_freq)

    # score each sentence depending on the words it contains and the frequency of each word
    sent_tokens = sent_tokenize(treanscript)
    
    # create a dictionary to hold the score of each sentence
    sent_scores = {}
    for sent in sent_tokens:
        sentence = sent.split(" ")
        for word in sentence:
            if word.lower() in freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = freq[word.lower()]
                else:
                    sent_scores[sent] += freq[word.lower()]

    select_length = int(len(sent_tokens) * (int(percent) / 100))
    # get the 10 sentences with the highest scores
    #summary_sents = nlargest(10, sent_scores, key=sent_scores.get)
    summary_sents = nlargest(select_length, sent_scores, key=lambda x: sent_scores[x])
    summary = ' '.join(summary_sents)
    return summary 



def clean_transcript(transcript):
    # Remove timestamps
    cleaned_transcript = re.sub(r'\d{1,2}:\d{2}', '', transcript)
    # Remove additional details
    cleaned_transcript = re.sub(r'\([^)]*\)', '', cleaned_transcript)
    # Remove -- from the transcript
    cleaned_transcript = cleaned_transcript.replace('--', '')

    return cleaned_transcript


# arj7oStGLkU 
summey = nltk_summerizer(clean_transcript(get_transcript("arj7oStGLkU")))
print(summey)
#temp()