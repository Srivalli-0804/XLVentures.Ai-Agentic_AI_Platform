from backend.tools.base.register_tools import register_all_tools
from backend.tools.base.tool_registry import tool_registry

register_all_tools()

print(tool_registry.list_tools())

provider = tool_registry.get("google_news")

print(provider.execute("OpenAI"))