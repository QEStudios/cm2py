from string import ascii_lowercase, ascii_uppercase, digits
from typing import Union, Callable, IO
import logging, base64, math, struct

try:
    import zlib
except:
    zlib = None
    logging.exception("'zlib' wasn't found. Install it to use HugeMemory.")

class Memory:
    """Base memory class; any memory. This class uses a list of integers (rather than bytes) as means of storing/processing data."""
    raw = []
    """The raw data in the memory. It is not recommended to use this directly."""
    size = 0
    """Size of the memory (in bytes). This number is the number of addresses, not the total data."""
    nbits = 0
    """Bits of data at each address."""
    __readable = 0
    """Readability; Not Implemented"""
    __writable = 0
    """Writability; Not Implemented"""

    __encoder = None
    """The encoding function to use; data -> memstring"""
    __decoder = None
    """The decoding function to use; memstring -> data"""

    def __init__(self, size : int, nbits : int, encoder : Callable, decoder : Callable, init_data = None):
        """You shouldn't use this class unless you're making your own memory type. Use MassMemory, MassiveMemory, etc instead.
        :param int size: The size (number of addresses)
        :param int nbits: The number of bits per address (must be a multiple of 8, and non-zero)
        :param encoder: An encoding function to encode data into memstrings. See massMemoryEncode as an example
        :param decoder: A decoder function to get data from a memstring. See massMemoryDecode as an example
        :param init_data: Optional initial data. If it's a memstring, it's decoded using the provided decoder, otherwise it's assumed to just be raw data."""
        self.size = size
        self.nbits = nbits
        self.__encoder = encoder
        self.__decoder = decoder
        if init_data:
            if isinstance(init_data, str):
                self.load(init_data)
            else:
                self.raw = init_data
        if len(self.raw) < self.size:
            self.raw.extend([0] * (self.size - len(self.raw)))
        

    def get(self, index : int) -> int:
        """Get data at an index. Alternatively, use Memory[index]. Negative indexes allowed."""
        if index >= self.size:
            raise IndexError(f"{index} is greater than maximum of {self.size-1}.")
        return self.raw[index]

    def put(self, data : int, index: int) -> None:
        """Put data at an index. Alternatively, use Memory[index] = data. Negative indexes allowed."""
        if index >= self.size:
            raise IndexError(f"{index} is greater than maximum of {self.size-1}.")
        self.raw[index] = data

    def load(self, text : str) -> None:
        """Load a memory string into this memory (overwrites existing contents)."""
        if not self.__decoder:
            raise NotImplementedError("A decoding function was not specified.")
        self.raw = self.__decoder(text)

    def save(self) -> str:
        """Save memory contents as a memstring."""
        if not self.__encoder:
            raise NotImplementedError("An encoding function was not specified.")
        return self.__encoder(self.raw)
    
    def dumpfile(self, file : Union[str, IO[bytes]], n:int=-1) -> None:
        """Dump memory data to a file or buffer
        :param int n: Max number of addresses to write. -1 for infinite
        """
        if n < 0:
            n = 2**32
        i=0
        if isinstance(file, str):
            with open(file, 'wb') as f:
                for v in self.raw:
                    f.write(v.to_bytes(math.ceil(self.nbits / 8), "little"))
                    i += 1
                    if i >= n:
                        break
        else:
            if file.seekable():
                file.seek(0)
            for v in self.raw:
                file.write(v.to_bytes(math.ceil(self.nbits / 8), "little"))
                i+=1
                if i >= n:
                    break
            

    def loadfile(self, file : Union[str, IO[bytes]]) -> None:
        """Load memory data from a file or buffer. Contents are truncated to fit"""
        if isinstance(file, str):
            with open(file, 'rb') as f:
                for i in range(self.size):
                    self.raw[i] = int.from_bytes(f.read(math.ceil(self.nbits / 8)), "little")
        else:
            if file.seekable():
                file.seek(0)
            for i in range(self.size):
                    self.raw[i] = int.from_bytes(file.read(math.ceil(self.nbits / 8)), "little")
        if len(self.raw) < self.size:
            self.raw.extend([0] * (self.size - len(self.raw)))

    def __getitem__(self, key : Union[str, int]) -> int:
        """Integers and bin strings can be used interchangeably for the index."""
        if isinstance(key,str):
            if key.startswith('0b'):
                key = key[2:]
            key = int(key,2)
        return self.raw[key]
    def __setitem__(self, key : Union[str, int], value : Union[str, int]) -> None:
        """Integers and bin strings can be used for both parameters interchangeably."""
        if isinstance(key,str):
            if key.startswith('0b'):
                key = key[2:]
            key = int(key,2)
        if isinstance(value,str):
            if value.startswith('0b'):
                value = value[2:]
            value = int(value,2)
        self.raw[key] = value

def load(data : str) -> Memory:
    """Load a memory string. Automatically detects memory type. Will raise an exception for invalid memstrings.
    If you already know what type of memory the string belongs to, you should use MassMemory(memstring), MassiveMemory(memstring), etc"""
    if len(data) == 8192:
        target = MassMemory
    elif len(data) == 12288:
        target = MassiveMemory
    else:
        target = HugeMemory
    return target(data)

def massMemoryEncode(data: list[int]) -> str:
    """Encodes data into a MassMemory memstring."""
    return ''.join(f'{i:02X}' for i in data)

