# Customizing AI Models (LLMs)

AI models (Large Language Models or LLMs) know a lot in general.  
Sometimes we want them to do **specific tasks** really well, like answering legal questions or helping with customer support.  

We can **customize** them in two main ways:

1. **Fine-Tuning** – teach the model new skills using examples.  
2. **RAG (Retrieval-Augmented Generation)** – let the model look up relevant info while answering.

---

## 1. Fine-Tuning (Making AI “specialized”)

**What it is:**  
Start with a general AI model and teach it using a smaller, task-specific dataset so it gives answers that match your needs.

**Steps:**  
1. Collect examples and clean the data.  
2. Train the model on this data to adjust it for your task.  
3. Test and improve until it works well.  

**Pros:**  
- Uses the AI’s general knowledge but makes it more accurate for your task.  
- Good for tasks like customer support, technical writing, or legal advice.  
- Saves time because you don’t start from scratch.  

**Cons:**  
- Needs high-quality task-specific data.  
- Can be expensive to train large models.  
- Risk of **overfitting** – the model may fail on new cases.  
- Needs updates as your data changes.

---

### Advanced Fine-Tuning Methods

#### **LoRA (Low-Rank Adaptation)**
- Makes training **faster and cheaper**.  
- Instead of updating all the model’s weights, it updates **small adapter matrices** inside each layer.  
- These small updates allow the model to learn the new task without using a lot of memory or computation.

#### **QLoRA (Quantized LoRA)**
- A more advanced version of LoRA.  
- Works with **very large models** efficiently by combining LoRA with **quantization** (storing numbers in smaller formats).  
- Reduces memory usage and training time even more.

#### **RLHF (Reinforcement Learning from Human Feedback)**
- Improves the model using human feedback.  
- Common in chatbots to make answers more aligned with user preferences.

#### **DPO (Direct Preference Optimization)**
- A simpler alternative to RLHF.  
- Focuses on teaching the AI to give answers humans prefer.  

---

## 2. RAG (Retrieval-Augmented Generation)

**What it is:**  
Instead of changing the AI’s brain, RAG lets it **search documents** while answering questions.  
It combines what the model knows with fresh information from external sources.

**Key parts:**  
- **Retriever:** Finds relevant documents from a database.  
- **Vector store / index:** Organizes documents for quick searching.  
- **Reader / Generator:** The AI uses retrieved info to make its answer.

**Pros:**  
- No need to retrain the AI for new info.  
- Good for fast-changing knowledge or big document collections.  
- Keeps sensitive data separate.  

**Cons:**  
- Quality of answers depends on how good the retrieval is.  
- System is more complex.  
- Can take longer to answer because it has to search first.

**When to use RAG:**  
- You need current or large-scale info without retraining.  
- You want to separate knowledge from the AI itself (for privacy or compliance).  
- You have lots of reliable documents.

---

## Choosing Between Fine-Tuning and RAG

- **Fine-Tuning:** Best for stable tasks with good datasets. AI relies mostly on its own knowledge.  
- **RAG:** Best for changing info or very large document sets. Base model stays unchanged.  
- **Hybrid:** Fine-tune AI for core skills, then use RAG for extra or updated info.

---

## Tips for Practice

**Data:**  
- Fine-tuning: high-quality labeled examples.  
- RAG: maintain a clean, updated document database.

**Tools:**  
- Fine-tuning: Hugging Face, PyTorch, OpenAI APIs.  
- RAG: Vector databases (FAISS, Pinecone, Weaviate), embedding tools, plus the AI model.  

**Evaluation:**  
- Fine-tuning: check accuracy, quality of answers, relevance.  
- RAG: check retrieval accuracy and answer quality.

**Deployment:**  
- Keep models updated with new data.  
- Consider privacy, latency (speed), and cost.  

---

## Examples

- **Fine-Tuning:** Finance chatbot trained on company rules and legal documents.  
- **RAG:** Medical assistant that looks up latest guidelines while answering patient questions.

---

## Common Pitfalls

- **Overfitting:** Model too narrow, fails on new questions.  
- **Data leakage:** Training data contains test answers.  
- **Retrieval errors:** Old or poor documents give wrong answers.  
- **Evaluation gaps:** Use multiple metrics and human checks.

---

## Recommended Starting Points

- New users: Try fine-tuning on a small dataset and RAG on a small document set to compare results.  
- Scaling up: Use LoRA/QLoRA for big models, and combine fine-tuning + RAG for best results.
