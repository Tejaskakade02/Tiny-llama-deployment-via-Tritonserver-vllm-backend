docker run --gpus all -it --rm -p 8000:8000 -p 8001:8001 -p 8002:8002 -v "$(pwd)/model_repository:/models" -v "$(pwd)/vllm_workspace/tiny-llama:/workspace/tiny-llama" triton-vllm-light
