import pickle

words = [
    "hi", "hello", "how", "are", "you", "is", "anyone", "there", "good", "day",
    "hey", "what’s", "up", "howdy", "morning", "evening", "bye", "see", "later",
    "goodbye", "take", "care", "catch", "ya", "thanks", "thank", "that", "helpful",
    "appreciate", "lot", "many", "how", "old", "what", "your", "birth", "year", 
    "location", "live", "find", "based", "weather", "rain", "temperature", 
    "forecast", "snow", "outside", "joke", "laugh", "skeleton", "fight", "guts", 
    "computer", "break", "kit-kat", "atoms", "sports", "football", "basketball", 
    "best", "soccer", "AI", "machine", "learning", "future", "neural", "networks", 
    "deep", "movie", "watch", "action", "comedy", "inception", "matrix", "shawshank",
    "redemption", "hangover", "eat", "food", "hungry", "sandwich", "pasta", "pizza", 
    "technology", "benefits", "like", "digital", "cloud", "virtual", "sci-fi", 
    "watching", "play", "team", "goal", "score", "match", "champion"
]

# Save words to words.pkl
with open('D:\PROJECTS\AI_PROJECT\Intelligent AI Web Chatbot\Preparation\model\words.pkl', 'wb') as f:
    pickle.dump(words, f)
