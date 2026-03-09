import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def read_tasks(filePath):
    with open(filePath, 'r') as f:
        return f.read()
    
def summarize_tasks(tasks):
    prompt = f"""
    You are a smart task planning agent.
    Here is a list of tasks, categorize them into 3 priority levels: 
    - High Priority, 
    - Medium Priority,
    - Low Priority.

    Tasks:
    {tasks}

    Return the summary in the following format:
    High Priority:  
    - Task 1
    - Task 2    
    Medium Priority:
    - Task 3  
    - Task 4          
    Low Priority:
    - Task 5
    - Task 6
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    task_text = read_tasks('tasks.txt')
    summary = summarize_tasks(task_text)
    print("\n Task Summary \n")
    print("-" * 30)
    print(summary)
