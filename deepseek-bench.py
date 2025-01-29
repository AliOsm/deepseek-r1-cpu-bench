from pathlib import Path

import ollama

from ollama import chat
from ollama import ChatResponse


MODELS = [
  'deepseek-r1:1.5b',
  'deepseek-r1:7b',
  'deepseek-r1:8b',
  'deepseek-r1:14b',
  'deepseek-r1:32b',
  'deepseek-r1:70b',
]


PROMPTS = {
  'chat': [
    'What are your thoughts on the latest scientific discovery regarding black holes?',
  ],
  'instruct': [
    'Write a step-by-step guide on how to bake a chocolate cake from scratch.',
    'Develop a python function that solves the following problem, sudoku game.',
    'Create a dialogue between two characters that discusses economic crisis.',
    'In a forest, there are brave lions living there. Please continue the story.',
    "I'd like to book a flight for 4 to Seattle in U.S.",
  ],
  'question-answer': [
    'Explain Artificial Intelligence and give its applications.',
    'How are machine learning and AI related?',
    'What is Deep Learning based on?',
    'What is the full form of LSTM?',
    'What are different components of GAN?',
  ]
}


ANSWERS_PATH = Path('./answers')


def main():
  ANSWERS_PATH.mkdir(exist_ok=True)

  for model in MODELS:
    print(f'Pulling "{model}" if it does not exist...')
    ollama.pull(model)

  print('')

  for model in MODELS:
    model_tokens_per_second = list()

    for prompts_type, prompts in PROMPTS.items():
      print(f'Benchmarking "{model}" on "{prompts_type}" prompts...', end=' ', flush=True)

      aggregated_tokens_per_second, prompts_tokens_per_second = benchmark(model, prompts_type, prompts)
      model_tokens_per_second.extend(prompts_tokens_per_second)

      print(f'{aggregated_tokens_per_second}t/s.')
    
    print(f'Overall "{model}" prompts: {round(sum(model_tokens_per_second) / len(model_tokens_per_second), 2)}t/s.\n')


def benchmark(model: str, prompts_type: str, prompts: list[str]) -> tuple[float, list[float]]:
  prompts_tokens_per_second = list()

  for index, prompt in enumerate(prompts):
    response: ChatResponse = chat(
      model=model,
      messages=[
        {
          'role': 'user',
          'content': prompt,
        },
      ],
    )

    answer_path = ANSWERS_PATH / model / prompts_type / f'{index + 1}.txt'
    answer_path.parent.mkdir(parents=True, exist_ok=True)

    with open(answer_path, 'w') as fp:
      fp.write(response.message.content)

    prompts_tokens_per_second.append(response.eval_count / response.eval_duration * (10**9))

  return round(sum(prompts_tokens_per_second) / len(prompts_tokens_per_second), 2), prompts_tokens_per_second


if __name__ == '__main__':
  main()
