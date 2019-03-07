

from locust import HttpLocust,TaskSet,task

class H5_index(TaskSet):

    @task
    def H5_index1(self):
        self.client.get('/online/store/stock/inventory?g=1155&groupID=1155&shopID=76067972')



class WebsiteUser(HttpLocust):
    task_set = H5_index
    min_wait = 3000
    max_wait = 8000

