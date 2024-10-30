class LearningSystem:
    def __init__(self):
        self.learned_data = []

    def learn(self, data):
        # Placeholder for learning logic
        self.learned_data.append(data)
        return f"Learned: {data}"

    def retrieve_learned_data(self):
        return self.learned_data
