import re

def extract_react_elements(input_string):
    # Define regex patterns for Thought, Action, and Action Input
    thought_pattern = r"Thought:\s*(.*?)\s*Action:"
    action_pattern = r"Action:\s*(.*?)\s*Action Input:"
    action_input_pattern = r"Action Input:\s*(.*)"

    # Search for the patterns in the input string
    thought_match = re.search(thought_pattern, input_string, re.DOTALL)
    action_match = re.search(action_pattern, input_string, re.DOTALL)
    action_input_match = re.search(action_input_pattern, input_string, re.DOTALL)

    # Extract the matches if they exist
    thought = thought_match.group(1).strip() if thought_match else None
    action = action_match.group(1).strip() if action_match else None
    action_input = action_input_match.group(1).strip() if action_input_match else None

    # Return the extracted elements as a dictionary
    return {
        "Thought": thought,
        "Action": action,
        "Action Input": action_input
    }

def format_output(output):
    formatted_string = f"Here is the output from REaCT agent: \n\n output: {output['output']}\n\nintermediate steps\n"
    
    for i in range(len(output['intermediate_steps'])):
        step = output['intermediate_steps'][i]
        tool_log = extract_react_elements(step[0].log)
        
        formatted_string += f"""
tool_name: {step[0].tool}
tool_input: {step[0].tool_input}
tool_thought: {tool_log}
tool_observation: {step[1]}

Reflect about this:
1. Generate a high-quality and diverse input question that requires the agent to use one of its tools effectively.
2. After providing the question, you will be given the agent's reasoning and outputs.
3. Reflect on the agent's performance by answering the following:
    * Is the reasoning of the REeACT agent correct?
    * Is the final answer correct?
    * Were the correct tools used?
    * Was the input instruction relevant to the reasoning or final answer?
    * Was the input instruction high quality and diverse?
If the answer to any of these questions is "no," output keep:no. All answers must be "yes" to keep the input and the agent's outputs for creating the high-quality dataset.
first reflect and explain your though then 
give your final answer at the end in this format
final_answer: yes or no
"""
    return formatted_string
