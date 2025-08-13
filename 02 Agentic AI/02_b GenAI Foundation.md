# What Multimodal LLMs Are

**LLM** stands for **large language model**.  
**Multimodal** means they can handle more than just text.

## Definition
Multimodal LLMs process and generate information using different data types:
- Text
- Images
- Audio
- Video


## Why This Matters
Real meaning often comes from combining senses — like seeing a picture and reading a description.  
Multimodal models can:
- Understand more context
- Give richer, more accurate responses


## Notable Models and Examples
- **OpenAI**: GPT-4o and Sora (include images in language understanding and responses)
- **DeepMind**: Flamingo
- **Microsoft**: KOSMOS-1

These are part of the push to make AI understand and respond across multiple data kinds.


## How They Work (High-Level)
1. Each data type has its own method of analysis (text, images, etc.).
2. The model combines information from all modalities to:
   - Make a decision
   - Generate a response

**Possible outputs**:
- Text
- Descriptions of pictures
- Answers to questions about images
- Explanations of videos

---

## Primary Advantages
- Combine **visual clues** and **text** for better understanding
- Improve tasks such as:
  - Describing images
  - Answering questions about photos
  - Recommending products based on both pictures and reviews
- Enable richer, more natural interactions (e.g., chatting about a photo you upload)


## Real-World Example
**E-commerce**:  
A model can look at a product image and read customer reviews simultaneously to:
- Suggest similar items
- Explain why a product might be a good fit


## Challenges and Considerations
- **Training complexity**: Needs large, diverse datasets including multiple data types
- **High computational resources**: More data and complexity require more power and money
- **Output quality**: Must remain coherent and useful across all modalities
- **Ethics and safety**: Privacy, copyright, bias, and harmful content risks
- **Alignment**: Ensuring outputs stay consistent and appropriate across different inputs


## Quick Glossary
- **Multimodal**: Able to handle and connect multiple kinds of data (text, images, audio, video)
- **Modality**: A type of data (e.g., text, images)
- **Alignment**: Ensuring the model’s outputs fit user goals and safety standards
- **Computational resources**: Hardware and time needed to train and run models

---

# Types of Models

## Quick History of OpenAI GPT Models
- **GPT-1 (2018)**: 117M parameters. First big success using a transformer on Internet text.  
- **GPT-2 (2019)**: 1.5B parameters. Much bigger and better than GPT-1.  
- **GPT-3 (2020)**: 175B parameters. Enabled a wide range of impressive tasks.  
- **GPT-4 (recent)**: Exact number of parameters not public; rumors say **1T+**.  

**Big investments:**  
- Microsoft invested ~$1B in 2019.  
- Total Microsoft investments now exceed **$13B**.  

---

## What “Types of LLMs” Means
- **Proprietary LLMs**: Made and owned by private companies.  
  *Examples*: OpenAI’s GPT, Anthropic’s Claude, Google’s Gemini.  
- **Open-source LLMs**: Code (and sometimes data) is publicly available.  
- **Small Language Models (SLMs)**: Much smaller than large proprietary or open-source models.

---

## Focus of This Section
Mainly explains **proprietary LLMs** and their **pros/cons**.

---

## Why Proprietary LLMs Are Popular
- **Large money & talent**: Big funding attracts top AI researchers & engineers.  
- **Strong capabilities**: Push boundaries in language tasks.  
- **Developer ecosystem**: APIs, testing tools, documentation.  
- **Cost efficiency at scale**: Use APIs instead of costly hardware.  
- **Comprehensive support**: Docs, tutorials, responsive help.  
- **Ethical & safety focus**: Emphasis on responsible use.  
- **Scalability**: Handles large deployments easily.

---

## Downsides of Proprietary LLMs
- **Limited customization**: Hard to deeply tailor.  
- **Data privacy & security**: Sharing data with a third party can be risky.  
- **Dependence on provider**:  
  - Outages, price hikes, or policy changes can disrupt operations.  
  - *Example*: OpenAI leadership change in late 2023 pushed some users toward alternatives.  
- **Transparency & control**: Training details may be hidden.  
- **Competitive disadvantages**: If others use the same model, advantage can fade.

---

## Quick Takeaways
- **Proprietary LLMs** = power, speed, support.  
- **Trade-offs** = privacy, cost, control issues.  
- **Alternatives** = open-source or small LLMs for more transparency/customization (with more setup work).

---

## Quick Glossary
- **LLM**: Large Language Model – works with text (and sometimes other data).  
- **Proprietary LLM**: Private, company-owned model.  
- **Open-source LLM**: Code/data publicly available.  
- **Small Language Model (SLM)**: Smaller LLM.  
- **Customization**: Adapting a model to specific needs.  
- **Data privacy**: Protecting user data.


# Open-Source LLMs & SLMs — A Game Changer in AI

Open-source **LLMs** (Large Language Models) and **SLMs** (Small Language Models) are like **free, community-built AI brains** that anyone can use, study, and improve.

---

## 📖 The Story of Mistral AI — The Underdogs

In **2023**, three former employees of Google and Meta — **Arthur Mensch**, **Timothée Lacroix**, and **Guillaume Lample** — founded **Mistral AI** in Paris.  
Their mission: **Create efficient, cost-effective, and open-source models**, breaking away from the trend of massive, closed models.

- Years earlier, Arthur Mensch co-authored a research paper on a model called **Chinchilla**, which challenged the “**bigger is always better**” belief in AI.  
- The paper showed that **balance between model size and training data** matters more than just scaling up parameters.

**Impact:**  
Mistral AI's approach worked — attracting **billions of dollars in investment** from companies like **Nvidia** and **Salesforce**.  
They proved that **open-source** and **small language models** can compete with expensive, massive LLMs.

---

## 🔍 Understanding Open-Source LLMs and SLMs

### **Open-Source LLMs**
AI models where:
- **Code** is public.
- **Weights** (learned parameters) are public.
- Sometimes even **training data** is public.

**Pros:**
- 🪟 **Transparent** — You can inspect the internals.
- 🤝 **Collaborative** — Community-driven improvements.
- 🌍 **Democratizing** — Free to use and share.
- 🔐 **Private** — Can run locally without sending data to big tech.

**Cons:**
- ⚡ Require **powerful hardware** (expensive GPUs).
- ⚠️ **Security risks** (e.g., model poisoning).
- ⚙️ **Complex setup** for non-experts.

---

### **Small Language Models (SLMs)**
Compact, efficient AI models with **billions of parameters** (not hundreds of billions).

**Pros:**
- 📱 Run on **everyday devices** (smartphones, laptops).
- 🛠️ Easier to **customize** for specific tasks.
- ⚡ Lower **compute requirements**.

---

## 🌍 Impact and the Future

- **Apple** and others are embedding SLMs in devices for **speed** and **privacy** — no need for constant internet connections.
- **Barriers** still exist:  
  - High hardware costs.  
  - Specialized skills for managing and training models.

**The Future:**
- Thousands of **specialized models** designed for niche tasks.
- **Hybrid systems**:  
  - Cloud-based LLM power.  
  - On-device SLM efficiency.

---

✅ **Key Takeaway:**  
Open-source LLMs and SLMs are reshaping AI — making it **more accessible, private, and specialized** while challenging the dominance of massive, closed models.

