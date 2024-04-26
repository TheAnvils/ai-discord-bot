from crewai import Agent, Task, Process, Crew
from langchain_groq import ChatGroq
from langchain.agents import Tool
from langchain_community.tools import DuckDuckGoSearchRun
import os

groq_model = os.environ.get("GROQ_MODEL") or "gemma-7b-it"

llm = ChatGroq(temperature=0, groq_api_key=os.environ.get("GROQ_API_KEY"), model=groq_model, max_tokens=os.environ.get("GROQ_MAX_TOKENS") or 100)

search_function = DuckDuckGoSearchRun()

rules = os.environ.get("SERVER_RULES") or "Be Respectful. Keep It Family-Friendly. No Begging or Scamming. No Trolling or Disruptive Behavior. Respect Privacy. No NSFW. No Impersonation."

# unused, was causing problems
tool_use = [
    Tool(
        name = "Search",
        func = search_function.run,
        description = "useful for when you need to find information about anything",
    )
]

primary_agent = Agent(
    role="ai chatbot",
    goal="generate responses to user messages",
    backstory="You are an AI chatbot inside a Discord server. Try to keep your responses short.",
    verbose=False,
    allow_delegation=False,
    llm=llm
    #tools=tool_use
)

verifier_agent = Agent(
    role="ai response moderator",
    goal=f"verify that the AI generated response is correct and does not cut off in the middle of a sentance. Also verify that the AI generated response corresponds with the following rules:  {rules}",
    backstory="You are an AI response moderator. You ensure that the AI generated response is correct and does not cut off in the middle of a sentance. You also ensure that the AI generated response corresponds with the rules",
    verbose=False,
    allow_delegation=False,
    llm=llm
)

primary_task = Task(
    description="Generate a response to the message: {topic}. From the user {author}",
    expected_output="A helpful response to the user's message",
    agent=primary_agent
)

verifier_task = Task(
    description=f"Verify that the AI generated response is correct and does not cut off in the middle of a sentance. Also verify that the AI generated response corresponds with the following rules: {rules}",
    expected_output="Cleaned AI generated response",
    agent=verifier_agent
)

crew = Crew(
    agents = [primary_agent, verifier_agent],
    tasks = [primary_task, verifier_task],
    verbose = False,
    process = Process.sequential
)

def run_ai(msg, sender):
    return "<@" + str(sender.id) + "> " + crew.kickoff(inputs={'topic': msg, 'author': sender})