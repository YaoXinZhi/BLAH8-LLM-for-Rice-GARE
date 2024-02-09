---
title: 'Biomedical Linked Annotation Hackathon 8: Rice-Alterome, Regulatory Events Extraction from Annotated Rice Corpus by LLM'
tags:
  - Oryza sativa
  - regulatory event
  - text mining
  - large language model
  - prompt engineering
authors:
  - name: Xinzhi Yao
    orcid: 0000-0001-6795-2653
    affiliation: 1
  - name: Jingbo Xia
    orcid: 0000-0002-7285-588X
    affiliation: 1
affiliations:
 - name: College of Informatics, Hubei Key Laboratory of Agricultural Bioinformatics, Huazhong Agricultural University, Wuhan, China
   index: 1
date: 15 January 2024
bibliography: paper.bib
authors_short: Yao \emph{et al.}
group: HZAU-BioNLP
event: Biomedical Linked Annotation Hackathon 8
---

# Introduction or Background


Rice, as the most important staple crop in Asia, has garnered significant attention in precision breeding research. The study of precise breeding in rice is crucial due to the potential alterations in downstream biological processes or plant traits caused by mutations in rice genes. In recent years, a plethora of research papers in the field of rice have been published, and with the continuous advancement of natural language processing technology, automated collection and organization of knowledge from literature have become feasible.

Traditional natural language processing methods typically rely on multi-step text mining pipelines, including named entity recognition, entity normalization, relationship extraction, etc. However, these methods often face two major challenges. Firstly, the implementation strategy based on pipelines often encounters the issue of cascading error propagation. This means that errors generated in one step may be further propagated in subsequent steps. Secondly, the implementation of these steps, in the era of deep learning, usually relies on large and precise manually annotated corpora, which are undeniably difficult to prepare, especially for specialized domains such as rice.

Fortunately, in recent years, the emergence of large language models has demonstrated powerful language understanding and extensive domain knowledge. This implies that often only simple prompts need to be provided, and the language model can respond to specific questions accordingly. The quality of the response largely depends on the design of the prompt, giving rise to the development strategy of prompt engineering for large models.

As an invited presentation at the Biomedical Linked Annotation Hackathon 8 (BLAH8), the topic "Rice-Alterome, Regulatory Events Extraction from Annotated Rice Corpus by LLM" explores the implementation strategy of prompt engineering based on the Rice-Alterome annotation corpus previously constructed by the team. This project aims to develop large language models (LLMs) for the task of mining regulatory events caused by genetic mutations in the field of rice. The results indicate that LLMs can achieve significant effectiveness in this task through appropriate prompt design. Specifically, GPT-3.5-turbo achieves a precision of 0.7470, a recall of 0.5041, and an F1 score of 0.6019, while GPT-4 achieves a precision of 0.7925, a recall of 0.4970, and an F1 score of 0.6109.

## Materials and methods
In this section, we will describe the preliminary preparation work for BLAH8, including the preparation of the rice annotation corpus and task definition, as well as the progress of the project during the BLAH8 conference, including prompt engineering, experimental setup, and results evaluation.


### Annotated Rice Corpus
The project is based on our previously developed rice annotation corpus, Rice-Alterome. Specifically, within the Rice-Alterome corpus, we adopted the definition of genetic alteration caused regulatory events (GARE) from the Active Gene Annotation Corpus (AGAC). We employed conventional text mining pipelines, including Named Entity Recognition (NER), Named Entity Normalization (NEN), Relationship Extraction (RE), and rule-based GARE identification. The final Rice-Alterome corpus comprises 1080 annotated GARE instances.


### Task Definition

As mentioned earlier, conventional text mining pipelines often lead to cascading error accumulation, and the specificity of rice domain text further complicates the construction of Rice-Alterome based on pipelines. Therefore, during BLAH8, we plan to leverage the powerful semantic understanding and extensive knowledge background of LLMs, combined with prompt engineering strategies, to extract rice genetic alteration caused regulatory events (rice-GARE) from rice literature. Specifically, we intend to provide only raw text without any additional NER, NEN, or RE knowledge and directly output structured rice-GARE knowledge using LLMs.

### Experimental Setup

In this project, we utilized the OpenAI API to make requests to GPT-3.5-turbo and GPT-4. The API requests were implemented using the OpenAI Python library. The complete code for making requests and usage instructions can be found in the GitHub repository associated with the project.

### Prompt Engineering

During the BLAH8 conference, we designed and experimented with different versions of prompts for requesting responses from the OpenAI API. The final version of the prompt, as illustrated in Figure *, consists of five components:


* **Task Defination**: This part is used to prompt GPT to understand the task it needs to accomplish and define the concepts involved. For example, it prompts GPT to extract GARE and provides the specific definition of GARE.


* **Extraction Rules**: This component defines the specific extraction rules for the task, such as ensuring that each GARE instance contains only one independent gene.

* **Format Require**: It prompts GPT to return results in a specific format, facilitating further analysis and evaluation of the results.

* **Empty Sentences**: These sentences are provided to GPT for GARE extraction.

* **Examples**: Several annotated examples are provided to GPT. It is essential to select examples with sufficient distinctiveness and representativeness to help GPT better understand the task requirements.


### Result Evaluation
To assess the direct generation results of GPT, we manually annotated 70 sentences to create a benchmark dataset. Among these, 50 sentences were designated as positive samples, containing a total of 89 annotated GARE instances, while 20 sentences were designated as negative samples, not containing any GARE descriptions.

