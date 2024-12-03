import pickle

classes = [
    "greeting", "goodbye", "thanks", "age", "location", "weather", "jokes", 
    "food", "sports", "technology", "movies"
]

# Save classes to classes.pkl
with open('D:\PROJECTS\AI_PROJECT\Intelligent AI Web Chatbot\Preparation\model\classes.pkl', 'wb') as f:
    pickle.dump(classes, f)
