from agents.coordinator import Coordinator
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.memory_agent import MemoryAgent

def main():
    # Initialize agents
    research_agent = ResearchAgent()
    analysis_agent = AnalysisAgent()
    memory_agent = MemoryAgent()
    coordinator = Coordinator(research_agent, analysis_agent, memory_agent)

    # Example user queries
    queries = [
        "What are the main types of neural networks?",
        "Analyze the efficienty of transformers",
        "What did we discuss about neural networks earlier?"
    ]

    # Process queries sequentially
    for q in queries:
        response = coordinator.handle_query(q)
        print("\nUser Query:", q)
        print("Response:")
        # If memory search returned multiple structured results, print line by line
        if isinstance(response, list):
            for r in response:
                print("-", r)
        else:
            print(response)

if __name__ == "__main__":
    main()
    
