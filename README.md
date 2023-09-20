# Reverse Polish Notation Calculator Two Ways

## The Gist

This repo has two RPN calculators in it, each built in a different language, and each built to handle inputs in a different way. 
One is in Python and will allow the user a lot more leeway with their inputs, and another in TypeScript, where I was a little more strict on what was allowed to be put in the input. 

### Are you thinking, ~"That's cool, but why did you do two? And why did you make them operate differently?"

That's a good question, and there are a few reasons:
1. Python is my daily driver, so I wanted to write something that felt more clean, concise, and comfortable.
2. TS is what the team uses, so I wanted to write something that shows I can work with TypeScript as well.
3. I made them different so it didn't seem like I just got an AI tool to rewrite things + a couple of other reasons, but I'll talk about those in the **Features** section.

This is an _attempt_ to show skill in Python and assertiveness in TypeScript.

I do want to note that while I don't have professional experience working with TypeScript, I do have a lot of experience with
[Pydantic](https://docs.pydantic.dev/latest/), as in I use it daily, which is basically JS:TS::Python:Pydantic

## Features
Probably should split this into separate README's, and I would if this were a long-lasting project, but we're just rolling with it.
### Similarities:
These are uniform features across both calculators.
I used this list as a base
![image](https://github.com/SethCWilliams/rpn_calc/assets/43652084/9f47e496-4efe-4b38-ac24-c68fe1f674bd)

**List of other shared features branching off the root requirements:**
- Entering a 'c' for your input will clear the stack, allowing you to start fresh with new equations without terminating the calculator
- I chose to display the operand stack instead of the specific display number because it's a little difficult to keep track of what operands are available/still in play as you keep adding inputs. This should make it easier for the user to keep up with what's going on.
- Upon quitting the application, you will get one last output showing your final operand stack. This is just in case you have errors in previous commands so the stack didn't ouput. It's not as big of an issue in the Python application, but with the inputs in the TS calculator being more strict I thought it'd be good to have. 

### What makes them different?

I decided to not strongly type the Python calculator and just try to work with whatever input was given, throwing soft errors when a `token` doesn't match a valid input, but continuing to process remaining `tokens`. This stemmed from when I was going through and figuring out what an RPN calculator even was, and I saw how long some equations can get. If I'm manually typing in an equation that is 20+ characters long, the chances of me fat-fingering something are pretty high. Instead of having to enter the whole equation again, it will just kick out pieces that don't make sense. 

**For example:**

![image](https://github.com/SethCWilliams/rpn_calc/assets/43652084/45b6660f-5db4-47da-9085-8f15e0d6839e)

On the other hand, the TypeScript application takes advantage of the ability to strongly type inputs/outputs/objects/etc, so if something in the input doesn't line up with how an input should be formatted, you will be shown an error, and the stack will reset back to it's previous state prior to the most recent input. 

**For example:**

![image](https://github.com/SethCWilliams/rpn_calc/assets/43652084/427ef0a4-ed28-4345-a7fa-5d31ddfbfbf6)

This behavior doesn't hold true if the only issue is that there are too many operators. With those it will just do the calculations that it can and let you know you went too far.

**For example**

![image](https://github.com/SethCWilliams/rpn_calc/assets/43652084/e79ee698-034d-44ca-a022-c94f27fc7826)


## Installation and running

### Python calculator

This _should_ work with all Python versions that are installed on Mac operating systems, so Python shouldn't need to be installed. If you are having trouble running python or pip commands though, head [here](https://www.python.org/downloads/) and get an official download

I kept this as clean from other libraries/packages as possible since this isn't a language you all work in regularly. Wanted to make sure you had to install as little useless stuff as possible.

It only has one package dependency, and that's `pytest`

**Steps to run application:**

```
cd python_version/

python main.py
```

**Steps to run tests:**

```
cd python_version

pip install -r requirements.txt

pytest test_main.py
```

### TS calculator

I used the Node built-in [readline](https://nodejs.org/api/readline.html) module to act as my command line interface (pretty neat stuff that I feel like , so that along with [@types/node](https://www.npmjs.com/package/@types/node) are the main dependencies that need to be installed here. 

** Steps to run application:**

```
cd ts_version

npm install

tsc rpn-calculator.ts

ts-node rpn-calculator.js  
```

You'll notice that I don't have tests for the TS application. I honestly just ran out of time to dig into Jest. I do have it tracked in my issues here, so it's not an oversight, just something I ommitted for the sake of time since the Python application does have pretty expansive testing. 

You'll also notice that the Python calculator is more organized than the TS calculator. Another ommission for the sake of time since there are two separate calculators. Figured showing code structure in one was sufficient, and to be perfectly honest, I didn't want to run into too many hiccups on the TypeScript calculator with exporting functions, compiling multiple files, etc. I'm still fresh enough with TypeScript that I'm working my way through Maximillian Schwarzmuller's [Understanding TypeScript](https://www.udemy.com/course/understanding-typescript/) course, so I could be prone to fall for 'gotchas' and I didn't want to spend my time untangling that. If needed, I can go back and make the code a little more DRY, separating some code out into utility funtions, separating concerns into different files, etc. I made my choice based on this paragraph in the instructions since it demonstrates well-crafted code in one application, but diminishing code quality for the sake of time in another 

![image](https://github.com/SethCWilliams/rpn_calc/assets/43652084/2dbaa8c7-b4a7-4efc-ac44-60b32272ffaf)


## To exit you can either enter in 'q' or send an end-of-input indicator (ex. CTL + C).
