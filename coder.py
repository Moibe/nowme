import os
# from huggingface_hub import HfApi

# api = HfApi()
# secret_value = api.get_repo_secret(repo_id="moibe/nowme", secret_name="llave")

api_key = os.getenv("llave")

print(f"El valor de mi secreto es: {api_key}")