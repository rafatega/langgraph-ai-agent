from mcp.server.fastmcp import FastMCP

# Inicia usando: mcp dev app/mcp_math_sample.py
# 1. MCP server instance named "Math"
mcp = FastMCP("Math")

# 2. Registra as funções como uma ferramenta no servidor MCP


@mcp.tool()
def add(a: int, b: int) -> int:
    """Soma dois números inteiros"""
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiplica dois números inteiros"""
    return a * b

# 3. Iniciando o servidor MCP
if __name__ == "__main__":
    mcp.run(transport="stdio")
