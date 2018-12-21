from slacker import Slacker
from requests.sessions import Session

token = "xoxb-507380538243-508581046935-lqaSBt76meMAiinShrNl7ohe"
slack = Slacker(token)

# # Send a message to #general channel
# slack.chat.post_message('#general', 'Hello fellow slackers!')
#
# Get users list
# response = slack.users.list()
# users = response.body['members']

# Upload a file
# slack.files.upload('hello.txt', channels='general')
#
# # If you need to proxy the requests
# proxy_endpoint = 'http://myproxy:3128'
# slack = Slacker('token',
#                 http_proxy=proxy_endpoint,
#                 https_proxy=proxy_endpoint)

# Advanced: Use `request.Session` for connection pooling (reuse)

with Session() as session:
    slack = Slacker(token, session=session)
    slack.chat.post_message('#slacker_test_bbq923', 'All these requests')
    slack.chat.post_message('#slacker_test_bbq923', 'go through')
    slack.chat.post_message('#slacker_test_bbq923', 'a single https connection')