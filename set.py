# create
x = set()

# add
x = {"a","b"}
x.add("c")

# update or add multiple things
x.update("e", "f")

# delete
x.remove("f")
x.discard("f") # even if m is not in it wont be an error and will be delete if it is in

# pop random thing cannot pop specific thing as hash
x.pop()
