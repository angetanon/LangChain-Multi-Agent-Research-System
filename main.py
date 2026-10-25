from src.tools.tools import web_search, scrape_url

#output = web_search.invoke({"query": "Latest news on AI research"})
# print(output)

results = web_search.invoke("What is the lastest news on AI research for climate change mitigation")
print(results)