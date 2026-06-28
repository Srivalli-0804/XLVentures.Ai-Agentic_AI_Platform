from backend.tools.base.base_tool import BaseTool
from backend.tools.base.tool_registry import tool_registry


class DummyTool(BaseTool):

    name = "dummy_tool"

    def validate(self):
        pass

    def execute(self):
        return "Hello"


tool_registry.clear()

tool_registry.register(DummyTool())

print(tool_registry.exists("dummy_tool"))

tool = tool_registry.get("dummy_tool")

print(tool.execute())

print(tool_registry.list_tools())

tool_registry.unregister("dummy_tool")

print(tool_registry.exists("dummy_tool"))