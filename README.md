This "project" aims to create a logging system similar to Ice Cream, but aims to be smaller in scope and size. Calling db.eval(X) will tell you what line X was called on, X's type, as well as the value of X. Additionally, if X is a function, the function will be called and returned. 

Output can be surpressed with db.disable()

The following script will output the below text:

script:
```
from debugger import db

def main():
    a = [1,2,3,4,5]
    db.eval(a)

if __name__ == "__main__":
    main()
```

output:
```
db [5] | a <class 'list'>: [1, 2, 3, 4, 5]
```
