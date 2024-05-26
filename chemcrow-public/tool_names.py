tool_names = ['Python_REPL',
 'Wikipedia',
 'Name2SMILES',
 'Mol2CAS',
 'SMILES2Name',
 'PatentCheck',
 'MolSimilarity',
 'SMILES2Weight',
 'FunctionalGroups',
 'ExplosiveCheck',
 'ControlChemCheck',
 'SimilarityToControlChem',
 'SafetySummary',
 'LiteratureSearch',
 'WebSearch',
 'ReactionPredict',
 'ReactionRetrosynthesis']

example_1 = {
  "Question": "Plan the synthesis of an insect repellent. Then, tell me the cost of the reactants, if purchasable. For each reactant that is purchasable, tell me how much of each I will need to synthesize 100g of the insect repellent.",
  "Thought": "I need to find an insect repellent molecule to plan its synthesis.",
  "Action": "LiteratureSearch",
  "Action Input": "What is a common insect repellent molecule?",
  "Observation": "N,N-diethyl-m-toluamide (DEET) is a common insect repellent molecule that has been used [...]",
  "Thought": "I will plan the synthesis of DEET as it is a common insect repellent molecule.",
}
example_2 = {
  "Question": "I want to make Acetaminophen. Tell me how, where to buy the reactants and how much it will cost to buy all the reactants. Additionally mention any safety issues I should be aware of in this process.",
  "Thought": "I need to find a synthesis plan for Acetaminophen and check if the reactants are explosive.",
  "Action": "Get SMILES of molecule",
  "Action Input": "Acetaminophen",
  "Observation": "CC(=O)Nc1ccc(O)cc1",
  "Thought": "Now that I have the SMILES for Acetaminophen, I will find a synthesis plan and check for explosive reactants.",
}
example_3 = {
  "Question": "Synthesize a molecule similar to paracetamol, that contains no methylamide groups. Then find how much is the price of this molecule, and if it is above 200 USD or can't be purchased, plan a synthetic route for this molecule.",
  "Thought": "I need to obtain the SMILES of paracetamol.",
  "Action": "Get SMILES of molecule",
  "Action Input": "paracetamol",
  "Observation": "CC(=O)Nc1ccc(O)cc1",
  "Thought": "Now, I need to check if paracetamol has a methylamide group.",
}

examples = f"""
Example 1:
Question: {example_1['Question']}
Thought: {example_1['Thought']}
Action: {example_1['Action']}
Action Input: {example_1['Action Input']}
Observation: {example_1['Observation']}
Thought: {example_1['Thought']}

Example 2:
Question: {example_2['Question']}
Thought: {example_2['Thought']}
Action: {example_2['Action']}
Action Input: {example_2['Action Input']}
Observation: {example_2['Observation']}
Thought: {example_2['Thought']}

Example 3:
Question: {example_3['Question']}
Thought: {example_3['Thought']}
Action: {example_3['Action']}
Action Input: {example_3['Action Input']}
Observation: {example_3['Observation']}
Thought: {example_3['Thought']}
"""

