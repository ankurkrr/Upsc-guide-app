#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download("punkt")
nltk.download("stopwords")

UPSC_KEYWORDS = [
    "polity", "governance", "geography", "economy", "sustainable development",
    "ethics", "biodiversity", "indian history", "international relations"
]

def extract_upsc_keywords(text):
    """Extracts UPSC-related keywords from text."""
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in tokens if word.isalpha() and word not in stop_words]
    matched_keywords = [word for word in filtered_words if word in UPSC_KEYWORDS]
    return matched_keywords
