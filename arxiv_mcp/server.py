import sys

from arxiv_mcp.app import mcp

from arxiv_mcp.resources import resources
from arxiv_mcp.tools import tools
from arxiv_mcp.prompts import prompts

def main():

    print("Đang khởi động máy chủ...", file=sys.stderr) 
    
    mcp.run()
    
    print("Máy chủ ngừng hoạt động.", file=sys.stderr)

if __name__ == "__main__":
    main() 
