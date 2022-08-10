## What are Lists?

Lists in Python are the collection of elements of any type. What does that mean? Let's check the below examples.

## Let us look at an example

- Example 1:

Let's say we have a list of employees with their `name` as the list items

```
employees = ["Abc", "Bcd"]
```

In the above item, you can add a new item, remove an item, append an item, and furthermore.

### Add an item

There are two ways in which we can add a new item to the list.

- Append

```
employee.append("Cde")
// employee -> ["Abc", "Bcd", "Cde"]
```

- Insert

```
employee.insert(0, "Efg")
// employee -> ["Efg", "Abc", "Bcd", "Cde"]
```

>The difference between the `append` and `insert` methods is that the `append` add the element at the last position of the list whereas in `insert` you can specify at what position you want to add the element.

### Get the length of the list

```
employee = ["Efg", "Abc", "Bcd", "Cde"]
len(employee) -> 4
```

`len` is useful that helps in getting the length of a list.

### Reference a list item by its position

```
employee = ["Efg", "Abc", "Bcd", "Cde"]
employee[2]
```

In the `[]` you need to specify a position of an element that you need a reference to.

### Changing an item in the list

```
employee = ["Efg", "Abc", "Bcd", "Cde"]
employee[1] = "Nitin"
```

Find the element by specifying the position and then assign the value.

## Conclusion

There are more posts on the way related to the lists...So keep reading.

Thanks in advance for reading this article...🚀

*I am more than happy to connect with you on*

- [@twitter](https://twitter.com/_nitinreddy3)
- [@LinkedIn](https://www.linkedin.com/in/nitinreddy3/)

*You can also find me on*

- [@Github](https://github.com/nitinreddy3)
- [@DEV](https://dev.to/nitinreddy3)
- [@Medium](https://medium.com/@nitinreddy3)
