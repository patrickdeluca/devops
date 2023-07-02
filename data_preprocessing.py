```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess_data(data):
    # Download necessary NLTK data
    nltk.download('punkt')
    nltk.download('stopwords')

    # Tokenize the data
    tokenized_data = word_tokenize(data)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_data = [word for word in tokenized_data if not word in stop_words]

    return filtered_data
```