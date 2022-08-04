# Learn Python #5 - Do with functions

## What functions are?

Functions in [Python](python.org) are meant to isolate the different parts of the program in smaller chunks.

Functions shall be easy to read and understand.

![functions](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/84xs9jc0wgw2qd55j555.png)

## Let us look at an example

Let us say we want to find the volume of a cube so we write

```
def volume(side):
    return side*side*side

print(f"The volume of a cube is {volume(3)} cubic cm")
//The volume of a cube is 27 cubic cm
```

- Here we say that we want to define a function with the keyword `def` which stands for `define` in [python](python.org).
- `volume` is a name given to that function.
- In parenthesis `()` we are passing an argument which is of type number.
- And we end the `()` with `:` so that the indentation (4 spaces) will begin from the next line.
- return the result with the `return` keyword.
- We are calling this method inside a `print` statement where we interpolate the value returned by the function.

## Quick gotchas when you are defining a function

- Function name cannot start with numbers or any special characters.

## Conclusion

There are more posts on the way related to the functions...So keep reading.

Thanks in advance for reading this article...🚀

*More than happy to connect with you on*

- [@twitter](https://twitter.com/_nitinreddy3)
- [@LinkedIn](https://www.linkedin.com/in/nitinreddy3/)

*You can also find me on*

- [@Github](https://github.com/nitinreddy3)
- [@DEV](https://dev.to/nitinreddy3)
- [@Medium](https://medium.com/@nitinreddy3)
