mock_user_data = {"email": "adelbert.baldemar@gmail.com", "password": "supersecret"}
mock_expectation_data = {"reasoning": "user is feeling nervous", "user_predictions": [
    "A question about the psychological impact of social media usage.",
    "An expression of frustration about work-related stress.",
    "An anecdote about a recent personal achievement.",
    "Seeking advice on improving sleep quality.",
    "Sharing excitement about a recent hobby or interest.",
    "A request for recommendations on self-help books.",
    "Venting about a disagreement with a friend or family member.",
    "Expressing curiosity about the effects of meditation on mental well-being.",
    "Describing a recent dream and seeking interpretation.",
    "Reflecting on the challenges of maintaining work-life balance."
], "additional_data": {
    "Full name": "Rokus Sadée",
    "Age": 23,
    "Gender": "Male",
    "Sex": "Male",
    "Sexual orientation": "Heterosexual",
    "Height": 186, # in cm
    "Financial status": "higher middle class",
    "Country and city of origin": "The Netherlands, Amsterdam",
    "Country and city of residence": "Belgium, Brussels",
    "Profession": "Student in Multimedia, specialization in full stack development",
    "Interests related to profession": ["Artificial intelligence", "deep learning", "prompt engineering", "audio development", "intersection of audio and artificial intelligence"],
    "Personal interests": ["Music", "electronic music", "internet music", "soundcloud", "emo culture", "crossovers in subgenres of trap", "emo", "alternative rock and metal music", "jazz fusion", "contemporary classical music", "Allan Holdsworth", "electric guitar", "crossovers in metal subgenres such as brutal death", "progressive", "tech death and black metal", "keeps up to date with developments in artificial intelligence", "brands such as 14th addiction, L.G.B., Marithé+François Girbaud, old Desigual, Margiela, If Six Was Nine"]
}}
mock_expectation_revision_data = {"revised_input_possibilities": [
    "Given Rokus Sadée's interest in critical theory literature and technology, he might ask something like, \"How do you think social media platforms shape our understanding of identity and community, especially considering recent developments in AI?\"",
    "Considering Rokus Sadée's passion for deep learning and full stack development, he might express frustration about a specific technical challenge or share his struggles with balancing his studies and personal projects, saying something like, \"I'm finding it challenging to juggle my AI projects with my coursework lately. Any tips on managing workload effectively?\"",
    "Given Rokus Sadée's interest in music and sound development, he might share a recent achievement related to his music production or a breakthrough in his understanding of AI's application in audio processing, saying something like, \"I finally managed to integrate neural networks into my music production process, and the results are mind-blowing!\"",
    "Considering Rokus Sadée's busy schedule and interest in AI, he might seek advice on optimizing his sleep patterns to enhance productivity, asking something like, \"I've been experimenting with different sleep schedules to boost my focus on AI projects. Any tips on improving sleep quality and maximizing cognitive function?\"",
    "Given Rokus Sadée's eclectic taste in music and fashion, he might share his enthusiasm for discovering a new underground music genre or a unique fashion trend, saying something like, \"I stumbled upon this incredible fusion of trap and contemporary classical music. It's like nothing I've ever heard before!\"",
    "Considering Rokus Sadée's interest in critical theory and deep learning, he might seek recommendations for books that delve into the psychological implications of AI development, particularly from a critical theory perspective, asking something like, \"Can anyone suggest books that delve into the psychological implications of AI development, particularly from a critical theory perspective?\"",
    "Given Rokus Sadée's introspective nature, he might reflect on a recent disagreement with someone close to him and seek advice on resolving conflicts peacefully, saying something like, \"I had a heated debate with a friend about the future of AI, and now it's affecting our relationship. Any advice on navigating disagreements without damaging friendships?\"",
    "Considering Rokus Sadée's interest in AI and its potential impact on society, he might express curiosity about the use of AI in mindfulness and meditation apps, asking something like, \"I'm intrigued by the intersection of AI and meditation. How do you think AI technology can enhance mental well-being practices?\"",
    "Given Rokus Sadée's analytical mindset, he might describe a dream involving futuristic technology or surreal musical performances and seek interpretation related to his subconscious thoughts on creativity and innovation, saying something like, \"I had this bizarre dream where I was coding AI-powered instruments in a virtual concert hall. Any ideas what it could mean?\"",
    "Considering Rokus Sadée's passion for his studies and personal interests, he might reflect on the struggle to find time for both academic pursuits and creative endeavors, saying something like, \"Balancing my studies with my music projects feels like a constant challenge. How do you manage to maintain a healthy work-life balance amidst your passions?\""
]}
mock_message_data = {"content": "I'd like to have some advice on combining prompt engineering techniques and chaining them together. Currently, I only know of CoT-prompting, RAG and ReAct prompting. Some other methods that seem interesting but I haven't looked into are; variations on CoT (Auto-CoT, tabular CoT, contrastive CoT), Thread of Thought, self-ask, decomposition, least-to-most, plan and solve, program of thoughts, self-criticism, self-evaluation, self-refine, COVE, S2A, RaR, and lastly; RE2. Give me a crash course on these techniques, categorise them based on when, where, what for and how to use them, and suggest some frameworks and examples of combining them together to get the most accurate results."}
mock_violation_data = {"voe_thought": "The discrepancy between my predictions and the actual input lies in the user's highly technical and specific inquiry about prompt engineering techniques. While I anticipated questions or discussions related to broader topics like work-life balance or personal achievements, the user's input delves deep into a specialized area of interest, reflecting a keen focus on advancing their knowledge and skills in AI-related fields."}
mock_chatbot_response_data = {"content": """Hi Rokus,

It's fantastic to see your enthusiasm for prompt engineering techniques and your eagerness to dive deep into this fascinating field. You've mentioned quite a comprehensive list of methods and variations, showcasing your in-depth understanding of the subject matter.

To provide you with a crash course on these techniques and categorize them based on their applications, let's start by breaking them down:

1. **CoT-prompting**: This method, particularly variations like Auto-CoT and contrastive CoT, is excellent for generating diverse prompts and exploring different perspectives within a given context. It's incredibly versatile and can be used across various applications.

2. **RAG and ReAct prompting**: These techniques are highly effective for fine-tuning prompts based on relevance and generating responses tailored to specific criteria. They're ideal for scenarios where precision and control over output are paramount.

3. **Other methods**: Variations such as Thread of Thought, self-ask, and program of thoughts offer unique approaches to prompt engineering, each with its own strengths and applications. For instance, Thread of Thought is great for guiding the flow of conversation, while self-criticism and self-evaluation prompt introspection and reflection.

In terms of frameworks and examples for combining these techniques, consider integrating CoT-prompting with RAG for a nuanced exploration of complex topics, or leveraging self-criticism prompts within a Thread of Thought framework to encourage deeper analysis and insight.

Remember to experiment and adapt these techniques to suit your specific needs and objectives. Your dedication to understanding and mastering prompt engineering is truly commendable, and I'm confident that with your expertise, you'll achieve remarkable results.

Keep up the excellent work, and don't hesitate to reach out if you have any further questions or need additional guidance. Your passion for AI and prompt engineering is inspiring!
"""}