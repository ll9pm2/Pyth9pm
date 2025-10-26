import requests
# Install the Python Requests library:
# `pip install requests`
import requests
import threading
import time
from random import randint
# Define the number of requests you want to send concurrently
NUM_REQUESTS = 1

def send_request(request_number,api):
    """
    Sends a single HTTP GET request and prints the status and content.
    The 'request_number' is used for clearer identification in the output.
    """
    headers = {
    'Content-Type': 'application/json',
    'x-api-key': api,
}

    json_data = {
    'url': 'https://viikqoye.com/dc/?blockID=399115',
    'proxyType': 'residential',
    'proxyCountry': 'US',
    'blockResources': False,
    'blockAds': False,
    'blockUrls': [],
    'wait': randint(10000,25000),
    'jsScenario': [
        {
            'click': 'button',
        },
        {
            'wait': f"{randint(1000,5000)}",
        },
    ],
    'extractRules': {
        'title': 'h1',
    },
    'screenshot': True,
    'jsRendering': True,
    'extractEmails': True,
    'includeOnlyTags': [],
    'excludeTags': [],
    'outputFormat': [],
}


    start_time = time.time()
    thread_name = threading.current_thread().name
    print(f"[{time.strftime('%H:%M:%S')}] {thread_name}: Starting Request #{request_number}...")

    try:
        response = requests.post('https://api.hasdata.com/scrape/web', headers=headers, json=json_data)

        print(response.text)
      
        duration = time.time() - start_time
        print(f"[{time.strftime('%H:%M:%S')}] {thread_name}: Finished Request #{request_number}. Status Code: {response.status_code} in {duration:.2f}s")
        # print('Response Body: ', response.content) # Uncomment to see the content
    
    except requests.exceptions.RequestException as e:
        print(f"[{time.strftime('%H:%M:%S')}] {thread_name}: Error in Request #{request_number}: {e}")

def send_requests_with_threading(api):
    """
    Creates and starts 5 threads, each running the send_request function,
    and waits for them all to complete.
    """
    threads = []
    
    global_start_time = time.time()
    print(f"--- Starting {NUM_REQUESTS} concurrent requests using threads ---")

    # 1. Create and Start Threads
    for i in range(1, NUM_REQUESTS + 1):
        # Create a new Thread object, targeting the send_request function
        thread = threading.Thread(target=send_request, args=(i,api), name=f"WorkerThread-{i}")
        threads.append(thread)
        thread.start() # Immediately start the thread, running the request concurrently

    # 2. Wait for all Threads to Finish (Joining)
    # The main program thread blocks (pauses) at .join() until the corresponding thread finishes.
    for thread in threads:
        thread.join()

    global_duration = time.time() - global_start_time
    print("\n--- All concurrent requests completed ---")
    print(f"Total elapsed time: {global_duration:.2f} seconds")

if __name__ == '__main__':
    for i in range(200):
      
      apis =[
     "57acce2c-9129-4105-989d-330f88dd97ec",
"4bb5a5ae-e930-4362-9e98-c5e9daad3bd9",
"2cf15792-0ed4-4611-8e41-dcc405d0b27a",
"d778c504-8b36-4b4f-a14a-7799a52b9d95",
"b535c470-d704-4b29-b758-cff276c2eb67",
"0733584e-0e95-46bf-9995-4cca8d820fe8",
         ]
      threads2 = []
      for api in apis:
        # Create a new Thread object, targeting the send_request function
        thread2 = threading.Thread(target=send_requests_with_threading, args=(api,))
        threads2.append(thread2)
        thread2.start() # Immediately start the thread, running the request concurrently
      for thread2 in threads2:
        thread2.join()
    

      


