# Calculator Example

I did a very quick calculator application, figuring it would be easy. It mostly was.

## Floating Point Math in Python

Oh yeah - I forgot that math in python can sometimes be dumb.

```python
>>> 5.2 + 2.3
7.5
>>> 5.2 - 2.3
2.9000000000000004
```

Argh. Fortunately, the [decimal](https://docs.python.org/3/library/decimal.html) module is pretty reasonable to use.

Since I had also been playing with [Julia](https://julialang.org/), I had hopes that Julia, being more math-oriented, may do the right (expected) thing, but alas:

```julia
julia> 1.1 + 1.2
2.3

julia> 1.2 - 1.1
0.09999999999999987
```

```python
In [9]: 1.2 - 1.1
Out[9]: 0.09999999999999987
```

At least Python and Julia _get the same answer_.
