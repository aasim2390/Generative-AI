# 📘 LangChain Essentials with OpenAI Models

## 1️⃣ What is LangChain?

- A framework to build AI-powered apps using LLMs (Large Language Models).
- Helps integrate language understanding + reasoning + external tools.
- Core building blocks: **Chains, Memory, Agents.**

## 2️⃣ Chains

- **🔗 Definition:** A sequence of steps where each output becomes the next input.
   - **Sequential Chain** = fixed pipeline.
   - **Steps Example:**
       1. Location → Famous dish (China → Peking Duck)
       2. Dish → Recipe (Peking Duck → Recipe)
       3. Recipe → Cooking Time (Recipe → 2 hours)

  ### ✅ How to build:
    - Define prompt template.
    - Create LLMChain using ChatOpenAI.
    - Combine multiple chains into a SequentialChain.
    - Use `verbose=True` to trace execution.

  #### 🧠 Memorable Hook: Chains = Dominoes (fall in order).

  <img width="500" height="274" alt="image" src="https://github.com/user-attachments/assets/c806a800-a101-4d3e-953c-4bdef153789c" />

## 3️⃣ Memory
 - **💾 Definition:** Stores and recalls conversation context.
    - Reads memory before processing.
    - Writes new inputs/outputs after execution.
    - Class: `ChatMessageHistory`, `ConversationBufferMemory`.
  
  ### ✅ Why it matters:
     - Without memory = talking to a stranger.
     - With memory = talking to a friend who remembers yesterday.

  #### 🧠 Memorable Hook: Memory = Diary (keeps history safe).

## 4️⃣ Agents
- **🤖 Definition:** Dynamic decision-makers that pick tools at runtime.
   - **Difference from Chains:**
       - Chains = fixed steps.
       - Agents = flexible, decide which tool/chain to use.

   - Tools they use: Search engines, APIs, databases, Pandas DataFrames.

  ### ✅ Example: Pandas DataFrame Agent
    - Input: "How many rows in the DataFrame?"
    - LLM → writes Python code → executes → returns result.


  #### 🧠 Memorable Hook: Agents = Smart Assistants (choose the right tool).

## 5️⃣ Code Example (Chains + Memory + Agent)

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
```
#### Chain Example 

```python
# -------------------------------------------------------------------------
# 1. Initialize the model (OpenAI GPT)
# -------------------------------------------------------------------------
# llm is the brain (language model) we will ask questions to.
# We use the OpenAI GPT-3.5-turbo model. Temperature=0 means we want very predictable,
# repeatable answers (no randomness).
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# -------------------------------------------------------------------------
# 2. Memory Setup
# -------------------------------------------------------------------------
# A ConversationBufferMemory can store past messages (chat history).
# This is useful if you want the model to remember earlier chats,
# but we won't use it in this simple sequential chain.
# memory = ConversationBufferMemory() # Memory is not used in SequentialChain below

# -------------------------------------------------------------------------
# 3. Chains Example (Sequential Workflow)
# -------------------------------------------------------------------------
# A "Chain" is a mini-step that runs a prompt through the model and gives back an answer.
# Each chain has:
# - input_variables: what you must provide to run this step
# - an output_key: the name used to store the result from this step

# Chain 1: Find a famous dish by location
dish_prompt = PromptTemplate(
    input_variables=["location"],
    template="What is a famous dish in {location}?"
)
# Dish chain: run the dish_prompt, store the answer as "meal"
dish_chain = LLMChain(llm=llm, prompt=dish_prompt, output_key="meal")

# Chain 2: Get the recipe for that dish
recipe_prompt = PromptTemplate(
    input_variables=["meal"],
    template="Give me a simple recipe for {meal}."
)
recipe_chain = LLMChain(llm=llm, prompt=recipe_prompt, output_key="recipe")

# Chain 3: Estimate cooking time for the recipe
time_prompt = PromptTemplate(
    input_variables=["recipe"],
    template="Estimate the cooking time for this recipe: {recipe}"
)
time_chain = LLMChain(llm=llm, prompt=time_prompt, output_key="time")

