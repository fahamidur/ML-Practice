import numpy as np

shape1 = (3, 2, 2)
shape2 = (3, 1, 2)
shape3 = (3, 3, 2)


array1 = np.array(np.random.randint(10, 50, shape1))
array2 = np.array(np.random.randint(10, 50, shape2))
array3 = np.array(np.random.randint(10, 50, shape3))

result1 = array1 + array2

print(f"I have array of 3 shapes {shape1}, {shape2} and {shape3}")
print(f"Successfully added \n\n {array1} \n\n  and \n\n {array2}")
try:
    result2 = array1 + array3
except ValueError as e:
    print(
        f"If I addition: \n {array1} \n\n And \n\n {array3}  \n This will throw an error"
    )
    print(f"Caught an error: {e}")
