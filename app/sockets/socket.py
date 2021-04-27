from app import socket

@socket.on("new_color")
def new_color(data):
    socket.emit("change_color", data, broadcast=True)

@socket.on("new_dim")
def new_dim(data):
    socket.emit("change_dim", data, broadcast=True)