# Hiring Challenge

Welcome to our hiring challenge! We're excited to see what you can do and how you solve problems. Here's how the challenge works:

## Part 1

You'll find the task description for Part 1 in [this repository](./Part-1.md). You can solve it in any language of your choice. By the way, the languages we use at Melli include:

* Rust 🦀
* Kotlin 🤖
* Elm 🔥
* TypeScript 🦾
* Python 🐍

## Part 2

Once you've solved Part 1, you'll be able to decrypt the task description for Part 2. This part builds on what you've learned in Part 1, so be sure to complete it before moving on.

To decrypt the task description using `age`, run:

```
age --decrypt --output Part-2.md Part-2.md.encrypted
```

## Submission

To submit your solution, create a pull request to our GitHub repository. We'll review your code and get back to you with feedback. Please incoparate the solution of part 2 in your GitHub message so we know you solved the task and do it discreetly so that others can't copy your solution 😜.

We can't wait to see what you come up with! 🤗

## (Optional) Development Environment ❄️

Setting up a development environment and sharing it with your colleagues can be a very tedious and error-prone endeavor. At Melli, we use [Nix](https://nixos.org/) to solve the "it works on my machine"-problem. In case you haven't heard of Nix: It is a package manager, you can use to create highly-producible and isolated environments in a declarative way.

The repository comes with a Nix setup. Check out the [devshell.nix](devshell.nix) file: We have added some exemplary languages, you can enable them by uncommenting the respective lines. Of course, it is not mandatory to use Nix and you can use the setup you are most comfortable with. But it will give you an idea about our workflow here at Melli.
