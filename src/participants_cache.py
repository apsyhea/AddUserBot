import os
import pickle

# Указание правильного пути для кэша в корневом каталоге проекта
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
cache_dir = os.path.join(base_dir, 'data')
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)
cache_file = os.path.join(cache_dir, 'participants_cache.pkl')

def load_cache():
    try:
        with open(cache_file, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def save_cache(cache):
    with open(cache_file, 'wb') as f:
        pickle.dump(cache, f)
