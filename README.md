# FastAPI and Vue.js Example App

I found an [article](https://6chaoran.github.io/data-story/visualization/data-engineering/fastapi-vue-app/) describing how to make a quick and dirty Vue.js front-end to a FastAPI application.

The example uses some ML stuff that, while interesting, is more than I have energy for right now, so I'll make a much simpler API, and see if I can fudge the rest.

## My Example

I did a very quick calculator application, figuring it would be easy. It mostly was.

## Floating Point Math in Python

Oh yeah - I forgot that math in python can sometimse be dumb.

```python
>>> 5.2 + 2.3
7.5
>>> 5.2 - 2.3
2.9000000000000004
```

Argh. Fortunately, the [decimal](https://docs.python.org/3/library/decimal.html) module is pretty reasonable to use.
