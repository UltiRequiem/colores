# Colores

A simplifier of the [Colorama](https://github.com/tartley/colorama) API,
and some extra functions.

## Description

Colors was originally born in [Chuy](https://github.com/UltiRequiem/chuy).
But little by little, as I created more terminal applications
I realized that in all of them I had some helper methods related to colorama,
so I decided to separate it to a new package.

## Usage

Is very simple to use this package:

```python
from colores import colorized_print, colorized_input, CYAN, MAGENTA, YELLOW

colorized_print(colorized_input("Enter a text:"), CYAN)
```

All the functions are defined in [colores/core.py](https://github.com/UltiRequiem/colores/blob/master/colores/core.py)
and are well documented.

### License

This project is licensed under the [MIT License](./LICENSE.md)
