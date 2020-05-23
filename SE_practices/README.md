# Software Engineering Practices

This document is about the following practices of software engineering and how they apply in data science.

1. Writing clean and modular code
2. Writing efficient code
3. Code refactoring
4. Adding meaningful documentation
5. Using version control


## Clean and Modular code

**Production Code**: code run on production servers to handle live users and data of intended audience. Note this is different from *production quality cod*e*, which describes code that meets expectations in reliability, efficiency, etc., for production.

1. The code needs to be ***clean*** i.e. *readable, simple, concise* that is crucial for collaboration and maintainability in software development.

2. The code needs to be ***modular*** i.e. logically broken up into *functions and modules* this proves efficiency and reliability.
Encapsulate code in modules (files) and call the code (import) in other modules - just like you'd encapsulate logic code in functions.

A modular analogy is like organizing your clothes in different drawers. One for tshirts, another for socks, another for trousers etc. This makes it easier for you to find your clothes. Modularizing your code - or breaking up your code into logical functions and modules - really helps you organize your program in cleaner and more efficient ways. 


## Refactoring Code

**Refactoring**: after you have achieved a working model always go back to restructure code to improve internal structure of code without changing external functionality. Gives an opportunity to clean and modularize code after your code has worked.

Allocating time to do this is essential to producing high quality code. Despite the initial time and effort required, this really pays off by speeding up your development time in the long run.

### Meaningful names

**Tip: Use meaningful names**

***Be descriptive and imply type*** - E.g. for booleans, you can prefix with is_ or has_ to make it clear it is a condition. You can also use part of speech to imply types, like verbs for functions and nouns for variables.

***Be consistent but clearly differentiate*** - E.g. age_list and age is easier to differentiate than ages and age.

***Avoid abbreviations and especially single letters*** - (Exception: counters and common math variables) Choosing when these exceptions can be made can be determined based on the audience for your code. If you work with other data scientists, certain variables may be common knowledge. While if you work with full stack engineers, it might be necessary to provide more descriptive names in these cases as well.

***Long names != descriptive names*** - You should be descriptive, but only with relevant information. E.g. good functions names describe what they do well without including details about implementation or highly specific uses.


### Nice Whitespace

**Tip: Use whitespace properly**

1. Organize your code with consistent indentation - the standard is to use 4 spaces for each indent. You can make this a default in your text editor.
2. Separate sections with blank lines to keep your code well organized and readable.
3. Try to limit your lines to around 79 characters, which is the guideline given in the PEP 8 style guide. In many good text editors, there is a setting to display a subtle line that indicates where the 79 character limit is.


