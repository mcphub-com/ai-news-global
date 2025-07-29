import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/ai-box-ai-box-default/api/ai-news-global'

mcp = FastMCP('ai-news-global')

@mcp.tool()
def get_news(version: Annotated[str, Field(description='')],
             region: Annotated[str, Field(description="One of the region's key code in the list of Get Regions method.")]) -> dict: 
    '''Get News by region.'''
    url = 'https://ai-news-global.p.rapidapi.com/get_news/v1/us'
    headers = {'x-rapidapi-host': 'ai-news-global.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'version': version,
        'region': region,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def available_regions() -> dict: 
    '''Get all available regions.'''
    url = 'https://ai-news-global.p.rapidapi.com/get_regions'
    headers = {'x-rapidapi-host': 'ai-news-global.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()


if __name__ == '__main__':
    mcp.run(transport="stdio")
