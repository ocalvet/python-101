class ApiService(object):
    """A service to make api calls"""

    def __init__(self):
        self.title = "Api service"

    def say(self):
        return "Hello %s" % self.title
