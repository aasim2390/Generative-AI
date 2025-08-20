## 📝 Structured Output in LangChain (with_structured_output)

### 🔹 1. What is Structured Output?

Normally, AI replies in free text (like an essay). But computers work better with structured data (like forms or JSON).

**Structured Output = Forcing AI to fill a form you design.**

✅ Example:
```json

{
  "setup": "Why don’t cats play poker?",
  "punchline": "Because they are afraid of the dog’s bark!"
}
```

❌ Not structured:

"The cat joke is: Why don’t cats play poker? Because they are afraid of the dog’s bark!"

💡 One-liner: 

👉 “Structured output is AI filling out forms instead of writing essays.”

---

### 🔹 2. Why do we need Structured Output?

**Consistency** → Always get answers in the same shape.

**Easy for machines** → Can be directly stored in DBs, APIs, Excel, etc.

**Error prevention** → No messy answers like half JSON.

---

### 🔹 3. Where do we use it?

**Data Extraction** → Names, dates, prices from documents.

**Agents** → Agents need structured info to make decisions.

**APIs & Apps** → Apps expect JSON/dicts, not free text.

---

### 🔹 4. Two Approaches in LangChain

1. `with_structured_output()`
   - Works if the model **supports structured output** (e.g. OpenAI GPT models).
   - Best way: ***clean, direct, reliable.***

2. Output Parsers
   - For models that **don’t support structured output.**
   - Adds instructions in the prompt → parses text back into JSON/dict.

---

### 🧑‍💻 5. Code Examples

✅ Example 1: Simple TypedDict
```python
# First, we import some special tools we'll need for this program.
# `TypedDict` is like creating a recipe card that tells us exactly what
# ingredients (or in this case, data) our output should have.
# `Annotated` lets us add a little extra note or description to our ingredients.
from typing_extensions import TypedDict, Annotated

# We also need to import the `ChatOpenAI` tool, which is what we use to talk to
# the AI model. Think of it as a connection to a very smart friend.
from langchain_openai import ChatOpenAI

# Here, we set up our smart friend, the AI. We're telling it to use a
# specific model called "gpt-4o-mini", which is a version of the AI.
llm = ChatOpenAI(model="gpt-4o-mini")

# Now, we create our "recipe card" for the joke.
# We're defining a new type called `JokeDict`.
# It must have two parts:
# 1. `setup`: This is the beginning of the joke, and we use `Annotated`
#    to add a note that says it's the "Beginning of the joke".
# 2. `punchline`: This is the funny ending, and the note says it's
#    "The funny ending".
class JokeDict(TypedDict):
    setup: Annotated[str, "Beginning of the joke"]
    punchline: Annotated[str, "The funny ending"]

# This is the most important part! We're telling the AI that when we ask it
# to do something, we want the result to follow our `JokeDict` recipe card.
# This makes sure the output is always organized in the same way, with a
# clear "setup" and "punchline" every time.
structured_llm = llm.with_structured_output(JokeDict)

# Finally, we ask our newly configured AI to "Tell me a cat joke".
# Because we used `with_structured_output`, the AI knows to give us the
# joke in the exact `setup` and `punchline` format we defined earlier.
# The `print()` command then displays the result on the screen.
print(structured_llm.invoke("Tell me a cat joke"))

```
👉 Output:
```json
{
  "setup": "Why did the cat sit on the computer?",
  "punchline": "Because it wanted to keep an eye on the mouse!"
}
```

---

✅ Example 2: Optional Field (TypedDict)
```python

# We bring in some helpful tools from Python:
# - TypedDict: lets us make a "blueprint" for data (like a form).
# - Annotated: lets us add a short description to each piece of data.
# - NotRequired: marks something as optional (not always needed).
from typing_extensions import TypedDict, Annotated, NotRequired

# We also bring in ChatOpenAI, which is how we talk to the AI model.
# Think of it like a phone line to chat with a really smart robot.
from langchain_openai import ChatOpenAI

# Here we create our AI "friend". We're choosing which brain it should use:
# "gpt-4o-mini" is a smaller but still smart version of the AI.
llm = ChatOpenAI(model="gpt-4o-mini")

# Now we make a "blueprint" for how movie info should look.
# This is called MovieDict.
# Because we used `total=False`, all the fields inside are optional
# (we can give 1, 2, or all 3 pieces of info, and it still works).
class MovieDict(TypedDict, total=False):
    # Movie title (string of text)
    title: Annotated[str, "The name of the movie"]
    # Year the movie was released (whole number)
    year: Annotated[int, "Release year"]
    # Director's name (string of text)
    director: Annotated[str, "The director name"]

# Next, we connect our AI with the MovieDict blueprint.
# This tells the AI: "Whenever you answer, give it back in this exact format."
structured_llm = llm.with_structured_output(MovieDict)

# Finally, we ask our AI friend: "Tell me about Titanic."
# Because we set the blueprint, the answer will come back neatly organized
# into title, year, and director.
# print() just shows the result on the screen.
print(structured_llm.invoke("Tell me about Titanic"))

```

