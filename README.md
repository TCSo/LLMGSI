# LLMGSI
The LLMGSI Project is a research project aiming to use large language models (LLM) to simulate realistic office hour (OH) experiences with real GSIs. Except that instead of waiting for long OH queues, students can get almost instant guidance. 

## Repository Structure
```
LLMGSI
│   README.md
│   requirements.txt
│   .gitignore  
└───data (Course specific data)
│   └───hw1_data.json
│   └───hw2_data.json
│   └───...   
└───src (main source code)
│   └───main.py (main entry point for the program)
│   └───query_engines (llamaindex query engines)
│   └───setup_utils.py (setup utilities)
└───storage (Prebuilt retrieval index)
│   └───...
```

## Usage
Clone the repository with
```
git clone https://github.com/TCSo/LLMGSI.git
```
Install all required dependencies with
```
pip install -r requirements.txt
```
Replace "YOUR_OPENAI_API_KEY" in src/setup_utils.py with a valid openAI API key and run make to start the application
```
make run
```
