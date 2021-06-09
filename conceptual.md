### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?
restful routing is an industry standard to label the routes you create
- What is a resource?
it is a tool to help and simplify your code
- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?
because you cant encrypt and add security to the users profile
- What does idempotent mean? Which HTTP verbs are idempotent?
it means that the same function call can be used multiple times. GET, HEAD, OPTIONS, TRACE, PUT and DELETE.
- What is the difference between PUT and PATCH?
Put adds something to a specific model
patch updates something from a specific model
- What is one way encryption?
means you can only encrpyt and it takes alot more time to hack into it
- What is the purpose of a `salt` when hashing a password?
salt adds another layer of safety to the password people enter, it also alows random people to have similar passwords without getting an error
- What is the purpose of the Bcrypt module?
Bcrypt makes it easier in flask to add encrytption to forms for passwords
- What is the difference between authorization and authentication?
authorization is the app checking to see if you are allowed to acess certain aspects
authentication is the app checking to see if you are registered and allowed to continue