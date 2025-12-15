# agents/research_agent.py

class ResearchAgent:
    def __init__(self):
        self.knowledge = {
            "neural networks": [
                "Neural Networks are a foundational component of modern artificial intelligence and machine learning, here are some of its types",
                "Feedforward Neural Networks",
                "Convolutional Neural Networks",
                "Recurrent Neural Networks",
                "Transformers"
            ],
            "transformers": [
                "Self-attention mechanism",
                "Parallel computation",
                "High memory usage"
            ],
            "reinforcement learning": [
                "Policy optimization",
                "Value-based learning",
                "Exploration vs exploitation"
            ],
            "optimizers": [
                "Gradient Descent",
                "Adam",
                "RMSProp"
            ]
        }

    def research(self, topic):
        topic_lower = topic.lower()
        return self.knowledge.get(topic_lower, ["No data found"]), 0.8  # confidence 0.8
