import sqlite3
import datetime
import matplotlib.pyplot as plt
import random
import time


def get_status():
    status = 'OK'
    return status

def save_image(status, timestamp):
    plt.plot([1, 2, 3], [random.randint(1, 10), random.randint(10, 30), random.randint(10, 30)])
    plt.savefig(f"images/{timestamp}.jpg")

def write_log(status, timestamp):
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS logs (timestamp TEXT, status TEXT)")
        c.execute("INSERT INTO logs (timestamp, status) VALUES (?, ?)", (timestamp, status))
        conn.commit()

def main():
    status = get_status()

    if status == 'OK':
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        save_image(status, timestamp)
        write_log(status, timestamp)
            
if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    execution_time = end - start
    print(f"The execution time is {execution_time} seconds")

