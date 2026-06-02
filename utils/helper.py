import yaml
# make a function to remove white spaces from email
def pre_process(email):
    return {"email_text",email.strip()}
def post_process(output):
    return output.model_dump()

def load_prompt_from_yaml(file_path: str):
    with open(file_path, "r", encoding="utf-8") as file:
        prompt_data = yaml.safe_load(file)
    return prompt_data["system_prompt"]
