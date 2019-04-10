"""Find the average length of a word in a sentence."""


def avg_word_len(input):
    """Find the average sentence length."""
    lens = [len(x) for x in input.split()]
    return sum(lens) / len(lens)
