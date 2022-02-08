# Build a Python CLI tool with argparse

The `argparse` module is part of the Python standard library and meant to help you build robust command line tools. Once you need flags, switches, values, or positional arguments, it is very difficult to achieve that without using a framework.

## Watch the Video tutorial

[![Build a robust CLI in Python tutorial](https://img.youtube.com/vi/g2JGmA4vmoU/0.jpg)](https://youtu.be/g2JGmA4vmoU "Build a robust CLI in Python")


In this case, `argparse` can help build all you need to handle inputs in the terminal. We'll see how a single file named `size.py` that calculates file sizes can make use of `argparse` to handle the input in the terminal. Then, we will cover how error handling is done automatically when the expectations from `argparse` aren't met. And finally, we'll go through some of the help menu options that construct the body of the help output.


## Why would you want to use argparse

Since `argparse` is part of the Python standard library, there is no need for you to define or install any external dependencies. You are ensuring that any Python installation in any system will work correctly out of the gate.
A very basic Python CLI tool without dependencies using the argparse module


## Next steps
Now that you know how to enhance a Python script into a more powerful one with `argparse`, you can try out other frameworks like the Click framework or something much simpler by using the `sys` module. I have examples and guides for the [sys.argv module](https://github.com/alfredodeza/basic-python-cli) and for [using the Click framework](https://github.com/alfredodeza/click-python-cli).
