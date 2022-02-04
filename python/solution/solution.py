import math


def calculateTFIDF(
    number_of_documents, number_of_documents_with_word, count_of_word_in_document
):
    """
    This function returns the calculation of "Term Frequency Inverse Document Frequency"
    or TFIDF.

    Given a set of documents, TFIDF is a measure of how frequent a particular word (or term) is
    in any specific document within that set.
    number_of_documents - The number of documents you're considering.
    number_of_documents_with_word - The number of documents that contain the word
    you calculating TFIDF for.
    count_of_word_in_document - The number of times the word appears in the document
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
    3) Return the num_top_words words with the highest TFIDF score.
    data - A dictionary with keys of the document names.
    The values are arrays of every word in the document.
    num_top_words - The number of top words to return.

    return - A dictionary with keys of the document names, and
    values of arrays of the top words.

    Example input for 'data' parameter:
    {
        "doc 1": ['a','b','c']
        "doc 2": ['a','d','e','a']
        "doc 3": ['d','x','y','z']
    }

    Example of how TFIDF calculation will work for the above input.
    tfidf['doc 1']['a'] = calculateTFIDF(3,2,1) 
    tfidf['doc 2']['a'] = calculateTFIDF(3,2,2) 
    """

    return {"doc 1": ["word 1", "word 2"], "doc 2": ["word 1", "word 2"] , "doc 3": ["word 1", "word 2"]}
