import time

start_time = time.time()
time.sleep(1)
elapsed_time = time.time() - start_time


if (time.time() - start_time) >= 1:
    print(str(time.time() - start_time))
time.sleep(5)
print(str(time.time() - start_time))