# Combine all 3 chains into one sequential pipeline
# The SequentialChain runs each chain in order, passing outputs along:
# - The first chain uses the provided input
# - The second chain uses the first chain's "meal" output as its input
# - The third chain uses the second chain's "recipe" output as its input
food_chain = SequentialChain(
    chains=[dish_chain, recipe_chain, time_chain],
    input_variables=["location"],           # User provides a location (e.g., "China")
    output_variables=["meal", "recipe", "time"], # Final outputs from the whole chain
    verbose=True,                           # Show detailed steps as it runs (helpful for learning)
)

# Run the chain: ask about a famous dish in China
print("\n--- Running Chain Example ---")
print(food_chain.invoke({"location": "China"}))
```

```bash

--- Running Chain Example ---


> Entering new SequentialChain chain...

> Finished chain.
{'location': 'China', 'meal': 'One famous dish in China is Peking duck, which is a traditional dish from Beijing. It is a roasted duck dish that is prized for its crispy skin and tender meat. Peking duck is often served with thin pancakes, scallions, cucumber, and hoisin sauce, and is considered a delicacy in Chinese cuisine.', 'recipe': 'Ingredients:\n- 1 whole duck\n- 1 tablespoon honey\n- 1 tablespoon soy sauce\n- 1 tablespoon hoisin sauce\n- 1 teaspoon five-spice powder\n- Salt and pepper to taste\n- Thin pancakes\n- Sliced scallions\n- Sliced cucumber\n\nInstructions:\n1. Preheat the oven to 375°F (190°C).\n2. Clean the duck and pat it dry with paper towels.\n3. In a small bowl, mix together the honey, soy sauce, hoisin sauce, five-spice powder, salt, and pepper.\n4. Brush the duck with the sauce mixture, making sure to coat it evenly.\n5. Place the duck on a roasting rack in a roasting pan and roast in the oven for about 1.5-2 hours, or until the skin is crispy and the meat is tender.\n6. Remove the duck from the oven and let it rest for 10-15 minutes before carving.\n7. To serve, slice the duck and serve with thin pancakes, sliced scallions, sliced cucumber, and hoisin sauce.\n8. To eat, place a slice of duck, some scallions, and cucumber on a pancake, drizzle with hoisin sauce, and roll it up like a burrito.\n9. Enjoy your homemade Peking duck!', 'time': 'The estimated cooking time for this recipe is about 1.5-2 hours.'}
```

#### Agent Example
```python
# -------------------------------------------------------------------------
# 4. Agent Example (Dynamic Tool Usage)
# -------------------------------------------------------------------------
# Agents decide what action/tool to use dynamically.
# Example: Pandas DataFrame Agent that can answer questions on data.

# Import pandas to work with tabular data (DataFrame)
import pandas as pd  # standard alias for pandas

# Create a small DataFrame (a table) with two columns: Name and Score
df = pd.DataFrame({"Name": ["John", "Bob"], "Score": [88, 92]})

# Create an agent that can query the DataFrame using natural language
# - llm: the language model we already set up earlier (gpt-like brain)
# - df: the DataFrame we want to query with natural language questions
# - verbose=True: print extra internal steps so you can see how it works
# - allow_dangerous_code=True: allow the agent to generate and run Python code
#   (use with caution; this can be risky if used with unknown input)
agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)

# Ask a question in plain English → the agent converts it to Python code internally
print("\n--- Running Agent Example ---")
print(agent.invoke({"input": "What is the average score?"}))
```

```bash
--- Running Agent Example ---


> Entering new AgentExecutor chain...
Thought: To find the average score, we need to calculate the mean of the 'Score' column in the dataframe.
Action: python_repl_ast
Action Input: df['Score'].mean()90.0The average score is 90.0.
Final Answer: 90.0

> Finished chain.
{'input': 'What is the average score?', 'output': '90.0'}
```

#### Memory Example
```python
# Step 1: Import the necessary building blocks
from langchain_openai import ChatOpenAI          # The "brain" we ask questions to (a chat model)
from langchain.chains import ConversationChain  # A chain that keeps a back-and-forth chat
from langchain.memory import ConversationBufferMemory  # Keeps track of past messages in memory

