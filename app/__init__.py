from flask import Flask
import redis
from rq import Queue
from config import config

app = Flask(__name__)
r = redis.Redis()
q = Queue(connection=r)

from . import (views, admin_views, tasks)