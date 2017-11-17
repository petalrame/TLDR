"""
Tokenizes, queues, summarizes, and formats the content passed here.
"""
import sys
import os
import nltk
from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tokenize.moses import MosesDetokenizer
from .models import Event
from summarize.pgmodel import run_summarization

# Status: In Progress
# TODO: Get better summ model

def tokenize(content):
    """Breaks up text-based content into tokens in the style of PTB corpus"""
    _path_to_jar = os.path.abspath(
        'summarize/stanford-postagger/stanford-postagger.jar')
    token_list = []
    st = StanfordTokenizer(path_to_jar=_path_to_jar)
    content = content.lower()
    token_list = st.tokenize(content)
    return token_list


def format_summary(token_list):
    """
    Converts a token_list into human readble format
    Args: token_list(a list/sequence of tokens)
    Returns: A content string
    """
    #Replaces any instance of -LRB- and -RRB- with '(' and ')' respectively
    for idx, tok in enumerate(token_list):
        if tok == '-LRB-':
            token_list[idx] = '('
        elif tok == '-RRB-':
            token_list[idx] = ')'

    detokenizer = MosesDetokenizer()
    summary = detokenizer.detokenize(token_list, return_str=True)
    sentences = nltk.sent_tokenize(summary)
    summary = ' '.join([s.replace(s[0], s[0].capitalize(), 1)
                        for s in sentences])
    return summary


def feed_model(token_list):
    """
    Feeds token_list to model with hard-coded parameters
    """
    summarized_tokens = run_summarization.article_summary(token_list)
    return summarized_tokens


def run_summary(article):
    """Takes events that need a summary and returns summarized content"""
    # Get the dictionary of articles that needs a summary
    # process article(tokenize, feed and format)
    token_list = tokenize(article)
    if len(token_list) < 30:
        return format_summary(token_list)
    summ_token = feed_model(token_list)
    summary = format_summary(summ_token)
    return summary


def test():
    "Tests tokenization, summarization and formating"
    f = open('test_article.txt', 'r')
    article = f.read()
    print('Original Article: %s', article)
    tokenized_article = tokenize(article)
    summarized_tok = feed_model(tokenized_article)
    print(summarized_tok)
    summary = format_summary(summarized_tok)
    print('Summarized Article: ', summary)


if __name__ == '__main__':
    test()