👉 Output:
```json
{
  "title": "Titanic",
  "year": 1997
}

```
---

✅ Example 3: Pydantic with Default & Optional
```python
# We bring in tools from the pydantic library:
# - BaseModel: lets us make a "blueprint" (a fixed shape) for data.
# - Field: lets us add details like a description or a backup value.
from pydantic import BaseModel, Field

# We also bring in ChatOpenAI, which is our way to talk to the AI.
# Think of it as a hotline to chat with a really smart robot.
from langchain_openai import ChatOpenAI

# Here we set up our AI "friend" and tell it which brain to use.
# "gpt-4o-mini" is a smaller but still very smart version of the AI.
llm = ChatOpenAI(model="gpt-4o-mini")

# Now we create a "blueprint" for books.
# We call this class Book, and it uses BaseModel to stay organized.
# This tells the AI exactly what info we want when we ask about a book.
class Book(BaseModel):
    # Title of the book (must always be given, it's required).
    title: str
    # Author of the book (also required).
    author: str
    # Number of pages. If the AI doesn’t know, it will just use 100 by default.
    pages: int = Field(default=100, description="Default 100 if not given")
    # Publisher of the book. This is optional.
    # It can be a text (name of publisher) or None (nothing given).
    publisher: str | None = None

# Next, we connect our AI with the Book blueprint.
# This tells the AI: "Whenever you answer, give it back in this exact book format."
structured_llm = llm.with_structured_output(Book)

# Finally, we ask the AI: "The book is Harry Potter by J.K. Rowling."
# The AI will fill out our Book blueprint with the right info.
# print() shows the result neatly on the screen.
print(structured_llm.invoke("The book is Harry Potter by J.K. Rowling"))

```

👉 Output:

```json
{
  "title": "Harry Potter",
  "author": "J.K. Rowling",
  "pages": 100,
  "publisher": null
}

```
---

✅ Example 4: Optional + Validation (Pydantic)
```python
# First, we install and import some tools from the pydantic library:
# - BaseModel: helps us make a "blueprint" (form) for our data.
# - Field: lets us set rules or default values for data.
# - EmailStr: makes sure a piece of text is a real email address.
from pydantic import BaseModel, Field, EmailStr

# We also bring in ChatOpenAI, which is our way to talk to the AI.
# Think of it like a hotline to a very smart robot.
from langchain_openai import ChatOpenAI

# Here we create our AI "friend" and choose which brain it should use.
# "gpt-4o-mini" is a smaller but still smart version of the AI model.
llm = ChatOpenAI(model="gpt-4o-mini")

# Now we build a "blueprint" for user information.
# We call it UserInfo, and it uses BaseModel to stay neat and organized.
class UserInfo(BaseModel):
    # Name of the user (this is required and must be text).
    name: str
    # Email of the user. This is optional.
    # If given, it must look like a real email (example: test@mail.com).
    email: EmailStr | None = None
    # Age of the user. If not given, it will be set to 18 by default.
    # ge=0 means the age must be 0 or more.
    # le=120 means the age cannot be more than 120.
    age: int = Field(default=18, ge=0, le=120)

# Next, we connect our AI with the UserInfo blueprint.
# This tells the AI: "Whenever you answer, return the info in this format."
structured_llm = llm.with_structured_output(UserInfo)

# Finally, we ask the AI: "My name is Alice."
# The AI will fill out the UserInfo form:
# - name = "Alice"
# - email = None (since no email was given)
# - age = 18 (the default)
# print() shows the filled form on the screen.
print(structured_llm.invoke("My name is Alice"))

```

