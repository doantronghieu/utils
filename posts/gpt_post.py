from langchain.schema import StrOutputParser
from tqdm import tqdm

from langchain import PromptTemplate, OpenAI
from config import set_environment
set_environment()

file_path = 'crawled_text.txt'

# Read the content of the file
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Split the content into paragraphs based on the newline character
paragraphs = content.split('\\x')

# Remove empty paragraphs
paragraphs = [paragraph.strip()
              for paragraph in paragraphs if paragraph.strip()]


# Your OpenAI setup
llm = OpenAI(model='gpt-3.5-turbo-instruct')
prompt_template = PromptTemplate.from_template(
"""Optimize and compact the paragraph by eliminating inappropriate line breaks, unnecessary words, suggestions/invitations/collaborative words, pronouns, conjunctions, prepositions and adverbs:
{text}"""

)
# prompt_template = PromptTemplate.from_template(
#     """
#     Remove inappropriate carriage return characters, remove unnecessary words/pronouns/adverbs, and rewrite this content to make this more compact:
#     {text}
#     """
# )
output_parser = StrOutputParser()

# Iterate over paragraphs and generate summaries
summaries = []
for paragraph in tqdm(paragraphs):
    # Skip empty paragraphs
    if not paragraph.strip():
        continue

    # Generate summary using OpenAI
    runnable = prompt_template | llm | output_parser
    summary = runnable.invoke({'text': paragraph})

    # Append the summary to the list
    summaries.append(summary)

# Append summaries to the output file
output_file_path = 'post_summary.txt'
with open(output_file_path, 'a', encoding='utf-8') as output_file:
    for summary in tqdm(summaries):
        output_file.write(summary + '\n')

print(f'Summaries appended to {output_file_path}')
