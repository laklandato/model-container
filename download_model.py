from huggingface_hub import snapshot_download

# Specify the Hugging Face repository containing the model
model_repo = "taide/Llama-3.1-TAIDE-LX-8B-Chat"
snapshot_download(
    repo_id=model_repo,
    local_dir="/models",
    allow_patterns=["*.safetensors", "*.json", "*.txt"],
    token="hf-xxxxxxxxx",
)
