# async def route(message):
#     if message.get('type') == 'seen':
#         await dispatch(message, message['senderId'])

#     else:
#         clients = await asyncdb.get_clients_by_target(message['targetId'])
#         for client in clients:
#             client_id = client.get('id')
#             await dispatch(message, client_id)


# async def start(name):
#     syslog('Message router started')
#     while True:
#         queue, message = await queues.bpop_async(name)
#         syslog(f'Processing message: {message}')
#         await route(ujson.loads(message))


# async def dispatch(message, client_id):
#     active_sessions = await sessions.get_sessions(client_id)
#     for session, queue in active_sessions.items():
#         message['isMine'] = client_id == message['senderId']
#         message['sessionId'] = session.decode()
#         await queues.push_async(queue, message)