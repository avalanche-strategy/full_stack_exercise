import math


def calculateTFIDF(
    number_of_documents, number_of_documents_with_word, count_of_word_in_document
):
    """
    This function returns the calculation of "Term Frequency Inverse Document Frequency"
    or TFIDF.

    Given a set of documents, TFIDF is a measure of how frequent a particular word (or term) is
    in any specific document within that set.
    numberOfDocuments - The number of documents you're considering.
    numberOfDocumentsWithWord - The number of documents that contain the word
    you calculating TFIDF for.
    countOfWordInDocument - The number of times the word appears in the document
    you're calculating TFIDF for.
    """

    return math.log(number_of_documents / number_of_documents_with_word) * math.log(
        count_of_word_in_document
    )


def solution(data, num_top_words):
    """
    Put your solution here

    Given a set of documents, and the number of top words to
    calculate, this function should return the number of top words for
    each document. To calculate the top words you should
    1) Count how many times a word appears in each document.
    2) Calculate the TFIDF for each word in each document.
    3) Return the numberOfTopWords words with the highest TFIDF score.
    documents - A dictionary with keys of the document names.
    The values are arrays of every word in the document.
    numberOfTopWords - The number of top words to return.

    return - A dictionary with keys of the document names, and
    values of arrays of the top words.
    """

    return {"document 1": ["word 1", "word 2"], "document 2": ["word 1", "word 2"]}
