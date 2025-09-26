from typing import Dict, TypedDict
from langgraph.graph import StateGraph
from IPython.display import Image, display

# Agora, vou criar o AgentState


class AgentState(TypedDict):  # Schema do estado
    message: str


def greeting_node(state: AgentState) -> AgentState:
    """Um nó simples que adiciona uma saudação a mensagem."""
    state['message'] = "Olá " + state['message'] + ", como está sendo seu dia?"

    return state


graph = StateGraph(AgentState)

graph.add_node("Saudacao", greeting_node)

graph.set_entry_point("Saudacao")
graph.set_finish_point("Saudacao")

app = graph.compile()

display(Image(app.get_graph().draw_mermaid_png()))
