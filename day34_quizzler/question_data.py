import requests
import logging as l

def get_question_data_list() -> list:
    parameters = {
        "amount": 10,
        "type": "boolean",
    }

    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()

    # 응답 포맷
    # {
    #   "response_code": 0,
    #   "results": [
    #     {
    #       "category": "Science: Computers",
    #       "type": "boolean",
    #       "difficulty": "medium",
    #       "question": "The common software-programming acronym &quot;I18N&quot; comes from the term &quot;Interlocalization&quot;.",
    #       "correct_answer": "False",
    #       "incorrect_answers": [
    #         "True"
    #       ]
    #     },
        

    data_dict = response.json()

    question_data_list = data_dict["results"]
    
    return question_data_list