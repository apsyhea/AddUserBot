from tqdm import tqdm
import time

for i in tqdm(range(100), desc="Тест"):
    time.sleep(0.1)