### Modular Code
**Tip: DRY (Don't Repeat Yourself)**
Don't repeat yourself! Modularization allows you to reuse parts of your code. Generalize and consolidate repeated code in functions or loops.

**Tip: Abstract out logic to improve readability**
Abstracting out code into a function not only makes it less repetitive, but also improves readability with descriptive function names. Although your code can become more readable when you abstract out logic into functions, it is possible to over-engineer this and have way too many modules, so use your judgement.

**Tip: Minimize the number of entities (functions, classes, modules, etc.)**
There are tradeoffs to having function calls instead of inline logic. If you have broken up your code into an unnecessary amount of functions and modules, you'll have to jump around everywhere if you want to view the implementation details for something that may be too small to be worth it. Creating more modules doesn't necessarily result in effective modularization.

**Tip: Functions should do one thing**
Each function you write should be focused on doing one thing. If a function is doing multiple things, it becomes more difficult to generalize and reuse. Generally, if there's an "and" in your function name, consider refactoring.

**Tip: Arbitrary variable names can be more effective in certain functions**
Arbitrary variable names in general functions can actually make the code more readable.

**Tip: Try to use fewer than three arguments per function**
Try to use no more than three arguments when possible. This is not a hard rule and there are times it is more appropriate to use many parameters. But in many cases, it's more effective to use fewer arguments. Remember we are modularizing to simplify our code and make it more efficient to work with. If your function has a lot of parameters, you may want to rethink how you are splitting this up.

***See example dirty.py versus clean.py, and modular.py versus crafty.py***

### Efficient Code
Helps to reduce runtime, and takes up less memory space.
1. Use vector operations over loops e.g. *finding common items using ***numpy intersect*** and ***numpy arrays*** *
2. Know your data structures and which methods are faster e.g. *sets are faster than lists*

See how we implement this in the *optimizing code* jupyter notebooks.



## Documentation

**DOCUMENTATION**: additional text or illustrated information that comes with or is embedded in the code of software.

Helpful for clarifying complex parts of code, making your code easier to navigate, and quickly conveying how and why different components of your program are used.

Several types of documentation can be added at different levels of your program:
1. In-line Comments - line level
2. Docstrings - module and function level
3. Project Documentation - project level

### In-line Comments

In-line comments are text following hash symbols throughout your code. They are used to explain parts of your code, and really help future contributors understand your work.

One way comments are used is to document the major steps of complex code to help readers follow. Then, you may not have to understand the code to follow what it does. However, others would argue that this is using comments to justify bad code, and that if code requires comments to follow, it is a sign refactoring is needed.

Comments are valuable for explaining where code cannot. For example, the history behind why a certain method was implemented a specific way. Sometimes an unconventional or seemingly arbitrary approach may be applied because of some obscure external variable causing side effects. These things are difficult to explain with code.

### Docstrings

Docstring, or documentation strings, are valuable pieces of documentation that explain the functionality of any function or module in your code. Ideally, each of your functions should always have a docstring.

Docstrings are surrounded by triple quotes. The first line of the docstring is a brief explanation of the function's purpose.

If you think that the function is complicated enough to warrant a longer description, you can add a more thorough paragraph after the one line summary.


e.g.

`

    def population_density(population, land_area):

        """Calculate the population density of an area.

        Args:
        population: int. The population of the area
        land_area: int or float. This function is unit-agnostic, if you pass in values in terms 
        of square km or square miles the function will return a density in those units.

        Returns:
        population_density: population/land_area. The population density of a 
        particular area.
        """
        return population / land_area

`

The next element of a docstring is an explanation of the function's arguments. Here you list the arguments, state their purpose, and state what types the arguments should be. Finally it is common to provide some description of the output of the function. Every piece of the docstring is optional; however, doc strings are a part of good coding practice.


### Project Documentation

Project documentation is essential for getting others to understand why and how your code is relevant to them, whether they are potentials users of your project or developers who may contribute to your code. A great first step in project documentation is your README file. It will often be the first interaction most users will have with your project.

Whether it's an application or a package, your project should absolutely come with a README file. At a minimum, this should explain what it does, list its dependencies, and provide sufficiently detailed instructions on how to use it. You want to make it as simple as possible for others to understand the purpose of your project, and quickly get something working.


## Version Control in Data Science


### Scenario #1

Let's walk through the git commands that go along with each step in the scenario you just observed in the video above.

**STEP 1**: You have a local version of this repository on your laptop, and to get the latest stable version, you pull from the develop branch.
Switch to the develop branch

`git checkout develop`

Pull latest changes in the develop branch
`git pull`

**STEP 2**: When you start working on this demographic feature, you create a new branch for this called demographic, and start working on your code in this branch.
Create and switch to new branch called demographic from develop branch

`git checkout -b demographic`

Work on this new feature and commit as you go

`
    git commit -m 'added gender recommendations'

    git commit -m 'added location specific recommendations'
    
    ...
`

**STEP 3**: However, in the middle of your work, you need to work on another feature. So you commit your changes on this demographic branch, and switch back to the develop branch.
Commit changes before switching

`git commit -m 'refactored demographic gender and location recommendations '`

Switch to the develop branch
`git checkout develop`

**STEP 4**: From this stable develop branch, you create another branch for a new feature called friend_groups.
Create and switch to new branch called friend_groups from develop branch

`git checkout -b friend_groups`

**STEP 5**: After you finish your work on the friend_groups branch, you commit your changes, switch back to the development branch, merge it back to the develop branch, and push this to the remote repository’s develop branch.
Commit changes before switching

`git commit -m 'finalized friend_groups recommendations '`

Switch to the develop branch
`git checkout develop`

Merge friend_groups branch to develop
`git merge --no-ff friends_groups`

Push to remote repository
`git push origin develop`

**STEP 6**: Now, you can switch back to the demographic branch to continue your progress on that feature.
Switch to the demographic branch

`git checkout demographic`


### Scenario 2

Let's walk through the git commands that go along with each step in the scenario you just observed in the video above.

**Step 1**: You check your commit history, seeing messages of the changes you made and how well it performed.
View log history

`git log`

**Step 2**: The model at this commit seemed to score the highest, so you decide to take a look.
Checkout a commit

`git checkout bc90f2cbc9dc4e802b46e7a153aa106dc9a88560`

After inspecting your code, you realize what modifications made this perform well, and use those for your model.

**Step 3**: Now, you’re pretty confident merging this back into the development branch, and pushing the updated recommendation engine.
Switch to develop branch

`git checkout develop`

Merge friend_groups branch to develop

`git merge --no-ff friend_groups`

Push changes to remote repository

`git push origin develop`