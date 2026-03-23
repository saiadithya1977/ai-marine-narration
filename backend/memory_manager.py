class NarrationMemory:

    def __init__(self, max_history=3):
        self.history = []
        self.max_history = max_history

    def add(self, narration):

        self.history.append(narration)

        if len(self.history) > self.max_history:
            self.history.pop(0)

    def get_context(self):

        if not self.history:
            return "No previous narration."

        return "\n".join(self.history)