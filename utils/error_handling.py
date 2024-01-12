class ChatbotError(Exception):
    """
    Base class for other exceptions in the chatbot application.
    """
    pass

class DataError(ChatbotError):
    """
    Raised when there is an error in data processing or handling.
    """
    def __init__(self, message="Data error occurred"):
        self.message = message
        super().__init__(self.message)

class APIConnectionError(ChatbotError):
    """
    Raised when there is an issue connecting to an external API.
    """
    def __init__(self, message="API connection error occurred"):
        self.message = message
        super().__init__(self.message)

class EvaluationError(ChatbotError):
    """
    Raised during the evaluation process if an error occurs.
    """
    def __init__(self, message="Error occurred during evaluation"):
        self.message = message
        super().__init__(self.message)

# Add more custom exceptions as needed

def handle_error(error):
    """
    Generic error handling function.
    
    :param error: The exception to handle.
    """
    print(f"An error occurred: {error}")
    # Here, you can log the error to a file, notify an admin, etc.
