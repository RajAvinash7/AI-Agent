class Tool:
    def __init__(self, name, function, description):
        self.name = name
        self.function = function
        self.description = description

    def run(self, input_data):
        return self.function(input_data)


def calculator(expr):
    try:
        return eval(expr)
    except:
        return "Invalid expression"


def search(query):
    return f"Search results for '{query}'"


TOOLS = {
    "calculator": Tool(
        name="calculator",
        function=calculator,
        description="Solve mathematical expressions"
    ),
    "search": Tool(
        name="search",
        function=search,
        description="Search information"
    )
}
