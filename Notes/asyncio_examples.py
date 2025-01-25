import time

def fetch_data(api_name):
    """Simulate fetching data from an API."""
    print(f"Start fetching from {api_name}...")
    time.sleep(2)  # Simulate network delay
    print(f"Finished fetching from {api_name}!")

start_time = time.time()

# Fetch data from 3 APIs sequentially
fetch_data("API 1")
fetch_data("API 2")
fetch_data("API 3")

end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")



#####################################################################
### Benefits of Asyncio
# Concurrency: Tasks don’t block each other, saving time during I/O operations.
# Efficiency: It uses a single thread and avoids the overhead of creating multiple threads or processes.

import asyncio

# define a coroutine= async def my_function()
async def fetch_data(api_name):
    """Simulate fetching data from an API."""
    print(f"Start fetching from {api_name}...")
    await asyncio.sleep(2)  # Non-blocking wait
    print(f"Finished fetching from {api_name}!")

async def main():
    # Create tasks for each API call
    task1 = asyncio.create_task(fetch_data("API 1")) # schedule coroutine 1 as a task
    task2 = asyncio.create_task(fetch_data("API 2")) # task2 runs conncurrently on the event loop
    task3 = asyncio.create_task(fetch_data("API 3"))
    
    # Run all tasks concurrently and waits for them to complete
    await asyncio.gather(task1, task2, task3)

# Measure time taken
start_time = time.time()
# starts the event loop and runs the main coroutine
asyncio.run(main())
end_time = time.time()
print(f"Total time taken: {end_time - start_time:.2f} seconds")
