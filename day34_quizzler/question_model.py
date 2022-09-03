import logging as l

class Question:

    def __init__(self, q_text:str, q_answer:str):
        # l.info("class Question: __init__")
        
        self.text: str = q_text
        self.answer: str = q_answer
