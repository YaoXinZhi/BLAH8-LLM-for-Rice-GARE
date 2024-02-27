

# BLAH8 Project: Bioregulatory Event Extraction Using Large Language Models: A Case Study of Rice Literature


This repository contains the code and data for the paper "Bioregulatory Event Extraction Using Large Language Models: A Case Study of Rice Literature"

## Abstract
Extracting biological regulation events has long been a focal point in the field of biomedical nature language processing (BioNLP). Existing methods often face challenges such as cascading errors in text mining pipelines and topic limitations from the corpus selection. Fortunately, with the emergence of large language models (LLMs), their robust semantic understanding and extensive knowledge background offer a potential solution to alleviate these issues. Towards this goal, during the Biomedical Linked Annotation Hackathon 8 (BLAH 8), this project explores the feasibility of using LLMs for the task of extracting biological regulation events. Taking rice literature as a case, the results indicate promising performance of LLMs in this task, while also emphasizing several challenges that need to be addressed in future work.

**Keywords**: Oryza sativa, bioregulatory event, text mining, large language model, prompt engineering


## Directories
- ```blah_expr_dir```: Contains the original text files.
  
- real-data: Contains the manually annotated gold dataset.
  
- prompt_design: Contains different versions of prompts tested during BLAH8, with base-prompt.v4.2.template.txt being the final version of prompt reported in the paper.

- ChatGPT_result: Contains the generated results of GPT-3.5-turbo and GPT-4.0.

- rice-GARE-gpt-extraction_query_xzyao.py: Used to request OpenAI API and generate results using ChatGPT. The prompt version and ChatGPT version can be selected in the code.
  
- event-generation-evaluation.py: Used to evaluate the generated results.

## Dependencies
- Python 3.7+   
- OpenAI API key  

## Instructions  
1. Clone the repository.  
2. Install the dependencies.  
3. Run rice-GARE-gpt-extraction_query_xzyao.py to generate results using ChatGPT.  
4. Run event-generation-evaluation.py to evaluate the generated results.  


## Citation
If you use this code in your research, please cite the following paper: 
