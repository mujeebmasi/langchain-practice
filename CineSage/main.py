import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser


load_dotenv()
model = ChatGroq(
    model="llama-3.3-70b-versatile"
)
class MovieInfo(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str
    
parser = PydanticOutputParser(pydantic_object=MovieInfo)


prompt = ChatPromptTemplate.from_messages([('system', """
                                           Extract Movie information from the given paragraph.
                                           {format_instructions}
                                           """),
                                          ('human',"""
                                           "{paragraph}"
                                           """)])

para = input("Give your movie paragraph: ")

final_prompt = prompt.invoke({"paragraph": para, "format_instructions": parser.get_format_instructions()})

response = model.invoke(final_prompt)

parsed_output = parser.parse(response.content)

print(parsed_output)