# Object Oriented Programming

Object-oriented programming has a few benefits over procedural programming.

1. object-oriented programming allows you to create large, modular programs that can easily expand over time;
2. object-oriented programs hide the implementation from the end-user.

Consider Python packages like Scikit-learn, pandas, and NumPy. These are all Python packages built with object-oriented programming. Scikit-learn, for example, is a relatively large and complex package built with object-oriented programming. This package has expanded over the years with new functionality and new algorithms.

When you train a machine learning algorithm with Scikit-learn, you don't have to know anything about how the algorithms work or how they were coded. You can focus directly on the modeling.

An object has two essential parts; *characteristics*, *actions*. Consider the followoing image of two object -  a salesperson and a shirt.

![](AWS-ML/OOP/OOP.png)

### Characteristics and Actions in English Grammar

Another way to think about characteristics and actions is in terms of English grammar. A characteristic would be a noun. On the other hand, an action would be a verb.

Let's pick something from the real-world: a dog. A few characteristics could be the dog's weight, color, breed, and height. These are all nouns. What actions would a dog take? A dog can bark, run, bite and eat. These are all verbs.

## Class, Object, Method, Attribute

Object-Oriented Programming (OOP) Vocabulary

1. **class** - a blueprint consisting of methods and attributes
2. **object** - an *instance* of a class. It can help to think of objects as something in the real world like a yellow pencil, a small dog, a blue shirt, etc. 
3. **attribute** - a descriptor or characteristic. Examples would be color, length, size, etc. These attributes can take on specific values like blue, 3 inches, large, etc.
4. **method** - an *action* that a class or object could take
5. **OOP** - a commonly used abbreviation for object-oriented programming
6. **encapsulation** - one of the fundamental ideas behind object-oriented programming is called encapsulation: you can combine functions and data all into a single entity. In object-oriented programming, this single entity is called a class. Encapsulation allows you to hide implementation details much like how the scikit-learn package hides the implementation of machine learning algorithms.

### Function vs Method

A function and a method look very similar. They both use the `def` keyword. They also have inputs and return outputs. The difference is that a method is **inside** of a class whereas a function is **outside** of a class.


### What is Self?

If you instantiate two objects, how does Python differentiate between these two object, say, shirt_one and shirt_two?

`self` tells Python where to look in the computer's memory for the shirt_one object. And then Python changes the price of the shirt_one object. When you call the change_price method, shirt_one.change_price(12), `self` is implicitly passed in.

*See the OOP Syntax Practice One notebook in quiz/shirt_exercise.ipynb*


## Set and Get Methods

These methods are used to access and change attributes of an object. A get method is for obtaining an attribute value. A set method is for changing an attribute value.

e.g a Shirt class:

`
    class Shirt:

        def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
            self._price = shirt_price

        def get_price(self):
        return self._price

        def set_price(self, new_price):
        self._price = new_price

`

Instantiating and using an object might look like this:

`

    shirt_one = Shirt('yellow', 'M', 'long-sleeve', 15)
    print(shirt_one.get_price())
    shirt_one.set_price(10)

`

One of the benefits of set and get methods is that, you can hide the implementation from your user. Maybe originally a variable was coded as a list and later became a dictionary. With set and get methods, you could easily change how that variable gets accessed. Without set and get methods, you'd have to go to every place in the code that accessed the variable directly and change the code.

### A Note about Attributes

There are some drawbacks to accessing attributes directly versus writing a method for accessing attributes. Why might it be better to change a value with a method instead of directly? Changing values via a method gives you more **flexibility** in the long-term. 

What if the units of measurement change, like the store was originally meant to work in US dollars and now has to handle Euros? Here's an example:

Uf you've changed attribute values directly, you'll have to go through your code and find all the places where US dollars were used, like:

`

    shirt_one.price = 10 # US dollars

`

and then manually change to Euros

`

    shirt_one.price = 8 # Euros

`

If you had used a method, then you would only have to change the method to convert from dollars to Euros.

`

    def change_price(self, new_price):
        self.price = new_price * 0.81 # convert dollars to Euros

    shirt_one.change_price(10)

`

