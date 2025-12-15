# agents/coordinator.py

class Coordinator:
    def __init__(self, research_agent, analysis_agent, memory_agent):
        self.research_agent = research_agent
        self.analysis_agent = analysis_agent
        self.memory_agent = memory_agent

    def handle_query(self, query):
        print(f"[Manager] Received query: {query}")

        topic = self.extract_topic(query)
        print(f"[Debug] Extracted topic: '{topic}'")

        if not topic:
            return "Sorry, I could not identify a topic to research."

        # Case: Analyze / Compare query
        if "analyze" in query.lower() or "compare" in query.lower():
            # Research first
            research_data, research_conf = self.research_agent.research(topic)
            print(f"[Debug] Research data: {research_data}")

            # Log ResearchAgent state
            self.memory_agent.log_agent_state(
                "ResearchAgent", {"last_topic": topic, "last_output": research_data}
            )

            # Analysis
            analysis_summary, analysis_conf = self.analysis_agent.analyze(research_data)

            # Log AnalysisAgent state
            self.memory_agent.log_agent_state(
                "AnalysisAgent", {"last_topic": topic, "last_output": analysis_summary}
            )

            # Store in memory
            self.memory_agent.store_knowledge(
                topic=topic,
                content=analysis_summary,
                source="ResearchAgent",
                agent="AnalysisAgent",
                confidence=analysis_conf
            )
            return analysis_summary

        # Case: Memory retrieval query
        elif "what did we discuss" in query.lower():
            memory_results = self.memory_agent.search(topic)
            if memory_results:
                return [record.content for record in memory_results]
            return "No memory found for this topic."

        # Case: Just research
        else:
            research_data, research_conf = self.research_agent.research(topic)
            
            # Log ResearchAgent state
            self.memory_agent.log_agent_state(
                "ResearchAgent", {"last_topic": topic, "last_output": research_data}
            )

            # Store in memory
            self.memory_agent.store_knowledge(
                topic=topic,
                content=", ".join(research_data),
                source="ResearchAgent",
                agent="ResearchAgent",
                confidence=research_conf
            )
            return research_data

    def extract_topic(self, query):
        """
        Robust topic extraction: matches keywords even if singular/plural.
        """
        query_lower = query.lower()
        keywords = ["neural networks", "transformers", "reinforcement learning", "optimizers"]

        for k in keywords:
            # Remove trailing 's' to match singular/plural
            if any(word.rstrip('s') in query_lower for word in k.split()):
                return k
        return None
