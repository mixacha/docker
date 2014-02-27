import memcache

ip = 'localhost'
port = 49156

mc = memcache.Client(["{0}:{1}".format(ip, port)], debug=0)
mc.set("MDM", "Test1")
#mc.set("22", "2")
value = mc.get("MDM")

print value