# Step 1: Initialize LLM
# Create the language model object with a chosen model and creativity level
# - model="gpt-4o-mini": which version of the model to use (smaller, faster)
# - temperature=0.7: how creative/different the answers can be (0.0 = deterministic)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Step 2: Add memory so it remembers the conversation
# ConversationBufferMemory stores the chat history in memory.
# return_messages=True means the memory will provide the history back to the chain
memory = ConversationBufferMemory(return_messages=True)

# Step 3: Create the chain
# A ConversationChain ties together the LLM and the memory to handle a back-and-forth chat.
conversation = ConversationChain(llm=llm, memory=memory)

# Step 4: Interact (memory remembers previous inputs/outputs)
# We ask the model to suggest a dish, then ask for a recipe, then ask about cooking time.
print(conversation.invoke({"input": "Suggest a Chinese dish."}))
print(conversation.invoke({"input": "Give me the recipe."}))
print(conversation.invoke({"input": "How long will it take to cook?"}))
```

```bash
{'input': 'Suggest a Chinese dish.', 'history': [HumanMessage(content='Suggest a Chinese dish.', additional_kwargs={}, response_metadata={}), AIMessage(content="How about trying Kung Pao Chicken? It's a classic Sichuan dish made with diced chicken that's stir-fried with peanuts, vegetables, and a spicy sauce made from soy sauce, vinegar, and chili peppers. It's known for its bold flavors and a perfect balance of heat and sweetness. Plus, it's often served with steamed rice, which complements the dish nicely. Would you like to know how to make it?", additional_kwargs={}, response_metadata={})], 'response': "How about trying Kung Pao Chicken? It's a classic Sichuan dish made with diced chicken that's stir-fried with peanuts, vegetables, and a spicy sauce made from soy sauce, vinegar, and chili peppers. It's known for its bold flavors and a perfect balance of heat and sweetness. Plus, it's often served with steamed rice, which complements the dish nicely. Would you like to know how to make it?"}
{'input': 'Give me the recipe.', 'history': [HumanMessage(content='Suggest a Chinese dish.', additional_kwargs={}, response_metadata={}), AIMessage(content="How about trying Kung Pao Chicken? It's a classic Sichuan dish made with diced chicken that's stir-fried with peanuts, vegetables, and a spicy sauce made from soy sauce, vinegar, and chili peppers. It's known for its bold flavors and a perfect balance of heat and sweetness. Plus, it's often served with steamed rice, which complements the dish nicely. Would you like to know how to make it?", additional_kwargs={}, response_metadata={}), HumanMessage(content='Give me the recipe.', additional_kwargs={}, response_metadata={}), AIMessage(content='Sure! Here’s a simple recipe for Kung Pao Chicken:\n\n### Ingredients:\n- **For the marinade:**\n  - 1 pound (450g) boneless, skinless chicken thighs or breasts, diced\n  - 2 tablespoons soy sauce\n  - 1 tablespoon Chinese rice wine (or dry sherry)\n  - 1 teaspoon cornstarch\n\n- **For the stir-fry:**\n  - 3 tablespoons vegetable oil (divided)\n  - 3-4 dried red chili peppers (adjust to taste)\n  - 3 cloves garlic, minced\n  - 1-inch piece of ginger, minced\n  - 1 bell pepper (red or green), diced\n  - 1/2 cup unsalted roasted peanuts\n  - 2 green onions, chopped (white and green parts separated)\n\n- **For the sauce:**\n  - 3 tablespoons soy sauce\n  - 1 tablespoon rice vinegar\n  - 1 tablespoon sugar\n  - 1 tablespoon hoisin sauce (optional)\n  - 1 teaspoon sesame oil\n\n### Instructions:\n\n1. **Marinate the Chicken:**\n   - In a bowl, combine the diced chicken with soy sauce, rice wine, and cornstarch. Mix well and let it marinate for about 15-30 minutes.\n\n2. **Prepare the Sauce:**\n   - In a small bowl, whisk together the soy sauce, rice vinegar, sugar, hoisin sauce (if using), and sesame oil. Set aside.\n\n3. **Stir-Fry:**\n   - Heat 2 tablespoons of vegetable oil in a large skillet or wok over medium-high heat. \n   - Add the dried red chili peppers and stir-fry for about 30 seconds until fragrant.\n   - Add the marinated chicken and cook until browned and cooked through, about 5-7 minutes. Remove the chicken from the pan and set aside.\n   \n4. **Add Vegetables:**\n   - In the same pan, add the remaining tablespoon of oil. Add the minced garlic, ginger, and diced bell pepper. Stir-fry for 2-3 minutes until the vegetables are tender but still crisp.\n\n5. **Combine:**\n   - Return the cooked chicken to the pan along with the peanuts and the prepared sauce. Stir well to coat everything in the sauce and cook for another 2-3 minutes until heated through.\n\n6. **Finish:**\n   - Add the chopped green onions (white parts) and stir to combine. Cook for an additional minute.\n   - Serve hot over steamed rice and garnish with the green onion tops.\n\nEnjoy your homemade Kung Pao Chicken! If you have any questions about the recipe or need variations, feel free to ask!', additional_kwargs={}, response_metadata={})], 'response': 'Sure! Here’s a simple recipe for Kung Pao Chicken:\n\n### Ingredients:\n- **For the marinade:**\n  - 1 pound (450g) boneless, skinless chicken thighs or breasts, diced\n  - 2 tablespoons soy sauce\n  - 1 tablespoon Chinese rice wine (or dry sherry)\n  - 1 teaspoon cornstarch\n\n- **For the stir-fry:**\n  - 3 tablespoons vegetable oil (divided)\n  - 3-4 dried red chili peppers (adjust to taste)\n  - 3 cloves garlic, minced\n  - 1-inch piece of ginger, minced\n  - 1 bell pepper (red or green), diced\n  - 1/2 cup unsalted roasted peanuts\n  - 2 green onions, chopped (white and green parts separated)\n\n- **For the sauce:**\n  - 3 tablespoons soy sauce\n  - 1 tablespoon rice vinegar\n  - 1 tablespoon sugar\n  - 1 tablespoon hoisin sauce (optional)\n  - 1 teaspoon sesame oil\n\n### Instructions:\n\n1. **Marinate the Chicken:**\n   - In a bowl, combine the diced chicken with soy sauce, rice wine, and cornstarch. Mix well and let it marinate for about 15-30 minutes.\n\n2. **Prepare the Sauce:**\n   - In a small bowl, whisk together the soy sauce, rice vinegar, sugar, hoisin sauce (if using), and sesame oil. Set aside.\n\n3. **Stir-Fry:**\n   - Heat 2 tablespoons of vegetable oil in a large skillet or wok over medium-high heat. \n   - Add the dried red chili peppers and stir-fry for about 30 seconds until fragrant.\n   - Add the marinated chicken and cook until browned and cooked through, about 5-7 minutes. Remove the chicken from the pan and set aside.\n   \n4. **Add Vegetables:**\n   - In the same pan, add the remaining tablespoon of oil. Add the minced garlic, ginger, and diced bell pepper. Stir-fry for 2-3 minutes until the vegetables are tender but still crisp.\n\n5. **Combine:**\n   - Return the cooked chicken to the pan along with the peanuts and the prepared sauce. Stir well to coat everything in the sauce and cook for another 2-3 minutes until heated through.\n\n6. **Finish:**\n   - Add the chopped green onions (white parts) and stir to combine. Cook for an additional minute.\n   - Serve hot over steamed rice and garnish with the green onion tops.\n\nEnjoy your homemade Kung Pao Chicken! If you have any questions about the recipe or need variations, feel free to ask!'}
{'input': 'How long will it take to cook?', 'history': [HumanMessage(content='Suggest a Chinese dish.', additional_kwargs={}, response_metadata={}), AIMessage(content="How about trying Kung Pao Chicken? It's a classic Sichuan dish made with diced chicken that's stir-fried with peanuts, vegetables, and a spicy sauce made from soy sauce, vinegar, and chili peppers. It's known for its bold flavors and a perfect balance of heat and sweetness. Plus, it's often served with steamed rice, which complements the dish nicely. Would you like to know how to make it?", additional_kwargs={}, response_metadata={}), HumanMessage(content='Give me the recipe.', additional_kwargs={}, response_metadata={}), AIMessage(content='Sure! Here’s a simple recipe for Kung Pao Chicken:\n\n### Ingredients:\n- **For the marinade:**\n  - 1 pound (450g) boneless, skinless chicken thighs or breasts, diced\n  - 2 tablespoons soy sauce\n  - 1 tablespoon Chinese rice wine (or dry sherry)\n  - 1 teaspoon cornstarch\n\n- **For the stir-fry:**\n  - 3 tablespoons vegetable oil (divided)\n  - 3-4 dried red chili peppers (adjust to taste)\n  - 3 cloves garlic, minced\n  - 1-inch piece of ginger, minced\n  - 1 bell pepper (red or green), diced\n  - 1/2 cup unsalted roasted peanuts\n  - 2 green onions, chopped (white and green parts separated)\n\n- **For the sauce:**\n  - 3 tablespoons soy sauce\n  - 1 tablespoon rice vinegar\n  - 1 tablespoon sugar\n  - 1 tablespoon hoisin sauce (optional)\n  - 1 teaspoon sesame oil\n\n### Instructions:\n\n1. **Marinate the Chicken:**\n   - In a bowl, combine the diced chicken with soy sauce, rice wine, and cornstarch. Mix well and let it marinate for about 15-30 minutes.\n\n2. **Prepare the Sauce:**\n   - In a small bowl, whisk together the soy sauce, rice vinegar, sugar, hoisin sauce (if using), and sesame oil. Set aside.\n\n3. **Stir-Fry:**\n   - Heat 2 tablespoons of vegetable oil in a large skillet or wok over medium-high heat. \n   - Add the dried red chili peppers and stir-fry for about 30 seconds until fragrant.\n   - Add the marinated chicken and cook until browned and cooked through, about 5-7 minutes. Remove the chicken from the pan and set aside.\n   \n4. **Add Vegetables:**\n   - In the same pan, add the remaining tablespoon of oil. Add the minced garlic, ginger, and diced bell pepper. Stir-fry for 2-3 minutes until the vegetables are tender but still crisp.\n\n5. **Combine:**\n   - Return the cooked chicken to the pan along with the peanuts and the prepared sauce. Stir well to coat everything in the sauce and cook for another 2-3 minutes until heated through.\n\n6. **Finish:**\n   - Add the chopped green onions (white parts) and stir to combine. Cook for an additional minute.\n   - Serve hot over steamed rice and garnish with the green onion tops.\n\nEnjoy your homemade Kung Pao Chicken! If you have any questions about the recipe or need variations, feel free to ask!', additional_kwargs={}, response_metadata={}), HumanMessage(content='How long will it take to cook?', additional_kwargs={}, response_metadata={}), AIMessage(content="The total time to cook Kung Pao Chicken is approximately 30-45 minutes. Here's a breakdown:\n\n1. **Marinating the Chicken:** 15-30 minutes (you can marinate for as little as 15 minutes, but longer is better for flavor).\n2. **Preparation of Ingredients:** 10 minutes (chopping vegetables and preparing the sauce).\n3. **Cooking Time:** About 10-15 minutes for stir-frying everything.\n\nSo, if you combine all these steps, you're looking at around 30-45 minutes from start to finish. Let me know if you have any other questions!", additional_kwargs={}, response_metadata={})], 'response': "The total time to cook Kung Pao Chicken is approximately 30-45 minutes. Here's a breakdown:\n\n1. **Marinating the Chicken:** 15-30 minutes (you can marinate for as little as 15 minutes, but longer is better for flavor).\n2. **Preparation of Ingredients:** 10 minutes (chopping vegetables and preparing the sauce).\n3. **Cooking Time:** About 10-15 minutes for stir-frying everything.\n\nSo, if you combine all these steps, you're looking at around 30-45 minutes from start to finish. Let me know if you have any other questions!"}
```

## 6️⃣ Recap – Quick Recall Formula
  - **Chains** = Dominoes → Step-by-step flow.
  - **Memory** = Diary → Keeps history.
  - **Agents** = Smart Assistant → Chooses tools dynamically.
  - **OpenAI GPT Models** → Power the whole system.