def massMemoryDecode(text: str) -> list[int]:
    """Decodes a MassMemory memstring into data."""
    return [int(text[i:i+2], 16) for i in range(0, len(text), 2)]

def massiveMemoryEncode(data: list[int]) -> str:
    """Encodes data into a MassiveMemory memstring."""
    alphabet = ascii_uppercase + ascii_lowercase + digits + "+/"
    hex_str = ''.join(f'{i:04x}' for i in data)
    instruction_bytes = bytes.fromhex(hex_str)

    output_chars = []
    for b1, b2 in zip(instruction_bytes[::2], instruction_bytes[1::2]):
        bits = (b1 << 8) | b2
        output_chars.extend(alphabet[(bits >> (6 * i)) & 0x3F] for i in range(3))
    
    output = ''.join(output_chars)
    return output.ljust(12288, 'A')

def massiveMemoryDecode(text: str) -> list[int]:
    """Decodes a MassiveMemory memstring into data."""
    alphabet = ascii_uppercase + ascii_lowercase + digits + "+/"
    index_table = {c: i for i, c in enumerate(alphabet)}

    outb = []
    for i in range(0, len(text), 3):
        group = text[i:i + 3]
        bits = 0
        for c in group:
            bits = (bits << 6) | index_table[c]
        outb.append(bits)
    return outb

def hugeMemoryEncode(data: list[int]) -> str:
    """Encodes data into a HugeMemory memstring."""
    packed = struct.pack(f'<{len(data)}H', *data)  # Little-endian 16-bit unsigned ints
    compressed = zlib.compress(packed)[2:-4]       # Strip zlib headers and checksum (raw deflate)
    return base64.b64encode(compressed).decode('ascii')

def hugeMemoryDecode(text: str) -> list[int]:
    """Decodes a HugeMemory memstring into data."""
    rs = zlib.decompress(base64.b64decode(text), wbits=-zlib.MAX_WBITS)
    return list(struct.unpack(f'<{len(rs)//2}H', rs))

class MassMemory(Memory):
    """MassMemory; 8 bit addresses with 8 bit data."""
    size = 2**8

    def __init__(self, data : Union[str, list[int], None]=None):
        """
        :param data: Optional initial data. A memstring can be provided, or just data. 
        """
        super().__init__(2**8, 8, massMemoryEncode, massMemoryDecode, init_data=data)

class MassiveMemory(Memory):
    """MassiveMemory; 12 bit addresses with 16 bit data."""
    size = 2**12
    def __init__(self, data : Union[str, list[int], None]=None):
        """
        :param data: Optional initial data. A memstring can be provided, or just data. 
        """
        super().__init__(2**12, 16, massiveMemoryEncode, massiveMemoryDecode, init_data=data)

class HugeMemory(Memory):
    """HugeMemory; 16 bit addresses with 16 bit data."""
    size = 2**16
    def __init__(self, data : Union[str, list[int], None]=None):
        """
        :param data: Optional initial data. A memstring can be provided, or just data. 
        """
        super().__init__(2**16, 16, hugeMemoryEncode, hugeMemoryDecode, init_data=data)

class ROMs:
    """Pre-defined ROM loaders. These load a pre-defined ROM onto an existing Memory."""
    def divider(mem_instance : Memory) -> None:
        """6-bit divider (0 / 0 = 0). Outputs are rounded."""
        if not mem_instance.massive:
            raise Exception("Memory is not a MassiveMemory")
        fp = mem_instance
        for i in range(4096):
            param1 = (i & 0b111111000000)>>6
            param2 = (i & 0b000000111111)
            if param2 == 0:
                fp[i] = 0
            else:
                fp[i] = int(round(param1/param2))

    def multiplier(mem_instance : Memory) -> None:
        """6-bit multiplier."""
        if not mem_instance.massive:
            raise Exception("Memory is not a MassiveMemory")
        fp = mem_instance
        for i in range(4096):
            param1 = (i & 0b111111000000)>>6
            param2 = (i & 0b000000111111)
            fp[i] = param1*param2

    def adder(mem_instance : Memory) -> None:
        """6-bit adder."""
        if not mem_instance.massive:
            raise Exception("Memory is not a MassiveMemory")
        fp = mem_instance
        for i in range(4096):
            param1 = (i & 0b111111000000)>>6
            param2 = (i & 0b000000111111)
            fp[i] = param1+param2
        
    def subtractor(mem_instance : Memory) -> None:
        """6-bit subtractor (any result below 0 just outputs 0)."""
        if not mem_instance.massive:
            raise Exception("Memory is not a MassiveMemory")
        fp = mem_instance
        for i in range(4096):
            param1 = (i & 0b111111000000)>>6
            param2 = (i & 0b000000111111)
            if param1-param2 < 0:
                fp[i] = 0
            else:
                fp[i] = param1-param2

    def doubledabble(mem_instance: Memory) -> None:
        """Outputs the input number's digits as 4 4-bit numbers. Example: 1024 -> 4 2 0 1"""
        if not mem_instance.massive:
            raise Exception("Memory is not a MassiveMemory")
        fp = mem_instance
        for i in range(4096):
            st = f'{i:04}'  # 4-character decimal string, zero-padded
            fp[i] = (
                f'{int(st[3]):04b}' +
                f'{int(st[2]):04b}' +
                f'{int(st[1]):04b}' +
                f'{int(st[0]):04b}'
            )
