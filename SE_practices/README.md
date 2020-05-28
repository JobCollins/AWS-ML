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


### Scenario 3

Let's walk through the git commands that go along with each Step in the scenario you just observed in the video above.

**Step 1**: Andrew commits his changes to the documentation branch, switches to the development branch, and pulls down the latest changes from the cloud on this development branch, including the change I merged previously for the friends group feature.
Commit changes on documentation branch

`git commit -m "standardized all docstrings in process.py" `

Switch to develop branch

`git checkout develop`

Pull latest changes on develop down

`git pull`

**Step 2**: Then, Andrew merges his documentation branch on the develop branch on his local repository, and then pushes his changes up to update the develop branch on the remote repository.
Merge documentation branch to develop

`git merge --no-ff documentation`

Push changes up to remote repository

`git push origin develop`

**Step 3**: After the team reviewed both of your work, they merge the updates from the development branch to the master branch. Now they push the changes to the master branch on the remote repository. These changes are now in production.
Merge develop to master

`git merge --no-ff develop`

Push changes up to remote repository

`git push origin master`



## Testing and Data Science

Problems that could occur in data science aren’t always easily detectable; you might have values being encoded incorrectly, features being used inappropriately, unexpected data breaking assumptions

To catch these errors, you have to check for the quality and accuracy of your analysis in addition to the quality of your code. Proper testing is necessary to avoid unexpected surprises and have confidence in your results.



**UNIT TEST**: a type of test that covers a “unit” of code, usually a single function, independently from the rest of the program.

The advantage of unit tests is that they are isolated from the rest of your program, and thus, no dependencies are involved. They don't require access to databases, APIs, or other external sources of information. However, passing unit tests isn’t always enough to prove that our program is working successfully. To show that all the parts of our program work with each other properly, communicating and transferring data between them correctly, we use integration tests. 

e.g you want to write a function that find the nearest perfect square less than or equal to a certain number. *. First intuition is to test it interactively on the terminal or jupyter notebook. This requires manual typing, repetition and uncertainty in accuracy. 

To install `pytest`, run `pip install -U pytest` in your terminal.

1. Create a test file starting with `test_`
2. Define unit test functions that start with `test_` inside the test file
3. Enter `pytest` into your terminal in the directory of your test file and it will detect these tests for you!

`test_` is the default - if you wish to change this, you can learn how to in this pytest configuration https://docs.pytest.org/en/latest/customize.html


In the test output, periods represent successful unit tests and F's represent failed unit tests. Since all you see is what test functions failed, it's wise to have only one `assert` statement per test. Otherwise, you wouldn't know exactly how many tests failed, and which tests failed.

Your tests won't be stopped by failed  `assert` statements, but it will stop if you have syntax errors.

*Check ***nearest.py***  and ***test_nearest.py*** for code*


**TEST DRIVEN DEVELOPMENT**: a development process where you write tests for tasks before you even write the code to implement those tasks.

1. ***TEST DRIVEN DEVELOPMENT***: writing tests before you write the code that’s being tested. Your test would fail at first, and you’ll know you’ve finished implementing a task when this test passes.
2. Tests can check for all the different scenarios and edge cases you can think of, before even starting to write your function. This way, when you do start implementing your function, you can run this test to get immediate feedback on whether it works or not in all the ways you can think of, as you tweak your function.
3. When refactoring or adding to your code, tests help you rest assured that the rest of your code didn't break while you were making those changes. Tests also helps ensure that your function behavior is repeatable, regardless of external parameters, such as hardware and time.

Test driven development for data science is relatively new and has a lot of experimentation and breakthroughs appearing.


## Logging

Logging is valuable for understanding the events that occur while running your program. For example, if you run your model over night and see that it's producing ridiculous results the next day, log messages can really help you understand more about the context in which this occurred.

### Log Messages

Logging is the process of recording messages to describe events that have occurred while running your software. 

**Tip: Be professional and clear**

`

    Bad: Hmmm... this isn't working???
    Bad: idk.... :(
    Good: Couldn't parse file.
    
`


**Tip: Be concise and use normal capitalization**

`

    Bad: Start Product Recommendation Process
    Bad: We have completed the steps necessary and will now proceed with the recommendation process for the records in our product database.
    Good: Generating product recommendations.

`

**Tip: Choose the appropriate level for logging**

1. DEBUG - level you would use for anything that happens in the program.
2. ERROR - level to record any error that occurs
3. INFO - level to record all actions that are user-driven or system specific, such as regularly scheduled operations

**Tip: Provide any useful information**

`
    Bad: Failed to read location data
    Good: Failed to read location data: store_id 8324971
`

