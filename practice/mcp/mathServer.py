from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MATH")

@mcp.tool()
def add(a: int , b:int ) -> int:
    """_Summary_
    Add two numbers together."""
    return a + b 

@mcp.tool()
def multiple(a:int , b:int) -> int:
    """_Summary_
    Multiply two numbers together."""
    return a * b

if __name__ == "__main__":
    mcp.run(transport = 'studio')