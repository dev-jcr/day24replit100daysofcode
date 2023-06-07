# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Invalid Syntax

```python
def biggerNumber(number1 number2):
  if(number1 > number2):
    print(number 1, "is bigger")
  else:
    print(number 2, "is bigger")

biggerNumber (18,332)
```

<details> <summary> 👀 Answer </summary>

You need a `,`. Remember, you have to add a comma in between each variable that you expect to be a parameter. You can have as many arguments as you want. Remember, though, if you create *two* arguments, you must also call *two* arguments.

```python
def biggerNumber(number1, number2):
  if(number1 > number2):
    print(number1, "is bigger")
  else:
    print(number2, "is bigger")

biggerNumber (18,332)
```

</details>

