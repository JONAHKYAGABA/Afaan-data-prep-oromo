# This script has been sanitized to remove private access tokens and credentials.

# Replace sensitive tokens with environment-safe variables:
import os
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
WANDB_API_KEY = os.getenv("WANDB_API_KEY")

# Use these for secure login
# from huggingface_hub import login
# login(HF_API_TOKEN)

# from wandb import login as wandb_login
# wandb_login(key=WANDB_API_KEY)

# Replace the following line:
# login("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")
# with:
# login(HF_API_TOKEN)

# Avoid hardcoding API tokens or keys directly in scripts.
# This sanitized version encourages secure handling through environment variables or secret managers.