👉 Output:

```json
{
  "name": "Alice",
  "email": null,
  "age": 18
}

```

✅ Example 5: JSON Schema with Default
```python
# Here we create a "schema" (which is just a set of rules for data).
# Think of it like a form that tells the AI exactly how car info should look.

schema = {
  "title": "CarInfo",  # The name of our form (CarInfo). "Car Info" with space gave an error.
  "type": "object",    # The data should come back as an "object" (like a dictionary).
  "properties": {      # Here we define the details (fields) about the car:
    "brand": {"type": "string"},   # Brand must be text (example: "Tesla").
    "model": {"type": "string"},   # Model must be text (example: "Model S").
    "year": {"type": "integer", "default": 2020},  # Year must be a number, default = 2020 if missing.
    "color": {"type": "string"}    # Color is optional, but if given, it must be text.
  },
  # These are required fields (must always be given).
  "required": ["brand", "model"]
}

# Now we connect our AI with this schema.
# This tells the AI: "Whenever you answer, make sure it follows this car form."
structured_llm = llm.with_structured_output(schema)

# Finally, we ask the AI: "Tell me about Tesla Model S".
# The AI will fill out the form using the schema rules.
# print() shows the organized result on the screen.
print(structured_llm.invoke("Tell me about Tesla Model S"))

```

👉 Output:

```json
{
  "brand": "Tesla",
  "model": "Model S",
  "year": 2020
}

```
---

✅ Example 6: Output Parser (when model doesn’t support)
```python
# We import the tools we need:
# - BaseModel: lets us create a "blueprint" for data (like a form).
# - PydanticOutputParser: helps the AI's answer fit into our blueprint.
# - PromptTemplate: helps us design the message (prompt) we send to the AI.
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate

# Step 1: Create a blueprint for a joke.
# The Joke class has two parts:
# - setup: the beginning of the joke
# - punchline: the funny ending
class Joke(BaseModel):
    setup: str
    punchline: str

# Step 2: Make a parser that takes the AI’s response
# and makes sure it matches the Joke blueprint.
parser = PydanticOutputParser(pydantic_object=Joke)

# Step 3: Create a prompt (the message we send to the AI).
# - template: what we ask the AI ("Tell me a joke").
# - {format_instructions}: special instructions so the AI
#   gives the answer in the exact format our parser needs.
# - input_variables: none here, since we're not filling anything in.
# - partial_variables: we give it the format instructions from our parser.
prompt = PromptTemplate(
    template="Tell me a joke. {format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Step 4: Send the prompt to the AI.
# llm.invoke() asks the AI to tell a joke in the required format.
output = llm.invoke(prompt.format())

# Step 5: Parse the AI’s response.
# parser.parse() takes the AI’s answer and turns it into a Joke object
# with 'setup' and 'punchline' neatly filled in.
print(parser.parse(output.content))

```
---

### ⚖️ 6. Comparison: Which Schema to Use?

| Feature               | **TypedDict**        | **Pydantic**                      | **JSON Schema**              | **Output Parser**            |
| --------------------- | -------------------  | -------------------------------   | --------------------------   | ---------------------------- |
| **Use case**          | Simple, lightweight  | Validation, defaults, safety      | API-like, complex forms      | Models w/o structured output |
| **Optional support**  | `NotRequired`        | `Optional[...]`                   | Field not in `required`      | Yes                          |
| **Default support**   | ❌ No                | ✅ Yes (`Field(default=...)`)    | ✅ Yes (`"default": value`)  | ❌ No                       |
| **Validation**        | ❌ Limited           | ✅ Strong (emails, ranges, etc.) | ✅ Schema-based              | ✅ With Pydantic parser     |
| **Streaming support** | ✅ Yes               | ❌ No                            | ✅ Yes                       | Depends                      |

---

### 🎯 Final One-Liners

**Optional** = “You may leave it blank.”

**Default** = “If you leave it blank, I’ll fill it in for you.”

**TypedDict** = Simple forms.

**Pydantic** = Safe forms with rules.

**JSON Schema** = API contracts.

**Output Parser** = For models that don’t understand structured output.

👉 “With with_structured_output, AI doesn’t just talk—it fills your forms, correctly and safely.”

---
