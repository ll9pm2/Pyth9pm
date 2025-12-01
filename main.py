# Install the Python Requests library:
# `pip install requests`
import requests
import threading
import time
from time import sleep
# Define the number of requests you want to send concurrently
NUM_REQUESTS = 2
    
    # Replace with your actual proxy details
    

    # URL-encode the password if it contains special characters like '@', ':', '%'

def send_request(request_number,api):
    """
    Sends a single HTTP GET request and prints the status and content.
    The 'request_number' is used for clearer identification in the output.
    """
    #token = api
#    url="https://viikqoye.com/dc/?blockID=394255"
# 
    start_time = time.time()
    thread_name = threading.current_thread().name
    print(f"[{time.strftime('%H:%M:%S')}] {thread_name}: Starting Request #{request_number}...")

    try:
        #response = requests.post( "https://api.scrapeless.com/api/v2/unlocker/request",
#       json=payload,
#       headers={
#           "x-api-token": token,
#           "Content-Type": "application/json"
#       },
#       timeout=60)
        proxy_username = "fwEiEZznyiwskSYg"
        proxy_password = "G0JV6SJbj9R2SnNu" # Be careful with special characters in passwords 
        proxy_ip = "geo.floppydata.com"
        proxy_port = "10080"
        proxies = {
        "http": f"http://{proxy_username}:{proxy_password}@{proxy_ip}:{proxy_port}",
        #"https": f"https://{proxy_username}:{proxy_password}@{proxy_ip}:{proxy_port}",
    }
        response = requests.get(
            url='https://api.webscrapingapi.com/v2?',
            params={
                'api_key': api,
                'url': "https://www.effectivegatecpm.com/wi8c609y28?key=433b0fd1f7990464917c15b1a2e1be90",
                "render_js":"1"
            },
            
            timeout=60 # Set a timeout to prevent threads from hanging indefinitely
        )
        
        duration = time.time() - start_time
        print(f"[{time.strftime('%H:%M:%S')}] {thread_name}: Finished Request #{request_number}. Status Code: {response.status_code} in {duration:.2f}s")
        print('Response Body: ',"proxy" in response.text) # Uncomment to see the content
    
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
    for i in range(3000):
      
      apis =["9jnK3XQJHBNf8nr3u7zZ2gj6QNyuYujo",
    ]
      
    #  proxy = f"http://oc-3e23d2c0fdc45df7035adb7639613b0b70bcc0177590cade0f3c1b84bdf0ffa8-country-us-session-5{i}6gg{i+2}hh{i*3}b:uqx15udtl5ix@proxy.oculus-proxy.com:31114"
      #proxy="https://spgcjphbu4:Hy+zH5s4vmfr3vS3iN@gate.decodo.com:10001"
      threads2 = []
      for api in apis:
        # Create a new Thread object, targeting the send_request function
        thread2 = threading.Thread(target=send_requests_with_threading, args=(api,))
        threads2.append(thread2)
        thread2.start() # Immediately start the thread, running the request concurrently
      for thread2 in threads2:
        thread2.join()
