from utils.helper import pre_process, post_process, load_prompt_from_yaml
from prompts.prompt_template import final_prompt
import yaml

def load_prompt_from_yaml(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        prompt_data = yaml.safe_load(file)
    return prompt_data["system_prompt"]


print(load_prompt_from_yaml("prompts/base_prompt.yml"))