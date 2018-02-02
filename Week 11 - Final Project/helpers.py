from __future__ import print_function
import json
import csv
import urllib.request

from flask import redirect, render_template, request, session
from functools import wraps

from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions


def apology(message, code=400):
    """Renders message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# analyze the URL using the Watson Natural Language Processing API
def analyze(URL):

    # API documentation: https://www.ibm.com/watson/developercloud/natural-language-understanding/api/v1/?python#post-analyze
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        username='17449e70-6d27-40fe-9590-2f586a5dd36e',
        password='OoX2eHCbujar')

    response = natural_language_understanding.analyze(
        url=URL,
        features=Features(entities=EntitiesOptions(limit=5), keywords=KeywordsOptions(limit=5)))

    # return (json.dumps(response, indent=2))
    return response