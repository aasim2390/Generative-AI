
# 📘 Output Parsers in LangChain

Output Parsers help us **take messy model outputs and convert them into clean, structured formats**.

👉 *One-liner to remember:* "Output Parsers are like teachers—they make sure the LLM’s answers are well-formatted and ready for use."

---

## 🔹 What is an Output Parser?

* **Definition:** A tool in LangChain that converts the raw response from a Language Model (LLM) into a desired format (like text, JSON, or Python objects).
* **Why needed?**

  * Most open-source models are **not trained to return structured outputs**.
  * Even models that can return structured outputs (like OpenAI’s JSON mode) may still need post-processing.
  * Output parsers help in making responses **consistent, machine-readable, and useful**.
* **Use case:**

  * You ask the model: *“Give me a movie recommendation with title, year, and director.”*
  * The model may give: *“Inception, directed by Christopher Nolan, released in 2010.”*
  * Parser converts it to:

    ```json
    {
      "title": "Inception",
      "year": 2010,
      "director": "Christopher Nolan"
    }
    ```

---

## 🔹 Types of Output Parsers

LangChain provides different parsers depending on the required output:

1. **StrOutputParser** → For plain strings
2. **JSONOutputParser** → For JSON objects
3. **PydanticOutputParser** → For Python objects using Pydantic
4. **StructuredOutputParser** → For custom structured formats
5. *(And more… you can even build your own!)*

---

## 🔹 StrOutputParser

* **Definition:** Returns the model output as a plain string.
* **When to use:** If you just need text.
* This is the simplest parser, as it just takes the string output from the language model and returns it as is.
* It's useful when you don't need to transform the output.
  
* **Example:**

  ```python
  from langchain.schema import StrOutputParser

  parser = StrOutputParser()
  output = parser.parse("Hello World!")
  print(output)  # "Hello World!"
  ```
* **Tip:** Great when you want to send the result of one model **directly into another LLM**.

👉 *One-liner:* "StrOutputParser = Just give me the text."
  
  ```python
   from langchain.prompts import PromptTemplate
   from langchain.chat_models import ChatOpenAI
   from langchain.schema import StrOutputParser
 
   # Initialize the model and parser
   llm = ChatOpenAI(temperature=0)
   output_parser = StrOutputParser()
 
   # Define the prompt
   prompt = PromptTemplate.from_template("Tell me a simple fact about {topic}.") 
 
   # Create a simple chain
   chain = prompt | llm | output_parser 
 
   # Run the chain and print the output
   result = chain.invoke({"topic": "the sun"})
   print(result)
   # Example Output: The Sun is the star at the center of our solar system.
   ```

---

## 🔹 JSONOutputParser

* **Definition:** Converts model output into JSON format.
* **When to use:** If you want key-value data for APIs, databases, or structured storage.
* This parser expects the language model's output to be a valid JSON string. It then parses this string into a Python dictionary.

* **Example:**

  ```python
  from langchain.output_parsers import JSONOutputParser

  parser = JSONOutputParser()
  json_text = '{"title": "Inception", "year": 2010}'
  output = parser.parse(json_text)
  print(output)
  # {'title': 'Inception', 'year': 2010}
  ```

  * This parser expects the language model's output to be a valid JSON string.
  * It then parses this string into a Python dictionary.
  
  ```python
  import json
  from langchain.prompts import PromptTemplate
  from langchain.chat_models import ChatOpenAI
  from langchain_core.output_parsers import JsonOutputParser

  # Initialize the model and parser
  llm = ChatOpenAI(temperature=0)
  parser = JsonOutputParser()

  # Define the prompt, including instructions for the model to generate JSON
  prompt = PromptTemplate.from_template(
      "Return a JSON object with the keys 'name' and 'age' for a person named {person_name} who is {age} years old.\n"
      "Format instructions: {format_instructions}\n"
  )
  formatted_prompt = prompt.partial(format_instructions=parser.get_format_instructions())

  # Create a chain
  chain = formatted_prompt | llm | parser

  # Run the chain and print the output
  result = chain.invoke({"person_name": "Alice", "age": 30})
  print(result)
  # Example Output: {'name': 'Alice', 'age': 30}

  ```

👉 *One-liner:* "JSONOutputParser = Clean JSON every time."

