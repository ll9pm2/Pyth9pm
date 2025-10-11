import http.client
import threading

def send_request(api):
    print("start",api)
    url = "/scrape/web"
    payload = "{\"url\":\"https://viikqoye.com/dc/?blockID=394255\",\"proxyType\":\"residential\",\"proxyCountry\":\"US\",\"blockResources\":false,\"blockAds\":false,\"blockUrls\":[],\"wait\":10000,\"jsScenario\":[],\"extractRules\":{\"title\":\"h1\"},\"screenshot\":true,\"jsRendering\":true,\"extractEmails\":false,\"includeOnlyTags\":[],\"excludeTags\":[],\"outputFormat\":[]}"
    headers = {
    'x-api-key': api,
    'Content-Type': "application/json"
}
    try:
        conn = http.client.HTTPSConnection("api.hasdata.com")
        conn.request("POST", url, payload, headers)
        res = conn.getresponse()
        data = res.read()
        
        print(f"Request to {url} finished with status: {res.status}")
        # Process the response data as needed
    except Exception as e:
        print(f"Error sending request to {url}: {e}")
    finally:
        conn.close()

# Define your request details

for i in range(110):
	# Create a list of threads
	threads = []
	apis = ["338c9f49-d8b7-469d-84ce-d637ef751d15",
	"21f8d9ba-186b-4a75-845a-bf8b5885292e",
	"bf10ce57-122a-41be-8ae3-d7ae1ccfd0fd",
	"cca17caa-126b-46e9-902b-68b1bc1ed473",
	"0c8b6ab6-183a-4506-9650-707c68c0751e",
	"3a1aeb60-e567-40f2-9705-e44ba717374e",
	"56e05ac3-f9aa-407c-b792-3c2b45858e10",
	"2a46b0a9-968b-4e96-98fc-148ca58fab64",
	"14337553-7293-4edf-af18-0bbc9ae36165",
	"3071f8e3-109d-4514-ab9d-592550c2d595",
	"b2cafe42-4df4-4e98-93b9-2397b8e03b03"
	] 
	
	for api in apis:
	    thread = threading.Thread(target=send_request, args=(api,))
	    threads.append(thread)
	    thread.start()
	
	# Wait for all threads to complete
	for thread in threads:
	    thread.join()
	
	print("All requests finished.")
