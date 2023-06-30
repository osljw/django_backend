from gpt4free import theb_stream

client = theb_stream.Completion()

for token in client.create('hello world'):
    print(token, end='', flush=True)
