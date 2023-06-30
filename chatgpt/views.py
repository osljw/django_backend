import json
import time
from django.http import StreamingHttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.generic import View
# from django.views.decorators.csrf import csrf_exempt
from gpt4free import theb
from gpt4free import theb_client
# from sse_starlette.sse import EventSourceResponse

API_MODEL_NAME = 'your-api-model-name'

class Message:
    def __init__(self, text):
        self.text = text

messages = [
    Message("你好"),
    Message("请问有什么需要帮助的吗？"),
    Message("这个产品能做些什么呢？"),
    Message("我想了解一下价格"),
    Message("谢谢，再见")
]


# 模拟 OpenAI API 的响应
def generate_responses(question):
    #messages = theb.Completion.create(question, proxy='127.0.0.1:10809')

    client = theb_client.Completion
    messages = client.create(question, proxy='127.0.0.1:10809')

    # messages = "123456"
    for i, token in enumerate(messages):
        print(token, end='', flush=True)
        # yield f"data: {token}\n\n"
            
        result = {
            "id": i,
            "object": "text_completion",
            "created": int(time.time()),
            "model": API_MODEL_NAME,
            "choices": [
                {
                    "text": f"{token} <Response>",
                    "index": 0,
                    "logprobs": None,
                    "finish_reason": None,
                    "selected_text": None,
                    "prompt": token,
                    "start_offset": 0,
                    "end_offset": len(token),
                    "meta": {
                        "example_id": None,
                        "context": None
                    },
                    "delta": {
                        "content": token
                    }
                }
            ]
        }
        yield f"data: {json.dumps(result)}\n\n"
        # yield " " * 1024
        # time.sleep(1)  # 模拟网络延迟
    yield "data: [DONE]\n"  # 标识聊天已结束



# @csrf_exempt
async def chat_completions(request):
    '''
    OpenAI: {'model': 'gpt-3.5-turbo', 'messages': [{'role': 'user', 'content': '123'}, {'role': 'user', 'content': '123'}], 'stream': True}
    theb: 
    '''
    print("==== request", request, json.loads(request.body))
    if request.method != 'POST':
        return HttpResponseBadRequest('Invalid request method.')

    # 获取请求参数
    try:
        data = json.loads(request.body)
        messages = data.get('messages')
        question = messages[-1]['content']
    except Exception as e:
        print("exception:", e)
        return HttpResponseBadRequest('Invalid request data.')
    

    # 返回 StreamingHttpResponse，用于向前端不断推送聊天内容
    response = StreamingHttpResponse(
        generate_responses(question),
        content_type='text/event-stream',
        # content_type='application/octet-stream',
    )
    print("\n\n=============response:", response)
    response['Cache-Control'] = 'no-cache'
    response['Connection'] = 'keep-alive'
    return response
