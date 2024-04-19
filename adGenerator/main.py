from llama_index.llms.ollama import Ollama

llm = Ollama(model="llama2")

result = llm.complete("How can I start chat with you?")
print(result)