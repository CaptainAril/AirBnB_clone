<p align="center">
  <img src="https://raw.githubusercontent.com/CaptainAril/AirBnB_clone/master/img/ass1.png">
</p>


<h1 align="center">The AirBnB Project.</h1>
<p align="center">The Console.</p>

---

## Description :label:

The Alx AirBnB clone is a complete web application, integrating database storage, a back-end API, and front-end interface in a clone of AirBnB.

This team project is part of the (Alx) Holberton School Software Engineering program. </br>
It represents the first step towards building a full web application.

# Concept used in the project

### Unittest - and please work all together on tests cases
### Python packages concept page
### Serialization/Deserialization
### *args, **kwargs
### datetime
### More coming soon!

This first step consists of:
- a custom command-line interface for data management,
- and the base classes for the storage of this data.

## Usage 💻

The console works both in interactive mode and non-interactive mode, much like a Unix shell.
It prints a prompt **(hbnb)** and waits for the user for input.

Command | Example
------- | -------
Run the console | ```./console.py``` or ```python3 console.py```
Quit the console | ```(hbnb) quit```
Display the help for a command | ```(hbnb) help <command>```
Create an object (prints its id)| ```(hbnb) create <class>```
Show an object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Destroy an object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show all objects, or all instances of a class | ```(hbnb) all``` or ```(hbnb) all <class>```
Update an attribute of an object | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"``` or ```(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")```

### Interactive mode (example)

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all create destroy help quit show update

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Non-interactive mode (example)

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all create destroy help quit show update
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Execution:
<p align="center">
    <img src="https://raw.githubusercontent.com/CaptainAril/AirBnB_clone/master/img/ass2.png">
</p>


## Testing :straight_ruler:

The UnitTests for this Project are place and defined in the [tests](./tests)
folder.
Note: To run the entire test suite simultaneously, execute the following command below:


```
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```


## Authors :black_nib:

* **Obe Emmanuel Ogheneruro** <[CaptainAril](https://github.com/CaptainAril)>
* **Rotimi Adebowale Owolabi** <[Rohteemie](https://github.com/Rohteemie)>

