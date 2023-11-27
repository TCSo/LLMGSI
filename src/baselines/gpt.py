#!/usr/bin/env python3
"""Given a data file with student questions, get GPT results.

The questions are prompted in the exact order that they're given.

```
python -u ./gpt.py \
    --access-key "" \
    --input-path questions.jsonl \
    --output-path gpt_responses.jsonl.gz
```
"""
import argparse
import json
import logging
import sys
from copy import deepcopy
from time import sleep
from openai import OpenAI

from tqdm import tqdm
from xopen import xopen

from tenacity import (
                    retry,
                    stop_after_attempt,
                    wait_random_exponential,
                    )

logger = logging.getLogger(__name__)

def main(
    access_key,
    input_path,
    output_path,
):
    with open("./prompt.prompt") as f:
        prompt_template = f.read().rstrip("\n")

    client = OpenAI(api_key = access_key)

    @retry(wait=wait_random_exponential(min=1, max=30), stop=stop_after_attempt(1000))
    def get_resp(prompt):
        resp = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{'role': 'user', 'content': prompt}],
                temperature=0,
                max_tokens=1000
                )
        return resp.choices[0].message.content

    with xopen(input_path) as fin, xopen(output_path, "w") as f:
        for line in tqdm(fin):
            input_example = json.loads(line)
            question = input_example["question"]
            prompt = prompt_template.format(question=question)
            response = get_resp(prompt)
            output_example = deepcopy(input_example)
            output_example["model_prompt"] = prompt
            output_example["model_answer"] = response
            f.write(json.dumps(output_example) + "\n")

if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s - %(module)s - %(levelname)s - %(message)s", level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("--access-key", help="API key.", required=True)
    parser.add_argument("--input-path", help="Path to data with questions and documents to use.", required=True)
    parser.add_argument("--output-path", help="Path to write output file of generated responses", required=True)
    args = parser.parse_args()

    logger.info("running %s", " ".join(sys.argv))
    main(
        args.access_key,
        args.input_path,
        args.output_path,
    )
    logger.info("finished running %s", sys.argv[0])
