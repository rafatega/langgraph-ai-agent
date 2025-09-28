from mcp.server.fastmcp import FastMCP

# Inicia usando: mcp dev app/mcp_math_sample.py
# 1. MCP server instance named "Math"
mcp = FastMCP("Math")

# 2. Registra as funções como uma ferramenta no servidor MCP


@mcp.tool()
def add(a: int, b: int) -> int:
    """Use esta função para somar dois números inteiros. Ideal para qualquer cálculo que envolva adição entre dois valores."""
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Use esta função para multiplicar dois números inteiros. Útil quando precisar calcular produtos ou partes proporcionais."""
    return a * b


@mcp.tool()
def substract(a: int, b: int) -> int:
    """Use esta função para subtrair um número inteiro de outro. Indicado para operações de diferença ou decremento."""
    return a - b


@mcp.tool()
def division(a: int, b: int) -> float:
    """Use esta função para dividir um número pelo outro. Ideal para operações que envolvem razão, média ou divisão de valores."""
    return a / b


# 3. Iniciando o servidor MCP
if __name__ == "__main__":
    mcp.run(transport="stdio")
