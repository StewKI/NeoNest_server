# NeoNest server

This is repo for the server side of a NeoNest app.
Server is written completly in Python

## Usage

Firstly, you need to have Python and pip installed.
After that you have to install these pip packages:

```bash
pip install openai
pip install homeassistant_api
pip install pyngrok
pip install flask
```

When you have those, you have to add file **secret.py**.

Server is dependent on 3 servicies:
- Home Assistant
- Ngrok
- OpenAI

So you need have API keys/tokens for all 3 of them. You store them in **secret.py** like this:

```python
ha_access_token = '...'
my_sk = 'sk-proj-...'
ngrok_token = '...'
```

After that you are ready to start server:

```bash
python -m main.py
```