---

## 🔹 PydanticOutputParser

* **Definition:** Parses output into a **Pydantic model** (Python class with validation).
* **When to use:** If you need strong type-checking and validation.
* **Example:**

  ```python
  from pydantic import BaseModel
  from langchain.output_parsers import PydanticOutputParser

  class Movie(BaseModel):
      title: str
      year: int
      director: str

  parser = PydanticOutputParser(pydantic_object=Movie)
  data = '{"title": "Inception", "year": 2010, "director": "Christopher Nolan"}'
  output = parser.parse(data)
  print(output)
  # Movie(title='Inception', year=2010, director='Christopher Nolan')
  ```

  * This parser uses a Pydantic model to define the output structure and automatically generates detailed instructions for the language model.
  * It also validates the output against the schema.
  
  ```python
  from langchain.prompts import PromptTemplate
  from langchain.chat_models import ChatOpenAI
  from langchain.output_parsers import PydanticOutputParser
  from pydantic import BaseModel, Field

  # 1. Define the Pydantic model for the output structure
  class PersonInfo(BaseModel):
      name: str = Field(description="The person's full name.")
      age: int = Field(description="The person's age.")

  # 2. Initialize the parser with the Pydantic model
  parser = PydanticOutputParser(pydantic_object=PersonInfo)

  # 3. Initialize the model and create the prompt
  llm = ChatOpenAI(temperature=0)
  prompt = PromptTemplate(
      template="Answer the user query.\n{format_instructions}\nQuery: {query}\n",
      input_variables=["query"],
      partial_variables={"format_instructions": parser.get_format_instructions()},
  )

  # 4. Create the chain
  chain = prompt | llm | parser

  # 5. Run the chain and print the output
  result = chain.invoke({"query": "Alice is 30 years old."})
  print(result)
  # Example Output:
  # name='Alice' age=30
  # The result is a Pydantic object, not just a dictionary.
  print(type(result))
  # Example Output: <class '__main__.PersonInfo'>
  ```

👉 *One-liner:* "PydanticOutputParser = JSON + Validation Power."

---

## 🔹 StructuredOutputParser

* **Definition:** Lets you **define a schema** for structured output (like JSON with rules).
* **When to use:** If you want custom structured outputs directly from LLMs.
* **Example:**

  ```python
  from langchain.output_parsers import StructuredOutputParser, ResponseSchema

  response_schemas = [
      ResponseSchema(name="title", description="Movie title"),
      ResponseSchema(name="year", description="Release year")
  ]

  parser = StructuredOutputParser.from_response_schemas(response_schemas)
  format_instructions = parser.get_format_instructions()
  print(format_instructions)
  ```
* The model is guided to follow your schema.

👉 *One-liner:* "StructuredOutputParser = Design your own output blueprint."

* This parser lets you define a list of ResponseSchema objects to specify the output structure.
* It's similar to PydanticOutputParser but provides a slightly different, more flexible way to define the schema without a full Pydantic model.
 
```python
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

# 1. Define the response schemas
response_schemas = [
    ResponseSchema(name="city", description="The name of the city."),
    ResponseSchema(name="country", description="The country the city is in."),
    ResponseSchema(name="population", description="The approximate population of the city."),
]

# 2. Initialize the parser with the schemas
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

# 3. Initialize the model and create the prompt
llm = ChatOpenAI(temperature=0)
prompt = PromptTemplate(
    template="Answer the user query in JSON format.\n{format_instructions}\nQuery: {query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": output_parser.get_format_instructions()},
)

# 4. Create the chain
chain = prompt | llm | output_parser

# 5. Run the chain and print the output
result = chain.invoke({"query": "Tell me about London's population."})
print(result)
# Example Output:
# {'city': 'London', 'country': 'United Kingdom', 'population': 'Approximately 9 million'}

```
---

# ✅ Summary

* Output Parsers = Format fixer for LLM outputs.
* Types:

  * **StrOutputParser** → just text
  * **JSONOutputParser** → JSON
  * **PydanticOutputParser** → JSON with validation
  * **StructuredOutputParser** → custom schema
* Helps in: **APIs, databases, pipelines, and chaining models**.

⚡ *Golden Rule:* "If the model talks too freely, use Output Parser to keep it in line!"
