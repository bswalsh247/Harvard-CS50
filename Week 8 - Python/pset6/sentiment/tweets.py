#!/usr/bin/env python3
import os
import sys
import helpers

from analyzer import Analyzer
from termcolor import colored


def main():

    # ensure proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: ./tweets @user")

     # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)

    # screen name
    screen_name = sys.argv[1]

    # gets 50 tweets from user handle
    tweets = helpers.get_user_timeline(screen_name, 50)

    # check if successful
    if tweets == None:
        sys.exit("Error, unable to access user's tweets")

    # analyze word
    for tweet in tweets:
        score = analyzer.analyze(tweet)
        if score > 0.0:
            print(colored("{}".format(tweet), "green"))
        elif score < 0.0:
            print(colored("{}".format(tweet), "red"))
        else:
            print(colored("{}".format(tweet), "yellow"))


if __name__ == "__main__":
    main()