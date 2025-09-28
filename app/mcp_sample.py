from mcp.server.fastmcp import FastMCP
# Inicia usando: mcp dev app/mcp_sample.py

# 1. Inicializa o servidor MCP com o nome "MeuServidorMCP"
mcp = FastMCP("MeuServidorMCP")

# 2. Criando a primeira ferramenta


@mcp.tool()
def minha_primeira_tool_mcp() -> str:
    """Recomenda um filme de acordo com as especificações que o usuário passar"""
    url = "https://www.imdb.com/pt/chart/top/"
    resultado = f"Para acessar os melhores filmes você pode acessar o seguinte site: {url}"
    return resultado


# 3. Bloco de execução principal
if __name__ == "__main__":
    mcp.run()
