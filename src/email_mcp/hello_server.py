"""Step 1: a first MCP server with one small tool and no email data."""

from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import ToolError

# The name and instructions are what a client sees when it connects.
mcp = MCPServer("hello", instructions="Counts letters in text.")


# @mcp.tool() registers the function as a tool clients can discover and call.
# The SDK reads the tool's name from the function name, its description from
# the docstring, and its input schema from the type hints, so `text: str`
# makes `text` a required string argument.
@mcp.tool()
def count_letter(text: str, letter: str) -> int:
    """Count how many times a letter appears in text, ignoring case."""
    if len(letter) != 1:
        raise ToolError("letter must be exactly one character.")
    return text.lower().count(letter.lower())


if __name__ == "__main__":
    # stdout (standard output) carries MCP messages. Send diagnostic logs to
    # stderr (standard error) so log text does not interfere with those messages.
    mcp.run(transport="stdio")
