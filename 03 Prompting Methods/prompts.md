# Prompting Approach, Best Practices, and Examples

## 1. Approach to Prompting
Think of prompting as **talking to a robot who’s super smart but doesn’t guess your mind**.  
You have to be:
- **Clear** → No vague words.
- **Specific** → Tell it exactly what you want.
- **Structured** → Give a format to follow.
- **Step-by-step** → Break down big jobs.

---

## 2. Best Practices

| Best Practice         | Why It Works                     | Example |
|-----------------------|-----------------------------------|---------|
| **Be Specific**       | Avoids vague responses           | ❌ "Tell me about history" → ✅ "Summarize the American Civil War in 5 bullet points" |
| **Give a Role**       | Matches tone & perspective       | "You are a travel guide. Create a 3-day plan for Paris." |
| **Use Step-by-Step**  | Improves reasoning                | "List steps to solve this math problem before giving the answer." |
| **Give Examples**     | Helps AI copy style               | "Write a tweet like: 'Monday mood: coffee before code ☕💻'" |
| **Set Output Format** | Saves editing                     | "Return the answer in a JSON with fields: name, age, hobby." |
| **Ask for Alternatives** | Sparks creativity             | "Suggest 3 catchy slogans for a bakery." |

---

## 3. Types of Prompting with Expanded Examples

### A. Direct Prompting - Simple request.
It means you ask exactly for what you want in a clear and simple way.
You don’t add extra fluff, you don’t give long background stories — you just tell the AI exactly what to do.

> **Example:**  
> "List 5 tallest mountains in the world with their heights."
> 
> "Write the multiplication table of 7."
> 
> "Write a short joke about cats."
---

### B. Role-Based Prompting - Give the AI a persona.
Role-based prompting is when you tell the AI to pretend to be someone with a specific job, skill, or personality before answering your question.
It’s like in drama class — you give the AI a role, and it acts and answers like that character would.

> **Example:**  
> "You are a sports commentator. Describe the last World Cup final in an exciting tone."
>
> "You are a travel guide. Recommend 3 fun places to visit in Tokyo."
>
> "You are a scientist. Explain how solar panels work to a child."
> 

---

### C. Chain-of-Thought Examples
Chain-of-thought prompting means you ask the AI to show the steps it used to get an answer — like asking someone to “show their work” on a math test. It helps you learn how the answer was found, not just the final number.
(Quick note: some AIs won’t share their internal private thinking exactly the same way humans do, but they can give clear, short “worked solutions” or step summaries — which is what we’ll show below.)

> **Example1:**  
> "Explain how you solved: 15% of 200."

> **Example2:**
> 
> Q: The cafeteria had 23 apples. If they used 20 and then bought 6 more, how many apples do they have?
> 
> A: Let's think step-by-step. The cafeteria had 23 apples. They used 20, so 23−20=3. Then they bought 6 more, so 3+6=9. The answer is 9.
> 
> Q: The average weight of a box of apples is 15 pounds. There are 10 apples in each box. If a person buys 3 boxes and each apple weighs the same, what is the weight of one apple?
> 
> A: Let's think step-by-step.

> **Example3:**
> Prompt: "Think step-by-step: Solve the riddle — I’m an even number, greater than 10 and less than 20, my digits add to 5. What am I?" → check candidates, find 14 (1+4=5).

> **Example4:**
> Prompt: “Step-by-step: A train goes 60 km/h for 2.5 hours. How far does it go?” → distance = speed × time = 60 × 2.5 = 150 km.
> 
---

### D. Few-Shot Prompting - Show a few examples first.
Few-shot prompting means you show the AI a few examples of what kind of question-and-answer format you want before asking your real question.
It’s like showing a friend how to play a game by giving them a couple of sample rounds first — then letting them try.

> **Example1:**
> 
> Q: Capital of Italy? → Rome
> 
> Q: Capital of Germany? → Berlin
> 
> Q: Capital of Spain? →

> **Example2:**
> 
> Q: Hello (French) → Bonjour
> 
> Q: Thank you (French) → Merci
> 
> Q: Good night (French) →
---

### E. Instruction + Context Prompting - Give background info.

Instruction + Context prompting is when you:
Tell the AI exactly what to do (the instruction), and
Give background details so it knows how to do it the way you want (the context).

Think of it like telling a friend:
The task: “Write me a short story.”
The context: “It’s for a 5-year-old, and it should be about a talking robot who loves ice cream.”

> **Example1:**  
> "Write a 150-word article about recycling for kids under 12. Use fun examples."

> **Example2:**
> "Describe the water cycle in under 120 words for a science homework project. Use easy words and a friendly tone."
> 
---

