import requests


class QuestionData:

    def __init__(self):
        """Instantiate the class and create the attributes."""
        # invoke the API and get the data.
        a_parameters = {
            'amount': 10,
            'category': 18,
            'type': 'boolean',
        }
        a_response = requests.get(url='https://opentdb.com/api.php', params=a_parameters)
        a_response.raise_for_status()
        self.a_response_data = a_response.json()
        self.questions_list = []
        return

    def get_questions(self) -> list:
        """Gets the questions from the API response."""
        self.questions_list = self.a_response_data['results']
        return self.questions_list
