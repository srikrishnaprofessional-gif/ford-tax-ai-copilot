def ask_copilot(question):

    q = question.lower()

    if "tax determination" in q:
        return "Tax determination calculates the correct tax during a transaction."

    if "vertex" in q:
        return "Vertex is an enterprise tax engine used for real time tax calculations."

    if "tax reporting" in q:
        return "Tax reporting consolidates tax data and generates regulatory reports."

    return "I can answer questions about enterprise tax systems."