class ProtectedC:
    __slots__ = ["age"]  # what we can change, is not dict exactly
    name = "Jim"


pt = ProtectedC()
