from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://localhost:8000"

    @task
    def view_homepage(self):
        self.client.get("/newspaper/")

    @task
    def view_news_detail(self):
        self.client.get("/new/1/")