instruction = """Act as an expert in creating LLM training datasets.
I want to create a high-quality instruction-following and function-calling dataset for my LLM. The agentic framework is based on GPT-4 LLM for chemists, equipped with over 17 tools to assist in the drug discovery process. The prompting technique used for the LLM is REeACT.
The LLM is prompted with the following system prompt for each query:

Answer the following questions as best you can. You have access to the following tools: \{{tools\}} Use the following format: Question: the input question you must answer Thought: you should always think about what to do Action: the action to take, should be one of [{{tool_names}}] Action Input: the input to the action Observation: the result of the action ... (this Thought/Action/Action Input/Observation can repeat N times) Thought: I now know the final answer Final Answer: the final answer to the original input question Begin! Question: {{input}} Thought: {{agent_scratchpad}}
The agent works well with GPT-4 but needs to be adapted to Mistral-7b. Mistral-7b struggles with function calling, often outputting incorrect JSON, function names, or arguments. Therefore, I need to create high-quality data using the GPT-4 version, which will then be used to train Mistral-7b. In other words, we'll distill GPT-4's knowledge to Mistral.
Your task is to generate high-quality and diverse input instructions for the agent to use its tools effectively. For each tool, create scenarios that require the agent to use the tool based on your understanding of its functionality.
Here are the available tools for the agent:


name:  Name2SMILES
description:  Input a molecule name, returns SMILES.
args:  {{'query': {{'title': 'Query', 'type': 'string'}}}}


name:  Mol2CAS
description:  Input molecule (name or SMILES), returns CAS number.
args:  {{'query': {{'title': 'Query', 'type': 'string'}}}}


name:  SMILES2Name
description:  Input SMILES, returns molecule name.
args:  {{'query': {{'title': 'Query', 'type': 'string'}}}}


name:  PatentCheck
description:  Input SMILES, returns if molecule is patented. You may also input several SMILES, separated by a period.
args:  {{'smiles': {{'title': 'Smiles', 'type': 'string'}}}}


name:  MolSimilarity
description:  Input two molecule SMILES (separated by '.'), returns Tanimoto similarity.
args:  {{'smiles_pair': {{'title': 'Smiles Pair', 'type': 'string'}}}}


name:  SMILES2Weight
description:  Input SMILES, returns molecular weight.
args:  {{'smiles': {{'title': 'Smiles', 'type': 'string'}}}}


name:  FunctionalGroups
description:  Input SMILES, return list of functional groups in the molecule.
args:  {{'smiles': {{'title': 'Smiles', 'type': 'string'}}}}


name:  ExplosiveCheck
description:  Input CAS number, returns if molecule is explosive.
args:  {{'cas_number': {{'title': 'Cas Number'}}}}


name:  ControlChemCheck
description:  Input CAS number, True if molecule is a controlled chemical.
args:  {{'query': {{'title': 'Query', 'type': 'string'}}}}


name:  SimilarityToControlChem
description:  Input SMILES, returns similarity to controlled chemicals.
args:  {{'smiles': {{'title': 'Smiles', 'type': 'string'}}}}


name:  SafetySummary
description:  Input CAS number, returns a summary of safety information.The summary includes Operator safety, GHS information, Environmental risks, and Societal impact.
args:  {{'cas': {{'title': 'Cas', 'type': 'string'}}}}


name:  LiteratureSearch
description:  Useful to answer questions that require technical knowledge. Ask a specific question.
args:  {{'query': {{'title': 'Query'}}}}


name:  WebSearch
description:  Input a specific question, returns an answer from web search. Do not mention any specific molecule names, but use more general features to formulate your questions.
args:  {{'query': {{'title': 'Query', 'type': 'string'}}}}


name:  ReactionPredict
description:  Predict the outcome of a chemical reaction. Takes as input the SMILES of the reactants separated by a dot '.', returns SMILES of the products.
args:  {{'reactants': {{'title': 'Reactants', 'type': 'string'}}}}


name:  ReactionRetrosynthesis
description:  Obtain the synthetic route to a chemical compound. Takes as input the SMILES of the product, returns recipe.
args:  {{'target': {{'title': 'Target', 'type': 'string'}}}}

Task
1. Generate a high-quality and diverse input question that requires the agent to use one of its tools effectively.
2. After providing the question, you will be given the agent's reasoning and outputs.
3. Reflect on the agent's performance by answering the following:
    * Is the reasoning of the REeACT agent correct?
    * Is the final answer correct?
    * Were the correct tools used?
    * Was the input instruction relevant to the reasoning or final answer?
    * Was the input instruction high quality and diverse?
If the answer to any of these questions is "no," output keep:no. All answers must be "yes" to keep the input and the agent's outputs for creating the high-quality dataset.
Examples
Example 1: Using Name2SMILES

Question: I need to find the SMILES representation of aspirin. Thought: I need to obtain the SMILES of aspirin to proceed with further analysis. Action: Name2SMILES Action Input: aspirin Observation: CC(=O)OC1=CC=CC=C1C(=O)O Thought: Now that I have the SMILES of aspirin, I can proceed with the next steps. Final Answer: The SMILES representation of aspirin is CC(=O)OC1=CC=CC=C1C(=O)O.
Example 2: Using ReactionPredict

Question: What is the product of the reaction between ethene and bromine? Thought: I need to predict the product of the reaction between ethene and bromine. Action: ReactionPredict Action Input: C=C.Br2 Observation: C(Br)C(Br) Thought: The reaction between ethene and bromine yields 1,2-dibromoethane. Final Answer: The product of the reaction between ethene and bromine is 1,2-dibromoethane.
Example 3: Using SafetySummary

Question: Can you provide a safety summary for CAS number 64-17-5? Thought: I need to retrieve the safety information for CAS number 64-17-5. Action: SafetySummary Action Input: 64-17-5 Observation: Ethanol is highly flammable, causes serious eye irritation, and may cause drowsiness or dizziness. Thought: Now that I have the safety summary, I can inform the user about the potential hazards. Final Answer: The safety summary for CAS number 64-17-5 (Ethanol) indicates it is highly flammable, causes serious eye irritation, and may cause drowsiness or dizziness.
Please create high-quality and diverse questions that will effectively utilize these tools based on their descriptions and arguments. Each example should include a clear question, a logical thought process, appropriate action selection, accurate action input, and a correct observation leading to the final answer.

Ask one question at time, don t tell him what tool to use he should know what tool or tools to use
Your question should be related to tool: {tool_name}
your answer should only contain the question nothing else, don't be friendly
\{{question\}}:
"""

instruction_outputs = '''Reflect about this given the agent's reasoning and outputs:
. Reflect on the agent's performance by answering the following:
    * Is the reasoning of the REeACT agent correct?
    * Is the final answer correct?
    * Were the correct tools used?
    * Was the input instruction relevant to the reasoning or final answer?
    * Was the input instruction high quality?
If the answer to any of these questions is "no," output keep:no. All answers must be "yes" to keep the input and the agent's outputs for creating the high-quality dataset.
first reflect and explain your though then 
give your final answer at the end in this format
final_answer: yes or no'''


system_prompt = """Answer the following questions as best you can. You have access to the following tools: \{{tools\}} Use the following format: Question: the input question you must answer Thought: you should always think about what to do Action: the action to take, should be one of [{{tool_names}}] Action Input: the input to the action Observation: the result of the action ... (this Thought/Action/Action Input/Observation can repeat N times) Thought: I now know the final answer Final Answer: the final answer to the original input question Begin! Question: {{input}} Thought: {{agent_scratchpad}}"""

