import queue
import random
import time


# Ініціалізація черги заявок
request_queue = queue.Queue()


# Лічильник заявок
request_id = 1


def generate_request():
global request_id
request = f"Request-{request_id}"
request_queue.put(request)
print(f"Generated: {request}")
request_id += 1


def process_request():
if not request_queue.empty():
request = request_queue.get()
print(f"Processing: {request}")
else:
print("No requests to process.")


# Імітація головного циклу
if __name__ == "__main__":
print("--- Service Center Simulation ---")
for _ in range(5): # Генеруємо 5 заявок
generate_request()
time.sleep(0.5)


print("\n--- Start Processing ---")


for _ in range(6): # Пробуємо обробити 6 заявок
process_request()
time.sleep(0.5)
