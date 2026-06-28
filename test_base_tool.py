from backend.tools.base.base_tool import BaseTool


class DummyTool(BaseTool):

    name = "dummy"

    def validate(self):
        print("Validate")

    def execute(self):
        print("Execute")
        return "Hello"


tool = DummyTool()

tool.validate()

print(tool.execute())