import socketio

sio = socketio.Server()

@sio.on('connet')
def connect(sid, environ, auth):
    print("this is auth:\t", auth)
    print(sio.sockets)
    print("connect", sid)
    # sio.emit("users", users)


@sio.event
def disconnect(sid):
    print("disconnect", sid)




