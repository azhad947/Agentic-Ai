import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

OPEN_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(api_key=OPEN_API_KEY , model= 'gpt-4o-mini' , temperature=0.5)


class WaterIntakeAget:
    def __init__(self):
        self.history = []


    def analyze_intake(self , intake_ml):
        
        prompt=f"you are my hydration assistant based on much water  i have intake which is {intake_ml}  and give me some feedback in one or 2 line"

        response =  llm.invoke([HumanMessage(prompt)])

        return response.content




if __name__ == '__main__':
    agent = WaterIntakeAget()
    feedback = agent.analyze_intake(1500)  
    print(feedback)