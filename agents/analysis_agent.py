# agents/analysis_agent.py

class AnalysisAgent:
    def analyze(self, data):
        if not data or data == ["No data found"]:
            return "No data to analyze", 0.0  # confidence 0 for empty
        summary = " | ".join(data)
        tradeoffs = "Efficiency vs Accuracy trade-offs identified."
        return f"Analysis Summary: {summary}. {tradeoffs}", 0.85  # confidence 0.85
