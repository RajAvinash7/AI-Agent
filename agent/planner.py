class Planner:
    """
    Planner decides WHAT the agent should do and WHY
    """

    def decide(self, user_input: str):
        text = user_input.strip().lower()

        # Calculator detection
        if any(op in text for op in ["+", "-", "*", "/"]):
            return (
                "calculator",
                user_input,
                "Detected mathematical expression, using calculator tool"
            )

        # Search intent
        if text.startswith("search"):
            query = user_input.replace("search", "", 1).strip()
            return (
                "search",
                query,
                "Detected search intent, using search tool"
            )

        # Memory inspection
        if text == "memory":
            return (
                "respond",
                "memory",
                "User requested agent memory"
            )

        # Default language response
        return (
            "respond",
            user_input,
            "General language query, using LLM"
        )
