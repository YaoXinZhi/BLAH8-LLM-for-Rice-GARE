---
title: 'BLAH 8 Report: Rice-Alterome, Regulatory Events Extraction from Annotated Rice Corpus by LLM'
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

# Discussion and/or Conclusion

We recommend to include some discussion or conclusion about your work. Feel free to modify the section title as it fits better to your manuscript.

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
