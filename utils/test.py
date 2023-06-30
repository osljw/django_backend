import requests
from concurrent.futures import ThreadPoolExecutor

# 目标 API 的 URL
url = "http://127.0.0.1:8000/api/article"

# 定义测试函数，发送请求并返回响应时间
def make_request():
    response = requests.get(url)
    return response.elapsed.total_seconds()

# 设置并发请求数和总请求数
concurrent_requests = 10
total_requests = 100

# 使用线程池执行并发请求
with ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
    # 提交任务并获取结果
    results = [executor.submit(make_request) for _ in range(total_requests)]
    
    # 获取所有请求的响应时间
    response_times = [result.result() for result in results]

# 计算平均响应时间
average_response_time = sum(response_times) / len(response_times)
print("Average Response Time:", average_response_time, "seconds")