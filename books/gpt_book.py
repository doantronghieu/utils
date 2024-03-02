from langchain.schema import StrOutputParser
from tqdm import tqdm

from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from config import set_environment
set_environment()

file_path = 'llm_input.txt'

# Read the content of the file
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Split the content into paragraphs based on the newline character
paragraphs = content.split('\\x')

# Remove empty paragraphs
paragraphs = [paragraph.strip()
              for paragraph in paragraphs if paragraph.strip()]


# Your OpenAI setup
# """Condense/optimize each paragraph (separated by "\x")  by:
# - Removing inappropriate line breaks, unnecessary words, suggestions/invitations/collaborative words, pronouns, conjunctions, prepositions, and adverbs
# - Enclosing variable names, class names, nouns in backticks (``)
# - Removing "\x" in output
# Here is the input:"""

llm = OpenAI(model='gpt-3.5-turbo-instruct')

use_in_post = True
prompt_add_use_in_post = ' (separated by "\\x") ' if use_in_post else ' '
template = f"""Condense/optimize each paragraph{prompt_add_use_in_post}by:
- Removing inappropriate line breaks, unnecessary words, suggestions/invitations/collaborative words, pronouns, conjunctions, prepositions, and adverbs
- Enclosing names like variable, class, function in backticks (``)
- Removing "\\x" in output
Here is the input:

""" + "{text}"
prompt_template = PromptTemplate.from_template(template)

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
output_file_path = 'llm_output.txt'
with open(output_file_path, 'a', encoding='utf-8') as output_file:
    for summary in tqdm(summaries):
        output_file.write(summary + '\n')

print(f'Summaries appended to {output_file_path}')
