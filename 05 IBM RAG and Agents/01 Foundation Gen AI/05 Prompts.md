# 🧠 Introduction to In-Context Learning & Prompt Engineering  

---

## 🎯 Learning Objectives  
By the end of this lesson, you will be able to:  
- Describe **in-context learning (ICL)**  
- Explain the **fundamentals of prompt engineering**  
- Identify the **key components of a prompt**  

---

## 🔹 What is In-Context Learning?  
- **Definition**: A method of **prompt engineering** where examples of a task are included in the **prompt** (input) given to the model.  
- **How it works**:  
  - The model doesn’t need extra training.  
  - It learns the task from **examples in the prompt** during inference (when it’s generating answers).  

### ✅ Advantages of ICL  
- No need for **fine-tuning** on special datasets.  
- Saves **time and resources**.  
- Improves task performance quickly.  

### ⚠️ Limitations of ICL  
- Limited by how much context can fit in the prompt.  
- Complex tasks may still require **fine-tuning** or traditional training methods (adjusting model weights).  

---

## 🔹 What are Prompts?  
- **Prompts** = Instructions or inputs given to an **LLM** (Large Language Model).  
- They **guide the model** to perform a specific task or generate a desired output.  

### ✨ Two Main Components of a Prompt  
1. **Instructions** – Direct commands that tell the AI *what to do*.  
   - Must be clear and specific.  
   - Example: “Classify this review as positive, negative, or neutral.”  
2. **Context** – Extra background information that helps the AI understand better.  
   - Example: Mention that the review is about a *new product launch*.  

---

## 🔹 Prompt Engineering  
- **Definition**: The process of **designing and refining prompts** to get the most accurate and relevant responses from AI.  
- **Goal**: Not just asking questions, but asking them in the **best possible way**.  

### ✅ Why It’s Important  
- Improves **effectiveness and accuracy**.  
- Ensures **relevant responses**.  
- Helps meet **user expectations**.  
- Reduces need for continuous fine-tuning.  

---

## 🔹 Example: Prompt Breakdown  

**Prompt given to GPT-3.5**:  
> *The product arrived late but the quality exceeded my expectations. Classify the following customer review into neutral, negative, or positive sentiment. Sentiment:*  

### 🔎 Components in this Example  
1. **Instructions** → "Classify the review into neutral, negative, or positive."  
2. **Context** → It’s feedback about a new product.  
3. **Input Data** → "The product arrived late but the quality exceeded my expectations."  
4. **Output Indicator** → "Sentiment:" (tells AI where to put its answer).  

**Expected Output**: Positive ✅  

---

## 📌 Recap  
- **In-Context Learning** = AI learns tasks from examples in the prompt (no fine-tuning needed).  
- **Prompts** = Instructions + Context.  
- **Prompt Engineering** = Crafting prompts for best results.  
- **Four Elements of a Good Prompt**:  
  1. Instructions  
  2. Context  
  3. Input Data  
  4. Output Indicator  
