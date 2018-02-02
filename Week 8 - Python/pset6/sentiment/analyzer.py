import nltk


class Analyzer():
    """Implements sentiment analysis."""
    # Define a constructor. Always include self as first parameter to know which object is being invoked

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        # loads positive and negative words into a list
        self.positives = []
        self.negatives = []

        with open(positives, "r") as file_pos:
            for line in file_pos:
                # omit leading/trailing whitespace
                if not line.startswith((";", " ")):
                    # strip out comments
                    self.positives.append(line.strip())

        with open(negatives, "r") as file_neg:
            for line in file_neg:
                if not line.startswith((";", " ")):
                    self.negatives.append(line.strip())

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        # TODO
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        score = 0

        for token in tokens:
            token.lower()

            if token in self.positives:
                score += 1
            elif token in self.negatives:
                score -= 1

        return score