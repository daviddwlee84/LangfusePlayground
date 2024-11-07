from langfuse import Langfuse
from dotenv import load_dotenv
import os

load_dotenv()

# LANGFUSE_HOST = f"http://{os.getenv('SERVER_HOST')}:{os.getenv('SERVER_PORT')}"
LANGFUSE_HOST = "http://localhost:3000"
PUBLIC_KEY = os.getenv("LANGFUSE_INIT_PROJECT_PUBLIC_KEY")
SECRET_KEY = os.getenv("LANGFUSE_INIT_PROJECT_SECRET_KEY")
print(LANGFUSE_HOST, PUBLIC_KEY, SECRET_KEY)

# https://langfuse.com/docs/sdk/python/decorators
langfuse = Langfuse(secret_key=SECRET_KEY, public_key=PUBLIC_KEY, host=LANGFUSE_HOST)

import ipdb

ipdb.set_trace()

# BUG: Currently would have 502 error
print(langfuse.auth_check())

from langfuse.decorators import observe


@observe()
def test():
    print("Hello, from the test function!")


# BUG: Currently would have 502 error
test()

import ipdb

ipdb.set_trace()
