from django.shortcuts import render
from django.http import HttpResponse
import redis

r = redis.Redis(host="redis-server", db=0)
r.set("visits", 0)

def index(request):
    v = int(r.get("visits"))
    ret = f"Hello, world. You're at the polls index. Number of visits:{v}"
    r.set("visits", v+1)
    return HttpResponse(ret)