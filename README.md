# cm2py

cm2py is a Python package for generating and manipulating save strings for the roblox game [Circuit Maker 2](https://www.roblox.com/games/6652606416/Circuit-Maker-2).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cm2py from [pypi](https://pypi.org/project/cm2py/).

```bash
pip install cm2py
```

## Usage

Basic program to generate a line of 8 looping OR gates:

```python
import cm2py as cm2

LENGTH = 8

save = cm2.Save()

blocks = []

for i in range(LENGTH):
    blocks.append(save.addBlock(cm2.OR, (i, 0, 0)))

### Commented out for clarity.
### You should store connections in a list if you want to modify them later.
# connections = []

for i in range(LENGTH):
    # connections.append(save.addConnection(blocks[i-1], blocks[i]))
    save.addConnection(blocks[i - 1], blocks[i])  # Directly add the connections to the save object

saveString = save.exportSave()
print(saveString)
```
(from [the loop.py example](examples/loop.py))

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
