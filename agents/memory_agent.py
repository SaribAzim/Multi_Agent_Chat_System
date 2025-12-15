# agents/memory_agent.py

from datetime import datetime
from memory.schemas import MemoryRecord
from memory.vector_store import SimpleVectorStore

class MemoryAgent:
    def __init__(self):
        self.conversation_memory = []
        self.knowledge_base = []
        self.vector_store = SimpleVectorStore()
        self.agent_states = {}

    def store_knowledge(self, topic, content, source, agent, confidence):
        """
        Store structured knowledge in memory and vector store.
        """
        record = MemoryRecord(
            timestamp=str(datetime.now()),
            topic=topic,
            content=content,
            source=source,
            agent=agent,
            confidence=confidence
        )
        self.knowledge_base.append(record)
        self.vector_store.add(content)

    def search(self, query):
        """
        Search memory for a topic keyword.
        Returns a list of MemoryRecord objects.
        """
        results = [record for record in self.knowledge_base if query.lower() in record.topic.lower()]
        return results

    def log_agent_state(self, agent, state):
        """
        Track per-agent state (last task, last topic, etc.)
        """
        self.agent_states[agent] = state

    def print_memory(self):
        """
        Print all stored memory records for debugging or inspection.
        """
        print("\n--- Memory Contents ---")
        if not self.knowledge_base:
            print("Memory is empty")
            return

        for record in self.knowledge_base:
            print(f"Timestamp: {record.timestamp}")
            print(f"Topic: {record.topic}")
            print(f"Content: {record.content}")
            print(f"Source: {record.source}")
            print(f"Agent: {record.agent}")
            print(f"Confidence: {record.confidence}\n")
