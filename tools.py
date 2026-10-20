from langchain.tools import tool
import requests 
import os
from bs4 import BeautifulSoup
from tavily import TavilyClient
from rich import print
from dotenv import load_dotenv
load_dotenv()

tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
@tool
def web_search(query:str)->str:
    """Search the web and return three results with titles, URLs, and snippets."""

    tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    results=tavily.search(query=query,max_results=3)

    out=[]
    for i, result in enumerate(results.get("results", [])[:3], start=1):
        title = result.get("title", "Untitled")
        url = result.get("url", "")
        snippet = result.get("content", "No description available.")

        out.append(
            f"### {i}. {title}\n"
            f"**URL:** {url}\n\n"
            f"**Snippet:** {snippet}"
        )

    return "\n----\n".join(out)

# print(web_search.invoke("Tell me the latest news regarding War"))


@tool
def scrape_webpage(url: str) -> str:
    """Extract readable text from a webpage using its URL."""

    try:
        # Send a request to the webpage
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=8
        )

        # Raise an error if the request fails
        response.raise_for_status()

        # Parse the HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unnecessary HTML elements
        for tag in soup([
            "script",
            "style",
            "nav",
            "footer",
            "header",
            "noscript"
        ]):
            tag.decompose()

        # Extract clean text
        text = soup.get_text(separator=" ", strip=True)[:2000]

        # Limit the returned content
        return text if text else "No readable text found."

    except requests.RequestException as e:
        return f"Error fetching webpage: {str(e)}"

    except Exception as e:
        return f"Error scraping webpage: {str(e)}"

# print(scrape_webpage.invoke("https://www.csis.org/programs/latest-analysis-war-iran"))
