import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_random_forest_model(hotel):
    # Preprocess the data
    hotel['city'] = hotel['city'].str.lower()
    hotel['roomamenities'] = hotel['roomamenities'].str.lower()

    # Split the data
    X = tfidf_vectorizer.fit_transform(hotel['roomamenities'])
    y = hotel['hotelcode']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the Random Forest model
    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)

    # Save the trained model to a file
    joblib.dump(rf_model, 'rf_model.pkl')

if __name__ == '__main__':
    # Load your hotel data here
    hotel_data = pd.read_csv('hotel_data.csv')
    
    # Initialize the TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # Train the Random Forest model and save it
    train_random_forest_model(hotel_data)
