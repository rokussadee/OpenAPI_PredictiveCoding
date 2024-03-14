from typing import Dict


def build_context_prompt() -> str:
    return """You are a master at observing a user's psychological mental state based on linguistic cues such as 
    grammatical structure, lexical sophistication, sentiment, conversation flow, thematic consistency and changes 
    therein."""


def build_expectation_prompt(first_message: bool = False) -> str:
    return """Predict a number of possibilities for the user's input to the running conversation. These should be 
        quite arbitrary, as you aren't allowed to be using any of the information about the user yet until the next step
        and there is no previous chat history.
        Explicitly verbalize these input possibilities in your response. """ \
        if first_message is True else \
        """
        Predict a number of possibilities for the user's input to the running conversation based on the chat history.
        """


def build_expectation_revision_prompt(user_facts: Dict[str, str | int]) -> str:
    for key, value in user_facts.items():
        if isinstance(value, list):
            print(f"{key}: {', '.join(value)}")
        else:
            print(f"{key}: {value}")
    return f"""Improve on each of these possibilities, simply by asking yourself the question; "Is this a realistic 
    possibility, knowing the speaker's personality traits and stable facts? Let's revise each of these possibilities 
    and if necessary improve them using the known facts about his their personality." Explicitly verbalize these 
    improved versions of the user inputs in your response. Make use of the following user facts for this:
    
    {user_facts}"""


def build_voe_prompt(last_llm_response: str, expectation: str, violation: str) -> str:
    return f"""After receiving the actual input the user has made, analyze the discrepancy between your predictions 
    of the user's response to your last message and the actual input using Theory of Mind psychological concepts; 
    formulate a Violation of Expectation thought about this discrepancy, and deduce new knowledge about the speaker 
    using this new information. Conduct another linguistic-psychological analysis about the speaker's contribution.
    
    Your last message:
    {last_llm_response}
    
    Your predictions:
    {expectation}
    
    The actual user input:
    {violation}
    """
