# Python Dictionaries - Part 2 🐍

In the last article we had seen how we can create a dictionary and access an element in it. Today we are going to deep dive into the main data structure in Python known as Dictionary.

## Accessing an element 💡

The element in the dictionary can be accessed through the square brackets nomenclature.
```
dict = {"name": "Nitin", "age": 34, "gender": "male"}

dict["name"]
Result -> Nitin
```

What if you are trying to access to element that is not in the dictionary?

```
dict = {"name": "Nitin", "age": 34, "gender": "male"}

dict["address"]
Result -> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'address'
```
In the above example, the address is not in the dictionary because we are trying to access it from the square brackets.

But we can also leverage the `get` method to access the dictionary key
```
dict = {"name": "Nitin", "age": 34, "gender": "male"}
dict.get("name")
Result -> 'Nitin'
```



### Delete an element with `del` method 💡

```
dict = {"name": "Nitin", "age": 34, "gender": "male"}
del(dict["name"])
print(dict)
Result -> {"age": 34, "gender": "male"}
```

### Delete the dictionary 💡
```
dict = {"name": "Nitin", "age": 34, "gender": "male"}
del(dict)
print(dict)
Result -> <class 'dict'>
```
In order to delete the dictionary you just have to mention the dictionary variable name in the `del` method.

### Find the length 💡
Finding the length of the dictionary is quite simple.
```
dict = {"name": "Nitin", "age": 34, "gender": "male"}
len(dict)
Result -> 3
```

### Check if the key exists 💡

Not so difficult.
```
dict = {"name": "Nitin", "age": 34, "gender": "male"}
print("name" in dict)
Result -> True
```
The boolean would be returned when you try to check the key in the dictionary.



### Easy to understand? 💡

A dictionary contains

- unique keys
- key can have different types of values like `number`, `string`, `boolean` etc.

>This would look similar to an object in JavaScript


## Conclusion 📗

There are more posts on the way related to the tuples...So keep reading.

Thanks in advance for reading this article...🚀

*I am more than happy to connect with you on*

- [@twitter](https://twitter.com/_nitinreddy3)
- [@LinkedIn](https://www.linkedin.com/in/nitinreddy3/)

*You can also find me on*

- [@Github](https://github.com/nitinreddy3)
- [@DEV](https://dev.to/nitinreddy3)
- [@Medium](https://medium.com/@nitinreddy3)
