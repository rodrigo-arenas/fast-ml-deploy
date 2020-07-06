from locust import HttpUser, TaskSet, task, between

"""
Run locus with:
locust -f ./tests/load_test.py
"""


class IrisPredict(TaskSet):
    @task
    def predict(self):
        request_body = {"data": [[4.8, 3, 1.4, 0.3]]}
        self.client.post('/predict', json=request_body)



class IrisLoadTest(HttpUser):
    tasks = [IrisPredict]
    host = 'http://127.0.0.1'
    stop_timeout = 200
    wait_time = between(1, 5)
