# Python Dictionaries - Part 2 🐍

Dictionaries are an interesting data structure in Python. In other programming languages like JavaScript, you can call it an object.

Getting back to our example, we can change the value of a dictionary key as shown below:

```
dict = {"name": "Nitin", "age": 34, "gender": "male"}

dict["name"] = "ABC"
dict["name"]
Result -> ABC
```
Pretty easy isn't it?

### Add a new key-value pair
Now let's look at how we can add a new key-value pair to a dictionary.
Python dictionary has an `update` method that gives you the freedom to add or update a new key-value pair.

```
dict = {"name": "Nitin", "age": 34, "gender": "male"}

dict.update({"city": "Pune"})
dict
Result -> {"name": "Nitin", "age": 34, "gender": "male", "city": "Pune"}
```

### Update a key-value pair
Updating a key-value pair is pretty simple.
```
dict = {"name": "Nitin", "age": 34, "gender": "male"}

dict.update({"city": "Delhi"})
dict
Result -> {"name": "Nitin", "age": 34, "gender": "male", "city": "Delhi"}
```

If you observe in the above example, the new key-value pair is added with the curly braces as an argument to the `update` method.
>If the key-value pair already exists in the dictionary then the value will be replaced and if the key-value pair does not exist then this method will create a new key-value pair.


### Loop over the dictionary
We can also loop over the dictionary data using the `for` iterator and it's quite easy.
```
dict = {"name": "Nitin", "age": 34, "gender": "male"}

for data in dict.keys():
    print(data)

Result ->
name
age
gender
```
Here we loop over the dictionary keys and as a result, the keys are getting printed.

We can also loop over the dictionary keys' values using the `for` iterator
```
dict = {"name": "Nitin", "age": 34, "gender": "male"}

for data in dict.values():
    print(data)

Result ->
Nitin
34
male
```

### Easy to understand? 💡

A dictionary contains

- Loop over the dictionary
- Add or update the dictionary data

>This would look similar to an object in JavaScript


## Conclusion 📗

There are more posts on the way related to the dictionaries...So keep reading.

Thanks in advance for reading this article...🚀

*I am more than happy to connect with you on*

- [@twitter](https://twitter.com/_nitinreddy3)
- [@LinkedIn](https://www.linkedin.com/in/nitinreddy3/)

*You can also find me on*

- [@Github](https://github.com/nitinreddy3)
- [@DEV](https://dev.to/nitinreddy3)
- [@Medium](https://medium.com/@nitinreddy3)
