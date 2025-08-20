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
# First, we import some special tools we'll need for this program.
# `TypedDict` is like creating a recipe card that tells us exactly what
# ingredients (or in this case, data) our output should have.
# `Annotated` lets us add a little extra note or description to our ingredients.
# `NotRequired` is a new tool we're adding to say a field is optional.
from typing_extensions import TypedDict, Annotated, NotRequired

# We also need to import the `ChatOpenAI` tool, which is what we use to talk to
# the AI model. Think of it as a connection to a very smart friend.
from langchain_openai import ChatOpenAI

# Here, we set up our smart friend, the AI. We're telling it to use a
# specific model called "gpt-4o-mini", which is a version of the AI.
llm = ChatOpenAI(model="gpt-4o-mini")

# Now, we create our "recipe card" for a movie.
# We're defining a new type called `MovieDict`.
# It must have three parts:
# 1. `title`: The title of the movie.
# 2. `year`: The year the movie was released.
# 3. `director`: The director of the movie. We use `NotRequired` here to
#    tell the AI that this field is optional, and it's okay if it doesn't
#    provide this information.
class MovieDict(TypedDict):
    title: str
    year: int
    director: NotRequired[str]  # Optional field

# This is the most important part! We're telling the AI that when we ask it
# to do something, we want the result to follow our `MovieDict` recipe card.
# This ensures the output is always organized in the same way.
structured_llm = llm.with_structured_output(MovieDict)

# Finally, we ask our newly configured AI to "Tell me about Titanic".
# Because we used `with_structured_output`, the AI knows to give us the
# movie details in the exact format we defined earlier.
# The `print()` command then displays the result on the screen.
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
# First, we import the tools we'll need from the `pydantic` library.
# `BaseModel` is a powerful tool for creating organized data structures.
# Think of it as a blueprint for how our data should look.
# `Field` lets us add extra details to our blueprint, like a description or a default value.
from pydantic import BaseModel, Field

# We also need to import the `ChatOpenAI` tool to connect to the AI model.
# This is like our connection to a very smart friend.
from langchain_openai import ChatOpenAI

# Here, we set up our smart friend, the AI, telling it to use a
# specific model called "gpt-4o-mini".
llm = ChatOpenAI(model="gpt-4o-mini")

# Now, we create our "blueprint" for a book. We're defining a new class
# called `Book` that uses `BaseModel`.
# This blueprint tells the AI exactly what information we want about a book.
class Book(BaseModel):
    # `title` is a required field and must be a string.
    title: str
    # `author` is also a required field and must be a string.
    author: str
    # `pages` has a default value of 100 if the AI can't find a specific number.
    # The `Field` tool also adds a clear description of what this field is for.
    pages: int = Field(default=100, description="Default 100 if not given")
    # `publisher` is an optional field. The `str | None` part means it can be
    # a string (the publisher's name) or `None` if the information isn't available.
    publisher: str | None = None  # Optional, Default value is None

# This is the most important part! We're telling the AI that when we ask it
# to do something, we want the result to follow our `Book` blueprint.
# This ensures the output is always organized and predictable.
structured_llm = llm.with_structured_output(Book)

# Finally, we ask our newly configured AI about "The book is Harry Potter by J.K. Rowling".
# The AI will try to fill in our `Book` blueprint with the information from this sentence.
# The `print()` command then displays the resulting structured data.
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
# First, we import the tools we'll need from the `pydantic` library.
# `BaseModel` is a powerful tool for creating organized data structures.
# Think of it as a blueprint for how our data should look.
# `Field` lets us add extra details to our blueprint, like a description or a default value.
# `EmailStr` is a special type that ensures a string is a valid email address.
from pydantic import BaseModel, Field, EmailStr

# We also need to import the `ChatOpenAI` tool to connect to the AI model.
# This is like our connection to a very smart friend.
from langchain_openai import ChatOpenAI

# Here, we set up our smart friend, the AI, telling it to use a
# specific model called "gpt-4o-mini".
llm = ChatOpenAI(model="gpt-4o-mini")

# Now, we create our "blueprint" for user information. We're defining a new class
# called `UserInfo` that uses `BaseModel`.
# This blueprint tells the AI exactly what information we want about a user.
class UserInfo(BaseModel):
    # `name` is a required field and must be a string.
    name: str
    # `email` is an optional field. `EmailStr | None` means it can be a valid
    # email string or `None`.
    email: EmailStr | None = None  # Optional but must be valid if present
    # `age` has a default value of 18. We use `Field` to add constraints:
    # `ge=0` means the value must be "greater than or equal to" 0.
    # `le=120` means the value must be "less than or equal to" 120.
    age: int = Field(default=18, ge=0, le=120)

# This is the most important part! We're telling the AI that when we ask it
# to do something, we want the result to follow our `UserInfo` blueprint.
# This ensures the output is always organized and predictable.
structured_llm = llm.with_structured_output(UserInfo)

# Finally, we ask our newly configured AI about "My name is Alice".
# The AI will try to fill in our `UserInfo` blueprint with the information
# from this sentence. It will fill in the `name` and use the default values
# for `age` and `email` since they aren't provided in the prompt.
# The `print()` command then displays the resulting structured data.
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
schema = {
  "title": "Car Info",
  "type": "object",
  "properties": {
    "brand": {"type": "string"},
    "model": {"type": "string"},
    "year": {"type": "integer", "default": 2020},  # Default year
    "color": {"type": "string"}                    # Optional
  },
  "required": ["brand", "model"]
}

structured_llm = llm.with_structured_output(schema)
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
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate

class Joke(BaseModel):
    setup: str
    punchline: str

parser = PydanticOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="Tell me a joke. {format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

output = llm.invoke(prompt.format())
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
