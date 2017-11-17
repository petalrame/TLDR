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


def get_articles():
    """Gets articles that need summarization and queues them up"""
    # Get a QuerySet of Event objects
    result = Event.objects.filter(needs_summary=True)
    article_dict = {}
    # Retreive said events and add their articles to a dictionary
    # Loop through the QuerySet and add Event Objects to a list
    for event_obj in result:
        articles = event_obj.articles.all()
        for article in articles:
            article_dict[event_obj.id] = article.content
    return article_dict


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
    #articles = get_articles()
    # process article(tokenize, feed and format)
    #for event_id, article in articles.items():
    token_list = tokenize(article)
    summ_token = feed_model(token_list)
    summary = format_summary(summ_token)
    return summary
        #print("HERE IS THE ARTICLE: ", article)
        #print("-----------------------------------------------------------------------------------------------------------\n")
        #print("HERE IS TEH SUMMARY: ", summary)
        #print("-----------------------------------------------------------------------------------------------------------\n")
        # Add summary to event object
        #try:
        #Event.objects.filter(id=event_id).update(summary=summary, needs_summary=False)
            #print("SAVING SUMMARY TO EVENT")
            #event.summary = summary
            #event.needs_summary = False
            #print(event.sumamry)
            #event.save()
        #except:
            #print("Something went wrong with getting/saving event")


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
