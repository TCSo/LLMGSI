from django.db import models
import random, string

# Create your models here.
def generate_code():
    length = 8
    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        if LLMRequest.objects.filter(code = code).count() == 0:
            break
    return code

def inputDefault():
    return {
        "input": "Please introduce yourself as a teaching assistent in UC Berkeley.",
    }
def outputDefault():
    return {
        "response": "Data unaccessible due to privacy concern.",
    }

class LLMRequest(models.Model):
    code = models.CharField(primary_key=True, max_length = 10, default=generate_code)

    input_data = models.JSONField(null=True, default=inputDefault)
    response_data = models.JSONField(null=True, default=outputDefault)
    succeed = models.BooleanField(default = False)

    updated_at = models.DateTimeField(auto_now=True, null=True)