from langchain.agents import AgentType, initialize_agent, create_structured_chat_agent
from langchain_community.agent_toolkits.jira.toolkit import JiraToolkit
from langchain_community.agent_toolkits.json.toolkit import JsonToolkit
from langchain_community.utilities.jira import JiraAPIWrapper
from langchain_openai import ChatOpenAI, OpenAI

class JiraAgent:
    def __init__(self, verbose):
        self.llm = OpenAI(temperature=0)
        self.jira = JiraAPIWrapper()
        self.toolkit = JiraToolkit.from_jira_api_wrapper(self.jira)
        self.jira_agent = initialize_agent(
            self.toolkit.get_tools(), self.llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=verbose
        )
        self.response_agent = ChatOpenAI(temperature = 0)

    def run(self, prompt):
        jira_response = self.jira_agent.run(prompt)
        human_result = self.response_agent.predict(text ="Convert the following JSON string received from a JIRA REST API response to human readable text in markdown format. Make it a single level bullet point list, and no preeceding or text following is required. Skip numeric ids but include keys.:\n" + jira_response)
        return human_result
