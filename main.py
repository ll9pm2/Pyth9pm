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
	apis = ['bd800d03-4239-423f-8530-ff54d19ece80', '83d9ba38-560c-4d0a-87bf-1746bedcadcd', '1e1cf78a-cd54-4882-9e71-e6bfb50ee79e', '6b06907a-72a7-4149-a6fe-2ec6a361187a', '3f747307-4667-41a8-af27-9fdae76071db', '91557644-4e49-4176-8e8a-566791f3298c', 'f64e734b-f115-479a-af06-ddd248d6bc15', 'de3e94cc-16dc-4eb6-9d59-3ff7271dd8e2', '43accce1-5208-44a6-a8d1-cd5229da08b4', 'db066a02-de89-4213-91ca-7080a7bc2e50']
	
	for api in apis:
	    thread = threading.Thread(target=send_request, args=(api,))
	    threads.append(thread)
	    thread.start()
	
	# Wait for all threads to complete
	for thread in threads:
	    thread.join()
	
	print("All requests finished.")
