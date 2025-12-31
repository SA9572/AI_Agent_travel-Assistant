"""
Agentic Travel Planning Assistant
Groq-powered, guaranteed-output agent
"""

import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from agent.prompts import SYSTEM_PROMPT

# Tools
from tools.flight_tool import search_flight
from tools.hotel_tool import recommend_hotel
from tools.places_tool import recommend_places
from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget


def create_travel_agent():
    if not os.getenv("GROQ_API_KEY"):
        raise EnvironmentError("GROQ_API_KEY not set")

    tools = [
        search_flight,
        recommend_hotel,
        recommend_places,
        get_weather,
        estimate_budget,
    ]

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    ).bind_tools(tools)

    reasoning_prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{query}")
    ])

    final_prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "Generate the final day-wise travel itinerary."),
        ("assistant", "{reasoning}")
    ])

    def run_agent(query: str) -> str:
        reasoning = (reasoning_prompt | llm).invoke(
            {"query": query}
        ).content or ""

        final = (final_prompt | llm).invoke(
            {"reasoning": reasoning}
        )

        return final.content

    return run_agent


# CLI TEST
if __name__ == "__main__":
    agent = create_travel_agent()
    result = agent("create a 5 days plan for Bangalore")
    print("\n===== FINAL RESPONSE =====\n")
    print(result)
