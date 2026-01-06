from agent import AIAgent

agent = AIAgent(goal="Assist user intelligently")

print("AI Agent Started (type 'exit' to stop)")
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    response = agent.step(user_input)
    print("Agent:", response)
