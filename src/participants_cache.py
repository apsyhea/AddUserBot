# participants_cache.py
import pickle
import os

CACHE_FILE = os.path.join('data', 'participants_cache.pkl')

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "rb") as file:
            return pickle.load(file)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "wb") as file:
        pickle.dump(cache, file)