We evaluated the performance of GPT by directly using its generated results for assessment. The results are presented in Table *, showing that GPT-3.5-turbo and GPT-4 perform similarly in terms of F1-score. However, GPT-4 achieved higher precision, while GPT-3.5-turbo demonstrated better recall. It is noteworthy that in tasks involving knowledge extraction for knowledge base construction, we often prioritize higher precision to ensure the authenticity and accuracy of the extracted knowledge, even though this may result in lower recall.

To better understand the generated results of GPT and design a more reasonable evaluation scheme, we conducted manual inspections of the generated results. During this process, we identified several interesting cases:

··· # wait to update

LLM mistake: Negation or Long-distance inference
28338653 TP53 mutations were exclusive to high grade DCIS and more frequent in PR-negative tumors compared with PR-positive tumors (P=0.037).
TP53 -- mutations -- exclusive to(Reg) -- high grade DCIS

Different with gold, but meanful
28338653 However, an increase in GATA3 mutations and fewer copy number changes were noted in DCIS compared with invasive carcinomas.
GATA3 -- mutations -- increase (PosReg) -- DCIS


17873349 We have investigated the role of Notch in a pre-invasive breast lesion, ductal carcinoma in situ (DCIS), and have found that aberrant activation of Notch signalling is an early event in breast cancer.
Notch -- aberrant activation -- early event in (Reg) -- breast cancer

···

Based on the adjusted evaluation metrics, we obtained the metrics shown in Table *. It can be observed that both versions of GPT have achieved more promising results, particularly with GPT-4 achieving a precision of 0.79.

# Discussion and/or Conclusion

This project leveraged a fascinating attempt with BLAH8 to explore whether large language models (LLMs) have the capability to surpass traditional, cumbersome multi-step NLP pipelines solely through prompt engineering. The results demonstrated promising outcomes, suggesting the potential for further improvement with prompt engineering. However, limitations in corpus size and narrow thematic scope pose challenges to generalizability, a problem likely alleviated by LLMs. Specifically, the AGAC corpus utilized in this project illustrates these limitations. With only 250 manually annotated abstracts, leveraging deep learning to fully exploit AGAC's knowledge or extend it to full-text annotation presents challenges. The outcomes of public evaluations such as OST-19 and CHIP-23 highlight these challenges, where the top-performing team achieved only * F-score in NER tasks and * F-score in RE tasks. Additionally, AGAC is tailored to human diseases, particularly cancer and Alzheimer's, meaning its effectiveness diminishes significantly when applied to other topics such as plants. However, as demonstrated by LLM's robust understanding of few-shot datasets and its transferability to rice-related contexts, LLMs hint at the potential to mitigate these challenges by tapping into valuable knowledge from diverse corpora like GENIA, which focuses on regulatory events, as well as other corpora addressing various topics.

Furthermore, we attempted to use LLMs to cover the NEN steps in this project but ultimately abandoned this approach. Our experiments revealed that NEN tasks typically require a vast and accurate dictionary for entity normalization, such as the NCBI Gene dictionary, Gene Ontology, or Human Phenotype Ontology. However, teaching an LLM to memorize and accurately map concepts to IDs is exceedingly difficult. One intuitive example is the inability to provide such a large dictionary within the prompt due to token limitations. Even when we tried to shrink the dictionary to fit within the prompt sent to GPT, the model still struggled to remember all mappings, resulting in frequent errors and even hallucinations of non-existent IDs, a phenomenon often referred to as LLM hallucinations. Fortunately, tools and platforms like LangChain that offer additional association extensions to LLMs are continuously evolving, suggesting that this issue will likely be mitigated soon.


In conclusion, traditional NLP methods and tools will undoubtedly face challenges in the era of LLMs. However, this disruption is promising, as works like this project, which utilize prompt engineering to explore the potential of LLMs in the BioNLP domain, are expected to yield more hopeful outcomes.


## Subsection level 2

Please keep sections to a maximum of three levels, even better if only two levels.

### Subsection level 3

Please keep sections to a maximum of three levels.

## Tables, figures and so on

Please remember to introduce tables (see Table 1) before they appear on the document. We recommend to center tables, formulas and figure but not the corresponding captions. Feel free to modify the table style as it better suits to your data.

Table 1
| Header 1 | Header 2 |
| -------- | -------- |
| item 1 | item 2 |
| item 3 | item 4 |

Remember to introduce figures (see Figure 1) before they appear on the document. 

![BioHackrXiv logo](./biohackrxiv.png)
 
Figure 1. A figure corresponding to the logo of our BioHackrXiv preprint.

# Other main section on your manuscript level 1

Feel free to use numbered lists or bullet points as you need.
* Item 1
* Item 2


# Future work

And maybe you want to add a sentence or two on how you plan to continue. Please keep reading to learn about citations and references.

For citations of references, we prefer the use of parenthesis, last name and year. If you use a citation manager, Elsevier – Harvard or American Psychological Association (APA) will work. If you are referencing web pages, software or so, please do so in the same way. Whenever possible, add authors and year. We have included a couple of citations along this document for you to get the idea. Please remember to always add DOI whenever available, if not possible, please provide alternative URLs. You will end up with an alphabetical order list by authors’ last name.

# Jupyter notebooks, GitHub repositories and data repositories

* Please add a list here
* Make sure you let us know which of these correspond to Jupyter notebooks. Although not supported yet, we plan to add features for them
* And remember, software and data need a license for them to be used by others, no license means no clear rules so nobody could legally use a non-licensed research object, whatever that object is

# Acknowledgements
Please always remember to acknowledge the BioHackathon, CodeFest, VoCamp, Sprint or similar where this work was (partially) developed.

# References

Leave thise section blank, create a paper.bib with all your references.
