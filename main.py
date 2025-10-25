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
     "0a312334-72ca-41e2-9636-8233389ad212",
"180fbbc2-3cac-411c-ba3f-2755037386dc",
"51215dab-0b73-4561-ba60-c743392c0c57",
"0cf0e1af-3d14-40dd-a7d9-df9f84696b10",
"df5e264d-0a9b-4fce-8e76-7bda7543e94f",
"5290bd6d-9942-49ac-b809-d711e105d233",
"62346cc4-e370-4394-a1f2-f3d7499dea5b",
         ]
      threads2 = []
      for api in apis:
        # Create a new Thread object, targeting the send_request function
        thread2 = threading.Thread(target=send_requests_with_threading, args=(api,))
        threads2.append(thread2)
        thread2.start() # Immediately start the thread, running the request concurrently
      for thread2 in threads2:
        thread2.join()
    

      


