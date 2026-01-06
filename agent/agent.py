from .memory import Memory
from .planner import Planner
from .tools import TOOLS
from .llm import LLM


class AIAgent:
    """
    A modular AI Agent implementing:
    Perception -> Reasoning -> Action -> Memory
    """

    def __init__(self, goal: str):
        self.goal = goal
        self.memory = Memory()
        self.planner = Planner()
        self.llm = LLM()

    # -----------------------------
    # PERCEPTION
    # -----------------------------
    def perceive(self, user_input: str):
        """
        Observe the environment (user input)
        """
        self.memory.add_short(user_input)

    # -----------------------------
    # REASONING / PLANNING
    # -----------------------------
    def reason(self, user_input: str):
        """
        Decide what action to take
        Returns: action, data, reasoning
        """
        action, data, reasoning = self.planner.decide(user_input)
        return action, data, reasoning

    # -----------------------------
    # ACTION
    # -----------------------------
    def act(self, action: str, data: str):
        """
        Execute selected action
        """
        # Special command: show memory
        if data.lower() == "memory":
            return self.memory.get_context()

        # Tool execution
        if action in TOOLS:
            return TOOLS[action].run(data)

        # Default: LLM response
        return self.llm.generate(data)

    # -----------------------------
    # AGENT STEP
    # -----------------------------
    def step(self, user_input: str):
        """
        One complete agent cycle
        """
        # Perceive
        self.perceive(user_input)

        # Reason
        action, data, reasoning = self.reason(user_input)

        # Explain reasoning (advanced feature)
        print(f"[Reasoning] {reasoning}")

        # Act
        result = self.act(action, data)

        # Store result in long-term memory
        self.memory.add_long(result)

        return result
