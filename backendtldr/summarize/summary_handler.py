"""
Tokenizes, queues, summarizes, and formats the content passed here.
"""
import os
import nltk
from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tokenize.moses import MosesDetokenizer
from summarize.models import Event
from pgmodel import run_summarization

# Status: In Progress
# TODO: Get better summ model


def get_articles():
    """Gets articles that need summarization and queues them up"""
    events = Event.objects.filter(Event__needs_summary=True)
    article_list = {}
    # Retreive said events and add their articles to a dictionary
    for event in events:
        article_list[event.id] = event.articles
    return article_list


def tokenize(content):
    """Breaks up text-based content into tokens in the style of PTB corpus"""
    _path_to_jar = os.path.abspath('stanford-postagger/stanford-postagger.jar')
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
    summarized_tokens = run_summarization.article_summarunner(token_list)
    return summarized_tokens


def run_summary():
    """Takes events that need a summary and returns summarized content"""
    # Get the dictionary of articles that needs a summary
    articles = get_articles()
    # process article(tokenize, feed and format)
    for event_id, article in articles.items():
        token_list = tokenize(article)
        summ_token = feed_model(token_list)
        summary = format_summary(summ_token)
        # Add summary to event object
        event = Event.objects.get(id__exact=event_id)
        event.summary = summary
        event.needs_summary = False
        event.save()


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
