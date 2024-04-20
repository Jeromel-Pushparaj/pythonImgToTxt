from extracter import ingrediant
from llama_index.llms.ollama import Ollama

llm = Ollama(model="llama2", request_timeout=1000)

prompt = """
Your task is to evaluate the advantages and disadvantages of a set of ingredients commonly found in medicinal or cosmetic products. The product formulation may vary, but your analysis should focus on providing clear insights into the benefits and drawbacks of each ingredient. Your analysis will assist consumers in making informed decisions about product usage.

Ingredients:
""""" + str(ingrediant) + """
Your objective is to succinctly outline the advantages and disadvantages of each ingredient in a straightforward and comprehensible manner. Consider potential benefits, such as therapeutic properties or functional characteristics, as well as any drawbacks, including adverse effects or limitations. Additionally, emphasize any pertinent considerations for individuals using products containing these ingredients.
"""

llmOutput = llm.complete(prompt)
print(llmOutput)
with open("MyFile.md", "w") as file:
    file.write(str(llmOutput))