# LiteGPT

LiteGPT is a simple Python library designed for interacting with APIs, enabling text query submission and image generation in a chat format. It supports saving chat history and configuring an HTTP client with the option to use HTTP/2 for faster data transfer. The library is built with a simplified interface, making it easy to integrate with various chatbots or user applications working with generative AI.

## Features

- **Text Queries:** The `ask` method sends user queries to the API and processes the response. It includes support for message history, allowing continuous dialogue.
- **Image Generation:** The `image` method sends a text description to generate an image and returns the result in JSON format.
- **Message History Management:** The library supports working with message history through the external `History` class, making it easy to track the conversation and improve the user experience.

## Documentation
For detailed documentation on how to use LiteGPT, please refer to the official documentation:
[LiteGPT Documentation](https://red-3.gitbook.io/litegpt)

## Installation

You can install the `LiteGPT` library from PyPI using `pip`:

```bash
pip install litegpt
```
## Usage

**Text Queries**

The ask function allows you to send a query to the AI chat and receive a response while maintaining chat history.

```python
from litegpt import LiteGPT

# Initialize LiteGPT and send a query
bot = LiteGPT()
response = bot.ask("Your query here...")
print(response)
```

**Text Queries Async**

```python
from litegpt import AsyncLiteGPT
import asyncio

async def main():
	# Initialize LiteGPT and send a query
	bot = AsyncLiteGPT()
	response = await bot.ask("Your query here...")
	print(response)
asyncio.run(main())
```
