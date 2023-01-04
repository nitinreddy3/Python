# Python dictionaries key value update novice way
dict = {"name": "Nitin", "age": 34, "gender": "male"}

dict["name"] = "ABC"
dict["name"]


# Python dictionaries key value update pro way
dict = {"name": "Nitin", "age": 34, "gender": "male"}

dict.update({"name": "ABC"})
dict["name"]
