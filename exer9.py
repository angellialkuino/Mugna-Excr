
class HexFormatError(Exception):
    """The given string is not hexidecimal"""
    # def __init__(self,message):
    #     self.message = message
    pass #what does this do again

class MemoryError(Exception):
    """The given string is beyond 4-bytes"""
    # def __init__(self,message):
    #     self.message = message
    pass

def converter(hex):
    try:
        if(len(hex.encode('utf-8'))>8):
            raise MemoryError
        print(int(hex,16))

    except ValueError:
        raise HexFormatError("The given string is not hexidecimal")
    except MemoryError:
        raise MemoryError("The given string is beyond 4-bytes")

converter("ah")

