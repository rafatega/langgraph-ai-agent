import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
# ou outro wrapper de LLM que você estiver usando
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

server_params = StdioServerParameters(
    command="python",
    args=[r"C:\Users\Tega\Documents\Projetos\langgraph-ai-agent\app\mcp_math_sample.py"],
)


async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await load_mcp_tools(session)

            # Crie uma instância do modelo
            llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-5")

            # Cria o agente ReAct com o LLM e as ferramentas carregadas
            agent = create_react_agent(llm, tools)

            # Use o agente, por exemplo:
            response = await agent.ainvoke({"messages": "Qual o nome do presidente do Brasil?"})
            print(response)

if __name__ == "__main__":
    asyncio.run(main())
