import requests
import xml.etree.ElementTree as ET
from typing import List, Dict, Any

from arxiv_mcp.app import mcp
from arxiv_mcp import utils

@mcp.resource("arxiv://{category}")
def get_papers_by_category(category: str) -> str:
    """Fetch the latest arXiv papers from a specific category."""
    papers = utils.fetch_arxiv_papers(category)
    
    if not papers:
        return f"No papers found in category '{category}'"
    
    result = f"## Latest Papers in arXiv '{category}' Category\n\n"
    for i, paper in enumerate(papers, 1):
        result += f"### {i}. {paper['title']}\n"
        result += f"**Authors**: {paper['authors']}\n"
        result += f"**Date**: {paper['published']}\n"
        result += f"**ID**: {paper['id']}\n"
        if 'categories' in paper and paper['categories']:
            result += f"**Categories**: {paper['categories']}\n"
        result += f"**Abstract**: {paper['summary'][:300]}...\n\n"
    
    return result

@mcp.resource("author://{name}")
def get_papers_by_author(name: str) -> str:
    """Fetch arXiv papers by a specific author."""
    base_url = "http://export.arxiv.org/api/query"
    params = {
        'search_query': f'au:"{name}"',
        'start': 0,
        'max_results': 10
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        return f"Error occurred while searching for author: {response.status_code}"
    
    root = ET.fromstring(response.content)
    
    papers = []
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
        paper_id = entry.find('{http://www.w3.org/2005/Atom}id').text.split('/abs/')[-1]
        published = entry.find('{http://www.w3.org/2005/Atom}published').text
        
        papers.append({
            'title': title,
            'id': paper_id,
            'published': published[:10] 
        })
    
    if not papers:
        return f"No papers found for author '{name}'"
    
    result = f"## List of arXiv Papers by '{name}'\n\n"
    for i, paper in enumerate(papers, 1):
        result += f"{i}. **{paper['title']}**\n"
        result += f"   Published: {paper['published']}\n"
        result += f"   ID: {paper['id']}\n\n"
    
    return result
