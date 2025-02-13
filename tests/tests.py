# from ElasticClass import ElasticLoader

"""elastic = ElasticLoader()
index_name = 'big_index_m'
# elastic.delete_index(index='big_index')
elastic.create_index(index=index_name, directory='jsons')


print("One match")
qm1 = [['languages', 'python']]
qmn1 = []
print(str(qm1))
print(str(qmn1))
print('\n'.join(elastic.get_by_multi_match(index_name, qm1, qmn1)), '\n\n\n')

print("Two matches")
qm2 = [['languages', 'python'], ['languages', 'shell']]
qmn2 = []
print(str(qm2))
print(str(qmn2))
print('\n'.join(elastic.get_by_multi_match(index_name, qm2, qmn2)), '\n\n\n')

print("Two matches with MUST_NOT var.")
qm4 = [['languages', 'python'], ['languages', 'shell']]
qmn4 = [['languages', 'Makefile']]
print(str(qm4))
print(str(qmn4))
print('\n'.join(elastic.get_by_multi_match(index_name, qm4, qmn4)), '\n\n\n')

print("Three matches with MUST_NOT var.")
qm4 = [['languages', 'python'], ['languages', 'shell'], ['languages', 'javascript']]
qmn4 = [['languages', 'Makefile']]
print(str(qm4))
print(str(qmn4))
print('\n'.join(elastic.get_by_multi_match(index_name, qm4, qmn4)), '\n\n\n')

print("MUST is equal MUST_NOT")
qm3 = [['languages', 'python'], ['languages', 'shell']]
qmn3 = [['languages', 'python'], ['languages', 'shell']]
print(str(qm3))
print(str(qmn3))
print('\n'.join(elastic.get_by_multi_match(index_name, qm3, qmn3)), '\n\n\n')

print("Three matches")
qm5 = [['languages', 'python'], ['languages', 'shell'], ['imports', 'requests']]
qmn5 = []
print(str(qm5))
print(str(qmn5))
print('\n'.join(elastic.get_by_multi_match(index_name, qm5, qmn5)), '\n\n\n')

print('Two matches, exact string')
qm5 = [['languages', 'python'], ['imports', 'cola functions counter CounterServer']]
qmn5 = []
print(str(qm5))
print(str(qmn5))
print('\n'.join(elastic.get_by_multi_match(index_name, qm5, qmn5)), '\n\n\n')

print('Two matches, not exact string')
qm5 = [['languages', 'python'], ['imports', 'cola CounterServer']]
qmn5 = []
print(str(qm5))
print(str(qmn5))
print('\n'.join(elastic.get_by_multi_match(index_name, qm5, qmn5)), '\n\n\n')

print('Three matches, not exact string')
qm5 = [['languages', 'python'], ['imports', 'monkeytype nonetype']]
qmn5 = []
print(str(qm5))
print(str(qmn5))
print('\n'.join(elastic.get_by_multi_match(index_name, qm5, qmn5)), '\n\n\n')

print('Three matches, not exact (bad) string')
qm5 = [['languages', 'python'], ['imports', 'monkeyType Nonetype']]
qmn5 = []
print(str(qm5))
print(str(qmn5))
print('\n'.join(elastic.get_by_multi_match(index_name, qm5, qmn5)), '\n\n\n')

print("Simple MUST and MUST_NOT")
qm1 = [['imports', 'base64']]
qmn1 = [['languages', 'shell']]
print(str(qm1))
print(str(qmn1))
print('\n'.join(elastic.get_by_multi_match(index_name, qm1, qmn1)), '\n\n\n')

print("query with dict")
q = {'query': {'bool': {'must': [{'multi_match': {'fields': ['imports'],
    'query': 'base64', 'type': 'cross_fields', 'operator': 'AND'}}],
    'must_not': [{'multi_match': {'fields': ['languages'], 'query':
    'shell', 'type': 'cross_fields', 'operator': 'AND'}}]}}}
print(q)
print(elastic.get_by_multi_match(q))
'''

'''
print("One match")
qm1 = [['languages', 'python']]
qmn1 = []
print(str(qm1))
print(str(qmn1))
print('\n'.join(elastic.get_by_repo(index_name, qm1, qmn1)), '\n\n\n')

print("Two matches")
qm2 = [['languages', 'python'], ['languages', 'shell']]
qmn2 = []
print(str(qm2))
print(str(qmn2))
print('\n'.join(elastic.get_by_repo(index_name, qm2, qmn2)), '\n\n\n')

print("Two matches with MUST_NOT var.")
qm4 = [['languages', 'python'], ['languages', 'shell']]
qmn4 = [['languages', 'Makefile']]
print(str(qm4))
print(str(qmn4))
print('\n'.join(elastic.get_by_repo(index_name, qm4, qmn4)), '\n\n\n')

print("Three matches with MUST_NOT var.")
qm4 = [['languages', 'python'], ['languages', 'shell'], ['languages', 'javascript']]
qmn4 = [['languages', 'Makefile']]
print(str(qm4))
print(str(qmn4))
print('\n'.join(elastic.get_by_repo(index_name, qm4, qmn4)), '\n\n\n')

print("MUST is equal MUST_NOT")
qm3 = [['languages', 'python'], ['languages', 'shell']]
qmn3 = [['languages', 'python'], ['languages', 'shell']]
print(str(qm3))
print(str(qmn3))
print('\n'.join(elastic.get_by_repo(index_name, qm3, qmn3)), '\n\n\n')

print("Three matches")
qm5 = [['languages', 'python'], ['languages', 'shell'], ['imports', 'requests']]
qmn5 = []
print(str(qm5))
print(str(qmn5))
print('\n'.join(elastic.get_by_repo(index_name, qm5, qmn5)), '\n\n\n')

print('Two matches, exact string')
qm5 = [['languages', 'python'], ['imports', 'cola functions counter CounterServer']]
qmn5 = []
print(str(qm5))
print(str(qmn5))
print('\n'.join(elastic.get_by_repo(index_name, qm5, qmn5)), '\n\n\n')

print('Two matches, not exact string')
qm5 = [['languages', 'python'], ['imports', 'cola CounterServer']]
qmn5 = []
print(str(qm5))
print(str(qmn5))
print('\n'.join(elastic.get_by_repo(index_name, qm5, qmn5)), '\n\n\n')

print('Three matches, not exact string')
qm5 = [['languages', 'python'], ['imports', 'monkeytype nonetype']]
qmn5 = []
print(str(qm5))
print(str(qmn5))
print('\n'.join(elastic.get_by_repo(index_name, qm5, qmn5)), '\n\n\n')

print('Three matches, not exact (bad) string')
qm5 = [['languages', 'python'], ['imports', 'monkeyType Nonetype']]
qmn5 = []
print(str(qm5))
print(str(qmn5))
print('\n'.join(elastic.get_by_repo(index_name, qm5, qmn5)), '\n\n\n')

print("Simple MUST and MUST_NOT")
qm1 = [['imports', 'base64']]
qmn1 = [['languages', 'shell']]
print(str(qm1))
print(str(qmn1))
print('\n'.join(elastic.get_by_repo(index_name, qm1, qmn1)), '\n\n\n')
"""