### F. Multi-Step Prompting - Ask for answers in sequence.

Multi-step prompting is when you break your request into separate steps, asking the AI to do one step at a time.
It’s like giving a chef:
Step 1: “Chop the vegetables.”
Step 2: “Now cook them in a pan with oil.”
By doing it step-by-step, you get better control over the result.

> **Example1:**
> 
> "Step 1: Give me 3 ideas for a short story.
>
> Step 2: Expand the second idea into a 200-word story."

> **Example2:**
> 
> Step 1: Explain what photosynthesis is in one paragraph.
>
> Step 2: Give me a simple diagram of photosynthesis.  


> **Example3:**
> 
> Step 1: List 5 interesting facts about dolphins.
>
> Step 2: Turn those facts into a fun children’s poem.


---

### G. Creative Constraint Prompting - Set limits for creativity.
Creative constraint prompting is when you tell the AI to be creative but also follow specific limits — like a challenge.
It’s like saying:
“Write a song about pizza… but only use 10 words.”
“Draw a picture using only blue and red.”
The limits make the creativity more fun and unique.

> **Example1:**
> 
> "Write a scary story in exactly 4 sentences."
> 

> **Example2:**
> 
> "Write a poem about rain, but every line must start with the letter R."

> **Example3:**
> 
> "Write a conversation between a robot and a tree, but each can only speak 5 times."
> 

---

### H. Refinement Prompting - Ask for edits.
Refinement prompting is when you give the AI something that already exists (like text, an idea, or a draft) and ask it to improve or change it based on your instructions.
It’s like showing a teacher your essay and saying:
"Can you make it sound better and fix mistakes?"


> **Example 1 – Tone**
>
> "Rewrite this email to sound polite but firm."

> **Example 2 – Length**
>
> "Shorten this story to 50 words without losing the main idea."

> **Example 3 – Vocabulary**
>
> "Replace all difficult words in this paragraph with simpler ones."
> 


---

### I. ReAct Prompting *(Reason + Act)* - The AI reasons step-by-step, then takes an action.
ReAct = Reason + Act. You ask the AI to think briefly about what to do, then pick an action (like Search, Calculate, or Summarize) and actually do it. It’s like: “Hmm — what do I need? → go look it up → give the answer.

> **ReAct Template**
>
> You are a [role]. Problem: [your question].
> 
> Step 1 (brief reason): Decide what kind of action is best (Search / Calculate / Summarize / Ask).
>
> Step 2 (act): Perform that action and return the result with one-sentence explanation.

> 
> **Example1:**
> 
> "You are solving a puzzle. First, think about the problem logically. Then, choose an action from: [Search, Calculate, Summarize].
> 
> Problem: What is the population of Tokyo?"

---

### J. Tree of Thoughts (ToT) - The AI explores multiple reasoning paths, compares them, then picks the best.
Tree of Thoughts means the AI (or you) tries many different ideas (branches), grows each idea a bit to see where it leads, then compares the results and picks the best one — like exploring a tree where each branch is a different plan.

> **ToT Template**
> You are a Tree-of-Thought problem solver.
>
> Problem: [describe problem].
>
> Step 1: List 3–5 different ideas (branches).
>
> Step 2: For each idea, write 2–3 pros, 2–3 cons, and one way to fix each con.
>
> Step 3: Compare the ideas and pick the best one with a short explanation.
>
> Step 4: Give a simple 4–6 step plan to try the chosen idea.



> **Example:**  
> "You are brainstorming ways to improve school lunches. Think of 3 different ideas, list pros and cons for each, then pick the most practical one."

---

## 4. Common Prompting Issues to Avoid

| Mistake                  | Why It’s a Problem         | Fix |
|--------------------------|----------------------------|-----|
| **Being Vague**          | Leads to generic answers   | Be specific with details, limits, and tone. |
| **Too Many Tasks in One Prompt** | Confuses the AI    | Break into smaller prompts. |
| **No Context**           | Output might be off-topic  | Add background info. |
| **No Format**            | Messy output               | Ask for lists, tables, or JSON. |
| **Overstuffing Keywords**| AI gets confused           | Keep language natural. |
| **Ignoring Iteration**   | First answer isn’t always best | Ask for refinements or alternatives. |

---

## 🧠 Memory Hook to remember — "R.I.C.E. P.O.T."
- **R**ole → Tell the AI who it is.  
- **I**nstructions → What to do.  
- **C**ontext → Why/for whom.  
- **E**xamples → Show samples.  
- **P**lan Steps → Break tasks down.  
- **O**utput Format → How to present it.  
- **T**ry Again → Refine the result.
