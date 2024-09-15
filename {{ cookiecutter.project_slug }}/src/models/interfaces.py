from typing import Any

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

from .models import model
from ..config.logger import logger
from .schemas import BaseSchema



class ModelInterface:
    def __init__(self):
        self.parser = JsonOutputParser(pydantic_object=BaseSchema)

        self.prompt_template = PromptTemplate(template=("### Instructions ###"
                                                        "First instruction\n"
                                                        "Second instruction\n"
                                                        "return the result following the format below:\n {instructions}"
                                                        "format: {text} json\n"
                                              ),
                                        partial_variables={"instructions":self.parser.get_format_instructions()},
                                        input_variables={"text"})



        self.chain = self.prompt_template | model | self.parser


        logger.info("Interface model initialized.")


    def get_response(self,text: str) -> Any:
        responses = self.chain.batch(text)
        logger.info("Invoke model succefull.")
        return responses


interface = ModelInterface()
