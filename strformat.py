text = "This is {variable_a} formatted string".format(variable_a="variable based")
print(text)
text = "This is another {variable_a} formatted string with \
multiple variables like {a} {b} {c}.".format(
    variable_a="variable based", 
    a="some random", b="replacement", c="text")
print(text)

text = """So, {name}, the best part is formated strings you don't have to order it. 
And these keyword argument replacements, ({var_a}, {var_b}, {name}) can be reused over and over.
Seriously {name}, this is some fun formatting.""".format(
            name="priyanka", 
            var_a="Variable 1", 
            var_b="Variable 2")
print(text)
