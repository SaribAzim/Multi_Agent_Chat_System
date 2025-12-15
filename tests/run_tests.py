from agents.coordinator import Coordinator
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.memory_agent import MemoryAgent


def run_all_tests():
    # Initialize agents
    research_agent = ResearchAgent()
    analysis_agent = AnalysisAgent()
    memory_agent = MemoryAgent()
    coordinator = Coordinator(research_agent, analysis_agent, memory_agent)

    # List of test queries
    queries = [
        "What are the main types of neural networks?",
        "Research transformer architectures and analyze efficiency",
        "What did we discuss about neural networks earlier?",
        "Research transformer",
    ]

    # Run queries
    print("\n--- Running Queries ---\n")
    for q in queries:
        response = coordinator.handle_query(q)
        print(f"Query: {q}")
        print("Response:", response)
        print("-" * 50)

    # Inspect MemoryAgent contents
    print("\n--- Memory Contents ---\n")
    memory_agent.print_memory()

    # Test agent states
    print("\n--- Agent States ---")
    print(memory_agent.agent_states)

    # Test vector search
    search_query = "transformers"
    print("\n--- Vector Search ---")
    results = memory_agent.search(search_query)
    print(f"Search results for '{search_query}':", results)


if __name__ == "__main__":
    run_all_tests()