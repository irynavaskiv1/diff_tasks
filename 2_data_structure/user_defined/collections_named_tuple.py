from collections import namedtuple


class ProtectedC:
    __slots__ = ["age"]  # what we can change, is not dict exactly
    name = "Jim"


pt = ProtectedC()
ProtectedC = namedtuple("Service", ("name", "url", "ip_attr"))
protected1 = ProtectedC(name="name3", url="url3", ip_attr="ip_attr3")
print(protected1)

service = namedtuple("Service", ("name", "url", "ip_attr"))
service1 = service(name="name1", url="url1", ip_attr="ip_attr1")
service2 = service(name="name2", url="url2", ip_attr="ip_attr2")
print(service2)
print(service2.name)


new_pt = pt._asdict()
