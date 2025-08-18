print("start")
import asyncio
import aiohttp  # Requires installing: pip install aiohttp
from random import randint

async def fetch_url(session, url):
    """Asynchronously fetches the content of a URL using aiohttp."""
    try:
        async with session.get(url) as response:
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return await response.text()  # Or response.read() for binary data
    except aiohttp.ClientError as e:  # Catch connection errors and HTTP errors
        print(f"Error fetching {url}: {e}")
        return None


async def main():
    """Creates an aiohttp session and fetches multiple URLs concurrently."""
    urls = list()
    apis =[
        "xRay19CvcTHL5gI0lj5tudj2E0qZOUqE","l8A2d1gMDXoLPePZ9uGdWytGxlIgAHj5"]
    ad="https://viidedss.com/dc/?blockID=383089"
    for api in apis:
        for _ in range(randint (3,5)):
            #url ="https://api.webscrapingapi.com/v1?api_key=jjgCEsYztVo8MpvwtZ2rVqZxMwTKQXFo&url=https%3A%2F%2Fwww.profitableratecpm.com%2Fes8iaffr0n%3Fkey%3Da180891d7e00848a91909a7b8081d758&render_js=1&wait_until=networkidle0&wait_for=10000&country=il"
          
            url = f"https://api.webscrapingapi.com/v2?api_key={api}&url={ad}&country=us&render_js=1"
            urls.append(url)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)  # Run all tasks concurrently

    # Process the results (optional)
    for i, result in enumerate(results):
        if result:
            print("proxy" in result)
        else:
            print(f"Failed to fetch {urls[i]}")


if __name__ == "__main__":
   for i in range (1000):
     print(i)
     asyncio.run(main())
