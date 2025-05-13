from arxiv_mcp.app import mcp
from arxiv_mcp import utils

@mcp.prompt()
def summarize_paper(paper_id: str) -> str:
    """Input paper ID and get an easy-to-understand summary of the paper."""
    paper = utils.get_paper_details(paper_id)
    
    if not paper:
        return f"Could not find paper with ID '{paper_id}'"
    
    return f"""
Please provide a summary of the following arXiv paper that even a middle school student could understand:

Title: {paper['title']}

Authors: {paper['authors']}

Abstract: {paper['summary']}

Please summarize in the following format:
1. Problem the paper aims to solve
2. Methods used by researchers
3. Key results and their significance
4. Simple analogies or examples for middle school students
"""

@mcp.prompt()
def compare_papers(paper_id1: str, paper_id2: str) -> str:
    """Compare and analyze two papers."""
    paper1 = utils.get_paper_details(paper_id1)
    paper2 = utils.get_paper_details(paper_id2)
    
    if not paper1 or not paper2:
        return f"One or more paper IDs are invalid."
    
    return f"""
Please compare and analyze the following two arXiv papers:

Paper 1:
- Title: {paper1['title']}
- Authors: {paper1['authors']}
- Abstract: {paper1['summary']}

Paper 2:
- Title: {paper2['title']}
- Authors: {paper2['authors']}
- Abstract: {paper2['summary']}

Please compare based on the following criteria:
1. Comparison of main goals/objectives of both papers
2. Comparison of methodologies used
3. Comparison of results and claims
4. Research limitations
5. Analysis of which paper is more innovative or impactful
"""
