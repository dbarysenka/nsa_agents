# **Task Description**
```
Alice knows that NSA agents use the following algorithm to cipher their messages.
1) They delete all spaces and punctuation marks.
2) They replace all successive identical letters with only one such letter.
3) They insert two identical letters at an arbitrary place many times.
Alice has intercepted some messages which are "meaningless" sequences of letters that NSA agent Bob has sent
to another NSA agent Alice about possible Alice’s location. He wants to be able to restore the message as
it was after step 2). Help Alice write a program in Python that removes all pairs of identical letters from 
the message inserted in the third step. 
The program should be executed by calling 'python alice.py cipheredmessage.txt' from the Unix shell where 
"cipheredmessage.txt" is the name of a file with a ciphered message sent by Bob. The message consists of 
lowercase English letters and its length is at most 100 000. Output the message after step 2). 
The program should produce an answer in less than a few seconds.
Example
Execute: python alice.py somefile.txt
somefile.txt: wwaldaadicffenn
Output: alice
```

# **How to Run a script**

``` python alice.py cipheredmessage.txt pip3 install -r requirements.txt  ``` 

* Install python3, if missing
https://www.python.org/downloads/.


* Install dependencies using requirements.txt .
Its can be done with a command in the terminal,
namely "pip3 install -r requirements.txt"


* To run the script from terminal
you need to copy the path to the .py file and
write the following
construction: "python3 path-to-file",
where path-to-file is your path.


#### Using the logging method of the loguru library.
* No Handler, no Formatter, no Filter:
one function to rule them all
* Easier file logging with rotation / retention / compression
* Modern string formatting using braces style
* Exceptions catching within threads or main
* Pretty logging with colors
* Fully descriptive exceptions
* Better datetime handling
* Entirely compatible with standard logging
* 10x faster than built-in logging