import spacy
# from spacy.lang.en import English
nlp = spacy.load("en_core_web_sm")
text = """Do you ever use print() or log() to debug your code? Of course you do. IceCream, or ic for short, makes print debugging a little sweeter.

ic() is like print(), but better:

It prints both expressions/variable names and their values.
It's 40% faster to type.
Data structures are pretty printed.
Output is syntax highlighted.
It optionally includes program context: filename, line number, and parent function.
IceCream is well tested, permissively licensed, and supports Python 2, Python 3, PyPy2, and PyPy3.

Inspect Variables
Have you ever printed variables or expressions to debug your program? If you've ever typed something like

print(foo('123'))
or the more thorough

print("foo('123')", foo('123'))
then ic() is here to help. With arguments, ic() inspects itself and prints both its own arguments and the values of those arguments.

from icecream import ic

def foo(i):
    return i + 333

ic(foo(123))
Prints

ic| foo(123): 456
Similarly,

d = {'key': {1: 'one'}}
ic(d['key'][1])

class klass():
    attr = 'yep'
ic(klass.attr)
Prints

ic| d['key'][1]: 'one'
ic| klass.attr: 'yep'
Just give ic() a variable or expression and you're done. Easy.

Inspect Execution
Have you ever used print() to determine which parts of your program are executed, and in which order they're executed? For example, if you've ever added print statements to debug code like

def foo():
    print(0)
    first()

    if expression:
        print(1)
        second()
    else:
        print(2)
        third()
then ic() helps here, too. Without arguments, ic() inspects itself and prints the calling filename, line number, and parent function.

from icecream import ic

def foo():
    ic()
    first()

    if expression:
        ic()
        second()
    else:
        ic()
        third()
Prints

ic| example.py:4 in foo()
ic| example.py:11 in foo()
Just call ic() and you're done. Simple.

Return Value
ic() returns its argument(s), so ic() can easily be inserted into pre-existing code.

>>> a = 6
>>> def half(i):
>>>     return i / 2
>>> b = half(ic(a))
ic| a: 6
>>> ic(b)
ic| b: 3
Miscellaneous
ic.format(*args) is like ic() but the output is returned as a string instead of written to stderr.

>>> from icecream import ic
>>> s = 'sup'
>>> out = ic.format(s)
>>> print(out)
ic| s: 'sup'
Additionally, ic()'s output can be entirely disabled, and later re-enabled, with ic.disable() and ic.enable() respectively.

from icecream import ic

ic(1)

ic.disable()
ic(2)

ic.enable()
ic(3)
Prints

ic| 1: 1
ic| 3: 3
ic() continues to return its arguments when disabled, of course; no existing code with ic() breaks.

Import Tricks
To make ic() available in every file without needing to be imported in every file, you can install() it. For example, in a root A.py:

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from icecream import install
install()

from B import foo
foo()
and then in B.py, which is imported by A.py, just call ic():

# -*- coding: utf-8 -*-

def foo():
    x = 3
    ic(x)
install() adds ic() to the builtins module, which is shared amongst all files imported by the interpreter. Similarly, ic() can later be uninstall()ed, too.

ic() can also be imported in a manner that fails gracefully if IceCream isn't installed, like in production environments (i.e. not development). To that end, this fallback import snippet may prove useful:

try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa
Configuration
ic.configureOutput(prefix, outputFunction, argToStringFunction, includeContext) can be used to adopt a custom output prefix (the default is ic| ), change the output function (default is to write to stderr), customize how arguments are serialized to strings, and/or include the ic() call's context (filename, line number, and parent function) in ic() output with arguments.

>>> from icecream import ic
>>> ic.configureOutput(prefix='hello -> ')
>>> ic('world')
hello -> 'world'
prefix can optionally be a function, too.

>>> import time
>>> from icecream import ic
>>>  
>>> def unixTimestamp():
>>>     return '%i |> ' % int(time.time())
>>>
>>> ic.configureOutput(prefix=unixTimestamp)
>>> ic('world')
1519185860 |> 'world': 'world'
outputFunction, if provided, is called with ic()'s output instead of that output being written to stderr (the default).

>>> import logging
>>> from icecream import ic
>>>
>>> def warn(s):
>>>     logging.warning(s)
>>>
>>> ic.configureOutput(outputFunction=warn)
>>> ic('eep')
WARNING:root:ic| 'eep': 'eep'
argToStringFunction, if provided, is called with argument values to be serialized to displayable strings. The default is PrettyPrint's pprint.pformat(), but this can be changed to, for example, handle non-standard datatypes in a custom fashion.

>>> from icecream import ic
>>>
>>> def toString(obj):
>>>    if isinstance(obj, str):
>>>        return '[!string %r with length %i!]' % (obj, len(obj))
>>>    return repr(obj)
>>>
>>> ic.configureOutput(argToStringFunction=toString)
>>> ic(7, 'hello')
ic| 7: 7, 'hello': [!string 'hello' with length 5!]
The default argToStringFunction is icecream.argumentToString, and has methods to register and unregister functions to be dispatched for specific classes using functools.singledispatch. It also has a registry property to view registered functions.

>>> from icecream import ic, argumentToString
>>> import numpy as np
>>>
>>> # Register a function to summarize numpy array
>>> @argumentToString.register(np.ndarray)
>>> def _(obj):
>>>     return f"ndarray, shape={obj.shape}, dtype={obj.dtype}"
>>>
>>> x = np.zeros((1, 2))
>>> ic(x)
ic| x: ndarray, shape=(1, 2), dtype=float64
>>>
>>> # View registered functions
>>> argumentToString.registry
mappingproxy({object: <function icecream.icecream.argumentToString(obj)>,
              numpy.ndarray: <function __main__._(obj)>})
>>>
>>> # Unregister a function and fallback to the default behavior
>>> argumentToString.unregister(np.ndarray)
>>> ic(x)
ic| x: array([[0., 0.]])
includeContext, if provided and True, adds the ic() call's filename, line number, and parent function to ic()'s output.

>>> from icecream import ic
>>> ic.configureOutput(includeContext=True)
>>>
>>> def foo():
>>>   ic('str')
>>> foo()
ic| example.py:12 in foo()- 'str': 'str'
includeContext is False by default.

Installation
Installing IceCream with pip is easy.

$ pip install icecream
Related Python libraries
ic() uses executing by @alexmojaki to reliably locate ic() calls in Python source. It's magic.

IceCream in Other Languages
Delicious IceCream should be enjoyed in every language.

Dart: icecream
Rust: icecream-rs
Node.js: node-icecream
C++: IceCream-Cpp
C99: icecream-c
PHP: icecream-php
Go: icecream-go
Ruby: Ricecream
Java: icecream-java
R: icecream
Lua: icecream-lua
Clojure(Script): icecream-cljc
Bash: IceCream-Bash
If you'd like a similar ic() function in your favorite language, please open a pull request! IceCream's goal is to sweeten print debugging with a handy-dandy ic() function in every language."""
doc = nlp(text)
print(doc.ents)
