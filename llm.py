from transformers import TFBloomForCausalLM, BloomTokenizerFast
from langchain import LLMChain, PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.llms import HuggingFaceHub

# Load the tokenizer and model with TensorFlow
model_name = "bigscience/bloom-560m"  # You can use different variants of BLOOM as needed
tokenizer = BloomTokenizerFast.from_pretrained(model_name)
model = TFBloomForCausalLM.from_pretrained(model_name, from_pt=True)

# Sample text generation
input_text = "The stock market today"
inputs = tokenizer(input_text, return_tensors="tf")
outputs = model.generate(**inputs, max_length=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))



# Initialize Hugging Face BLOOM with TensorFlow as the backend
hf_llm = HuggingFaceHub(
    repo_id=model_name,
    model_kwargs={"framework": "tf", "temperature": 0.7, "max_length": 50}
)

# Define a prompt template for financial analysis
template = """
You are a financial analyst bot. Answer the user's question based on the following information:

{question}

"""

prompt = PromptTemplate(
    input_variables=["question"],
    template=template,
)

# Define a LangChain with BLOOM
llm_chain = LLMChain(
    llm=hf_llm,
    prompt=prompt,
    memory=ConversationBufferMemory()
)

def analyze_financial_data(question: str):
    response = llm_chain.run(question)
    return response

# Example Usage
question = "What is the impact of inflation on cryptocurrency?"
response = analyze_financial_data(question)
print(response)
