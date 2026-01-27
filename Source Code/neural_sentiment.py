# ==============================================================================
# PROJECT: Sentiment Analyzer
# AUTHORS: AMEY THAKUR & MEGA SATISH
# DESCRIPTION: Advanced Neural Network Sentiment Classification Logic.
# RELEASE DATE: June 30, 2021
# LICENSE: MIT License

import os
import numpy as np
import tensorflow as tf
from tensorflow import keras

class NeuralSentimentModel:
    """
    A robust implementation of a Neural Sentiment Classifier.
    
    This architecture is designed for deep semantic inference using:
        1. Word Embeddings (Dimensionality: 16)
        2. Global Average Pooling for Dimensionality Reduction
        3. Dense Hidden Layers with ReLU Activation
        4. Sigmoid Output for Probabilistic Sentiment Prediction
    """
    
    def __init__(self, vocabulary_size=10000, embedding_dim=16, max_length=500):
        self.vocabulary_size = vocabulary_size
        self.embedding_dim = embedding_dim
        self.max_length = max_length
        self.model = self._build_architecture()

    def _build_architecture(self):
        """
        Defines the structural topology of the Neural Network.
        """
        model = keras.Sequential([
            keras.layers.Embedding(self.vocabulary_size, self.embedding_dim, input_length=self.max_length),
            keras.layers.GlobalAveragePooling1D(),
            keras.layers.Dense(16, activation='relu'),
            keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def load_weights(self, weights_path):
        """
        Loads pre-trained weights into the model architecture.
        """
        if os.path.exists(weights_path):
            self.model.load_weights(weights_path)
            return True
        return False

    def predict_sentiment(self, encoded_text):
        """
        Performs inference on integer-encoded textual data.
        """
        # Ensure input is in batch format
        input_data = np.array([encoded_text])
        prediction = self.model.predict(input_data)
        return "Positive" if prediction[0] > 0.5 else "Negative"

# ==============================================================================
# ENGINE NOTE: 
# The above architecture is optimized for large-scale datasets like IMDB.
# For localized or real-time terminal analysis, the TextBlob-based engine
# in app.py provides immediate linguistic utility without the need for 
# serialized weights or extensive dataset pre-processing.
# ==============================================================================
