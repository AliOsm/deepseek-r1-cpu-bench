# deepseek-r1-cpu-bench

## Machine Specifications

- R5 12xlarge (`r5.12xlarge`)
- Intel Xeon Platinum 8175
- 48 vCPUs
- 384GB of RAM (`htop` shows 374GB only 🤨)

## Benchmark Results

| DeepSeek R1 Size | Chat prompts | Instruct prompts | Question-Answer prompts | Overall  | Consumed Memory |
|------------------|--------------|------------------|-------------------------|----------|-----------------|
| 1.5B             | 48.03t/s     | 49.1t/s          | 51.16t/s                | 49.94t/s | ~1.4GB          |
| 7B               | 17.38t/s     | 17.2t/s          | 17.66t/s                | 17.43t/s | ~4.8GB          |
| 8B               | 14.58t/s     | 15.42t/s         | 15.76t/s                | 15.5t/s  | ~5.7GB          |
| 14B              | 9.64t/s      | 8.81t/s          | 9.29t/s                 | 9.1t/s   | ~10GB           |
| 32B              | 4.39t/s      | 4.38t/s          | 4.41t/s                 | 4.4t/s   | ~20.6GB         |
| 70B              | 2.2t/s       | 2.2t/s           | 2.23t/s                 | 2.21t/s  | ~42.3GB         |

## Run the Benchmark

- Install `ollama` using `curl -fsSL https://ollama.com/install.sh | sh`
- Install `ollama` Python package using `pip install ollama`
- Run the `deepseek-bench.py` file that exists in this repository using `python deepseek-bench.py`

## Script Output

```
Pulling "deepseek-r1:1.5b" if it does not exist...
Pulling "deepseek-r1:7b" if it does not exist...
Pulling "deepseek-r1:8b" if it does not exist...
Pulling "deepseek-r1:14b" if it does not exist...
Pulling "deepseek-r1:32b" if it does not exist...
Pulling "deepseek-r1:70b" if it does not exist...

Benchmarking "deepseek-r1:1.5b" on "chat" prompts... 48.03t/s.
Benchmarking "deepseek-r1:1.5b" on "instruct" prompts... 49.1t/s.
Benchmarking "deepseek-r1:1.5b" on "question-answer" prompts... 51.16t/s.
Overall "deepseek-r1:1.5b" prompts: 49.94t/s.

Benchmarking "deepseek-r1:7b" on "chat" prompts... 17.38t/s.
Benchmarking "deepseek-r1:7b" on "instruct" prompts... 17.2t/s.
Benchmarking "deepseek-r1:7b" on "question-answer" prompts... 17.66t/s.
Overall "deepseek-r1:7b" prompts: 17.43t/s.

Benchmarking "deepseek-r1:8b" on "chat" prompts... 14.58t/s.
Benchmarking "deepseek-r1:8b" on "instruct" prompts... 15.42t/s.
Benchmarking "deepseek-r1:8b" on "question-answer" prompts... 15.76t/s.
Overall "deepseek-r1:8b" prompts: 15.5t/s.

Benchmarking "deepseek-r1:14b" on "chat" prompts... 9.64t/s.
Benchmarking "deepseek-r1:14b" on "instruct" prompts... 8.81t/s.
Benchmarking "deepseek-r1:14b" on "question-answer" prompts... 9.29t/s.
Overall "deepseek-r1:14b" prompts: 9.1t/s.

Benchmarking "deepseek-r1:32b" on "chat" prompts... 4.39t/s.
Benchmarking "deepseek-r1:32b" on "instruct" prompts... 4.38t/s.
Benchmarking "deepseek-r1:32b" on "question-answer" prompts... 4.41t/s.
Overall "deepseek-r1:32b" prompts: 4.4t/s.

Benchmarking "deepseek-r1:70b" on "chat" prompts... 2.2t/s.
Benchmarking "deepseek-r1:70b" on "instruct" prompts... 2.2t/s
Benchmarking "deepseek-r1:70b" on "question-answer" prompts... 2.23t/s.
Overall "deepseek-r1:70b" prompts: 2.21t/s.
```
