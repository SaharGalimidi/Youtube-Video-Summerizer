import spacy
from transformers import pipeline

nlp = spacy.load('en_core_web_sm')
summarizer1 = pipeline('summarization')
summarizer2 = pipeline('summarization', model='t5-base', tokenizer='t5-base')
summarizer3 = pipeline('summarization', model='facebook/bart-large-cnn', tokenizer='facebook/bart-large-cnn')
summarizer4 = pipeline('summarization', model='google/pegasus-xsum', tokenizer='google/pegasus-xsum')

def summary1(text):
    summary = summarizer1(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def summary2(text):
    summary = summarizer2(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def summary3(text):
    summary = summarizer3(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def summary4(text):
    summary = summarizer4(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']


def compare_summaries(text):
    summaries = [summary1(text), summary2(text), summary3(text), summary4(text)]
    scores = []
    for summary in summaries:
        doc1 = nlp(summary)
        doc2 = nlp(text)
        score = doc1.similarity(doc2)
        scores.append(score)
    ranked_summaries = [x for _, x in sorted(zip(scores, summaries), reverse=True)]
    return ranked_summaries