"""
Tokenizes, queues, summarizes, and formats the content passed here.
"""
import os
from nltk.tokenize.stanford import StanfordTokenizer

# Status: In Progress
# TODO: Content to be summarized needs to be queued
# , Modied PGModel needs to be added, formatting function needs to be added.


def tokenize(content):
    """Breaks up text-based content into tokens in the style of PTB corpus"""
    _path_to_jar = os.path.abspath('stanford-postagger/stanford-postagger.jar')
    token_list = []
    st = StanfordTokenizer(path_to_jar=_path_to_jar)
    token_list = st.tokenize(content)
    print(token_list)


if __name__ == '__main__':
    s = 'Please tokenize this text.'
    tokenize(s)
