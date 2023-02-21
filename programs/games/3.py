Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

== RESTART: C:\Arunima\00 - projects\learning-python\programs\games\Hangman.py =



 _    _                                                  __        ___  
| |  | |                                                /_ |      / _ \ 
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     __   _| |     | | | |
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \    \ \ / / |     | | | |
| |  | | (_| | | | | (_| | | | | | | (_| | | | |    \ V /| |  _  | |_| |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     \_/ |_| (_)  \___/ 
                     __/ |                                              
                    |___/                                               


Welcome to Hangman v1.0!                                            
* Enter exit to abandon round and new to start a new round.             
Enter a difficulty level ( 1/[2]/3 ) : 3

Number of hints =  2

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[_] [_] [_] [_] [_] [_] [_] [_] 

>> 2
Please enter a valid guess.

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[_] [_] [_] [_] [_] [_] [_] [_] 

>> a
Correct!

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[_] [_] [_] [_] [a] [_] [_] [_] 

>> e
Correct!

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[_] [e] [_] [_] [a] [_] [_] [e] 

>> n
Correct!

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[_] [e] [_] [_] [a] [n] [_] [e] 

>> l
Incorrect! 5 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|          
|          
|        
|_________________


[_] [e] [_] [_] [a] [n] [_] [e] 


Incorrect guesses : ['l']


>> c
Correct!

 ________ 
|        |
|        |
|        |
|        O
|          
|          
|        
|_________________


[_] [e] [_] [_] [a] [n] [c] [e] 


Incorrect guesses : ['l']


>> b
Incorrect! 4 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|       /
|          
|        
|_________________


[_] [e] [_] [_] [a] [n] [c] [e] 


Incorrect guesses : ['l', 'b']


>> l
l is already guessed. Try again.
4 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|       /
|          
|        
|_________________


[_] [e] [_] [_] [a] [n] [c] [e] 


Incorrect guesses : ['l', 'b']


>> l
l is already guessed. Try again.
4 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|       /
|          
|        
|_________________


[_] [e] [_] [_] [a] [n] [c] [e] 


Incorrect guesses : ['l', 'b']


>> d
Correct!

 ________ 
|        |
|        |
|        |
|        O
|       /
|          
|        
|_________________


[d] [e] [_] [_] [a] [n] [c] [e] 


Incorrect guesses : ['l', 'b']


>> f
Correct!

 ________ 
|        |
|        |
|        |
|        O
|       /
|          
|        
|_________________


[d] [e] [f] [_] [a] [n] [c] [e] 


Incorrect guesses : ['l', 'b']


>> i
Correct!

 ________ 
|        |
|        |
|        |
|        O
|       /
|          
|        
|_________________


[d] [e] [f] [i] [a] [n] [c] [e] 


Incorrect guesses : ['l', 'b']


You win!
>> (new \ [exit]) : new



 _    _                                                  __        ___  
| |  | |                                                /_ |      / _ \ 
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     __   _| |     | | | |
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \    \ \ / / |     | | | |
| |  | | (_| | | | | (_| | | | | | | (_| | | | |    \ V /| |  _  | |_| |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     \_/ |_| (_)  \___/ 
                     __/ |                                              
                    |___/                                               


Welcome to Hangman v1.0!                                            
* Enter exit to abandon round and new to start a new round.             
Enter a difficulty level ( 1/[2]/3 ) : 3

Number of hints =  3

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[_] [_] [_] [_] [_] [_] [_] [_] [_] 

>> e
Incorrect! 5 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|          
|          
|        
|_________________


[_] [_] [_] [_] [_] [_] [_] [_] [_] 


Incorrect guesses : ['e']


>> a
Incorrect! 4 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|       /
|          
|        
|_________________


[_] [_] [_] [_] [_] [_] [_] [_] [_] 


Incorrect guesses : ['e', 'a']


>> i
Correct!

 ________ 
|        |
|        |
|        |
|        O
|       /
|          
|        
|_________________


[_] [_] [_] [_] [i] [_] [_] [_] [_] 


Incorrect guesses : ['e', 'a']


>> o
Correct!

 ________ 
|        |
|        |
|        |
|        O
|       /
|          
|        
|_________________


[_] [_] [_] [_] [i] [_] [o] [_] [_] 


Incorrect guesses : ['e', 'a']


>> u
Correct!

 ________ 
|        |
|        |
|        |
|        O
|       /
|          
|        
|_________________


[_] [_] [u] [_] [i] [_] [o] [u] [_] 


Incorrect guesses : ['e', 'a']


>> s
Correct!

 ________ 
|        |
|        |
|        |
|        O
|       /
|          
|        
|_________________


[_] [_] [u] [_] [i] [_] [o] [u] [s] 


Incorrect guesses : ['e', 'a']


>> d
Incorrect! 3 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|       /|
|          
|        
|_________________


[_] [_] [u] [_] [i] [_] [o] [u] [s] 


Incorrect guesses : ['e', 'a', 'd']


>> l
Correct!

 ________ 
|        |
|        |
|        |
|        O
|       /|
|          
|        
|_________________


[_] [l] [u] [_] [i] [_] [o] [u] [s] 


Incorrect guesses : ['e', 'a', 'd']


>> t
Correct!

 ________ 
|        |
|        |
|        |
|        O
|       /|
|          
|        
|_________________


[_] [l] [u] [t] [i] [_] [o] [u] [s] 


Incorrect guesses : ['e', 'a', 'd']


>> n
Correct!

 ________ 
|        |
|        |
|        |
|        O
|       /|
|          
|        
|_________________


[_] [l] [u] [t] [i] [n] [o] [u] [s] 


Incorrect guesses : ['e', 'a', 'd']


>> g
Correct!

 ________ 
|        |
|        |
|        |
|        O
|       /|
|          
|        
|_________________


[g] [l] [u] [t] [i] [n] [o] [u] [s] 


Incorrect guesses : ['e', 'a', 'd']


You win!
>> (new \ [exit]) : new



 _    _                                                  __        ___  
| |  | |                                                /_ |      / _ \ 
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     __   _| |     | | | |
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \    \ \ / / |     | | | |
| |  | | (_| | | | | (_| | | | | | | (_| | | | |    \ V /| |  _  | |_| |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     \_/ |_| (_)  \___/ 
                     __/ |                                              
                    |___/                                               


Welcome to Hangman v1.0!                                            
* Enter exit to abandon round and new to start a new round.             
Enter a difficulty level ( 1/[2]/3 ) : 1

Number of hints =  3

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[_] [_] [_] [_] [_] 

>> e
Incorrect! 5 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|          
|          
|        
|_________________


[_] [_] [_] [_] [_] 


Incorrect guesses : ['e']


>> a
Correct!

 ________ 
|        |
|        |
|        |
|        O
|          
|          
|        
|_________________


[a] [_] [_] [_] [_] 


Incorrect guesses : ['e']


>> i
Incorrect! 4 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|       /
|          
|        
|_________________


[a] [_] [_] [_] [_] 


Incorrect guesses : ['e', 'i']


>> o
Incorrect! 3 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|       /|
|          
|        
|_________________


[a] [_] [_] [_] [_] 


Incorrect guesses : ['e', 'i', 'o']


>> u
Correct!

 ________ 
|        |
|        |
|        |
|        O
|       /|
|          
|        
|_________________


[a] [u] [_] [u] [_] 


Incorrect guesses : ['e', 'i', 'o']


>> r
Correct!

 ________ 
|        |
|        |
|        |
|        O
|       /|
|          
|        
|_________________


[a] [u] [_] [u] [r] 


Incorrect guesses : ['e', 'i', 'o']


>> b
Incorrect! 2 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|       /|\
|          
|        
|_________________


[a] [u] [_] [u] [r] 


Incorrect guesses : ['e', 'i', 'o', 'b']


>> r
r is already guessed. Try again.
2 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|       /|\
|          
|        
|_________________


[a] [u] [_] [u] [r] 


Incorrect guesses : ['e', 'i', 'o', 'b']


>> g
Correct!

 ________ 
|        |
|        |
|        |
|        O
|       /|\
|          
|        
|_________________


[a] [u] [g] [u] [r] 


Incorrect guesses : ['e', 'i', 'o', 'b']


You win!
>> (new \ [exit]) : new



 _    _                                                  __        ___  
| |  | |                                                /_ |      / _ \ 
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     __   _| |     | | | |
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \    \ \ / / |     | | | |
| |  | | (_| | | | | (_| | | | | | | (_| | | | |    \ V /| |  _  | |_| |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     \_/ |_| (_)  \___/ 
                     __/ |                                              
                    |___/                                               


Welcome to Hangman v1.0!                                            
* Enter exit to abandon round and new to start a new round.             
Enter a difficulty level ( 1/[2]/3 ) : 3

Number of hints =  3

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[_] [_] [_] [_] [_] [_] [_] [_] [_] 

>> a
Incorrect! 5 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|          
|          
|        
|_________________


[_] [_] [_] [_] [_] [_] [_] [_] [_] 


Incorrect guesses : ['a']


>> e
Correct!

 ________ 
|        |
|        |
|        |
|        O
|          
|          
|        
|_________________


[_] [_] [_] [_] [e] [_] [e] [_] [_] 


Incorrect guesses : ['a']


>> i
Correct!

 ________ 
|        |
|        |
|        |
|        O
|          
|          
|        
|_________________


[i] [_] [_] [_] [e] [_] [e] [_] [_] 


Incorrect guesses : ['a']


>> o
Incorrect! 4 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|       /
|          
|        
|_________________


[i] [_] [_] [_] [e] [_] [e] [_] [_] 


Incorrect guesses : ['a', 'o']


>> u
Incorrect! 3 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|       /|
|          
|        
|_________________


[i] [_] [_] [_] [e] [_] [e] [_] [_] 


Incorrect guesses : ['a', 'o', 'u']


>> s
Incorrect! 2 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|       /|\
|          
|        
|_________________


[i] [_] [_] [_] [e] [_] [e] [_] [_] 


Incorrect guesses : ['a', 'o', 'u', 's']


>> b
Incorrect! 1 guesses remaining.

 ________ 
|        |
|        |
|        |
|        O
|       /|\
|       /
|        
|_________________


[i] [_] [_] [_] [e] [_] [e] [_] [_] 


Incorrect guesses : ['a', 'o', 'u', 's', 'b']


>> l
Correct!

 ________ 
|        |
|        |
|        |
|        O
|       /|\
|       /
|        
|_________________


[i] [_] [_] [l] [e] [_] [e] [_] [_] 


Incorrect guesses : ['a', 'o', 'u', 's', 'b']


>> d
Incorrect! 0 guesses remaining.


You lose...

 ________ 
|        |
|        |
|        |
|        O
|       /|\
|       / \
|        
|_________________


[i] [n] [c] [l] [e] [m] [e] [n] [t] 


Incorrect guesses : ['a', 'o', 'u', 's', 'b', 'd']
>> (new \ [exit]) : exit
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt
KeyboardInterrupt

====== RESTART: C:\Arunima\00 - projects\learning-python\programs\games\Hangman.py =====



 _    _                                                  __        ___  
| |  | |                                                /_ |      / _ \ 
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     __   _| |     | | | |
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \    \ \ / / |     | | | |
| |  | | (_| | | | | (_| | | | | | | (_| | | | |    \ V /| |  _  | |_| |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     \_/ |_| (_)  \___/ 
                     __/ |                                              
                    |___/                                               


Welcome to Hangman v1.0!                                            
* Enter exit to abandon round and new to start a new round.             
Enter a difficulty level ( 1/[2]/3 ) : 
  Setting difficulty level to default [2].

Number of hints =  2
Traceback (most recent call last):
  File "C:\Arunima\00 - projects\learning-python\programs\games\Hangman.py", line 367, in <module>
    main();
  File "C:\Arunima\00 - projects\learning-python\programs\games\Hangman.py", line 336, in main
    determineHints()
  File "C:\Arunima\00 - projects\learning-python\programs\games\Hangman.py", line 321, in determineHints
    print( "Available hints = ", availbleHints )
NameError: name 'availbleHints' is not defined. Did you mean: 'availableHints'?

====== RESTART: C:\Arunima\00 - projects\learning-python\programs\games\Hangman.py =====



 _    _                                                  __        ___  
| |  | |                                                /_ |      / _ \ 
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     __   _| |     | | | |
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \    \ \ / / |     | | | |
| |  | | (_| | | | | (_| | | | | | | (_| | | | |    \ V /| |  _  | |_| |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     \_/ |_| (_)  \___/ 
                     __/ |                                              
                    |___/                                               


Welcome to Hangman v1.0!                                            
* Enter exit to abandon round and new to start a new round.             
Enter a difficulty level ( 1/[2]/3 ) : 
  Setting difficulty level to default [2].

Number of hints =  2
Available hints =  ['j']
Available hints =  ['j', 'e']
Available hints =  ['j', 'e', 's']
Available hints =  ['j', 'e', 's', 't']

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[_] [_] [_] [_] 

>> 
====== RESTART: C:\Arunima\00 - projects\learning-python\programs\games\Hangman.py =====



 _    _                                                  __        ___  
| |  | |                                                /_ |      / _ \ 
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     __   _| |     | | | |
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \    \ \ / / |     | | | |
| |  | | (_| | | | | (_| | | | | | | (_| | | | |    \ V /| |  _  | |_| |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     \_/ |_| (_)  \___/ 
                     __/ |                                              
                    |___/                                               


Welcome to Hangman v1.0!                                            
* Enter exit to abandon round and new to start a new round.             
Enter a difficulty level ( 1/[2]/3 ) : 3

Number of hints =  2
Available hints =  ['e', 'x', 'p', 'l', 'i', 'c', 'i', 't']

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[_] [_] [_] [_] [_] [_] [_] [_] 

>> e
Correct!

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[e] [_] [_] [_] [_] [_] [_] [_] 

>> 
====== RESTART: C:\Arunima\00 - projects\learning-python\programs\games\Hangman.py =====



 _    _                                                  __        ___  
| |  | |                                                /_ |      / _ \ 
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     __   _| |     | | | |
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \    \ \ / / |     | | | |
| |  | | (_| | | | | (_| | | | | | | (_| | | | |    \ V /| |  _  | |_| |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     \_/ |_| (_)  \___/ 
                     __/ |                                              
                    |___/                                               


Welcome to Hangman v1.0!                                            
* Enter exit to abandon round and new to start a new round.             
Enter a difficulty level ( 1/[2]/3 ) : 3

Number of hints =  3
Available hints =  ['e', 'x', 'o', 'r', 'b', 'i', 't', 'a', 'n', 't']

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[_] [_] [_] [_] [_] [_] [_] [_] [_] [_] 

>> e

Number of hints =  3
Available hints =  ['e', 'x', 'o', 'r', 'b', 'i', 't', 'a', 'n', 't', 'e', 'x', 'o', 'r', 'b', 'i', 't', 'a', 'n', 't']
Correct!

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[e] [_] [_] [_] [_] [_] [_] [_] [_] [_] 

>> 
====== RESTART: C:\Arunima\00 - projects\learning-python\programs\games\Hangman.py =====



 _    _                                                  __        ___  
| |  | |                                                /_ |      / _ \ 
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     __   _| |     | | | |
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \    \ \ / / |     | | | |
| |  | | (_| | | | | (_| | | | | | | (_| | | | |    \ V /| |  _  | |_| |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     \_/ |_| (_)  \___/ 
                     __/ |                                              
                    |___/                                               


Welcome to Hangman v1.0!                                            
* Enter exit to abandon round and new to start a new round.             
Enter a difficulty level ( 1/[2]/3 ) : 3

Number of hints =  3
Available hints =  ['l', 'e', 'g', 'e', 'r', 'd', 'e', 'm', 'a', 'i', 'n']

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[_] [_] [_] [_] [_] [_] [_] [_] [_] [_] [_] 

>> i

Number of hints =  3
Available hints =  ['l', 'e', 'g', 'e', 'r', 'd', 'e', 'm', 'a', 'i', 'n']
Correct!

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[_] [_] [_] [_] [_] [_] [_] [_] [_] [i] [_] 

>> 
====== RESTART: C:\Arunima\00 - projects\learning-python\programs\games\Hangman.py =====



 _    _                                                  __        ___  
| |  | |                                                /_ |      / _ \ 
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     __   _| |     | | | |
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \    \ \ / / |     | | | |
| |  | | (_| | | | | (_| | | | | | | (_| | | | |    \ V /| |  _  | |_| |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     \_/ |_| (_)  \___/ 
                     __/ |                                              
                    |___/                                               


Welcome to Hangman v1.0!                                            
* Enter exit to abandon round and new to start a new round.             
Enter a difficulty level ( 1/[2]/3 ) : 3

Number of hints =  3
Traceback (most recent call last):
  File "C:\Arunima\00 - projects\learning-python\programs\games\Hangman.py", line 374, in <module>
    main();
  File "C:\Arunima\00 - projects\learning-python\programs\games\Hangman.py", line 341, in main
    determineHints()
  File "C:\Arunima\00 - projects\learning-python\programs\games\Hangman.py", line 322, in determineHints
    if guess == c:
NameError: name 'guess' is not defined

====== RESTART: C:\Arunima\00 - projects\learning-python\programs\games\Hangman.py =====



 _    _                                                  __        ___  
| |  | |                                                /_ |      / _ \ 
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     __   _| |     | | | |
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \    \ \ / / |     | | | |
| |  | | (_| | | | | (_| | | | | | | (_| | | | |    \ V /| |  _  | |_| |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     \_/ |_| (_)  \___/ 
                     __/ |                                              
                    |___/                                               


Welcome to Hangman v1.0!                                            
* Enter exit to abandon round and new to start a new round.             
Enter a difficulty level ( 1/[2]/3 ) : 3

Number of hints =  3
Available hints =  ['d', 'i', 'l', 'e', 't', 't', 'a', 'n', 't', 'e']

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[_] [_] [_] [_] [_] [_] [_] [_] [_] [_] 

>> t

Number of hints =  3
Available hints =  ['d', 'i', 'l', 'e', 't', 't', 'a', 'n', 't', 'e']
Correct!

 ________ 
|        |
|        |
|        |
|          
|          
|          
|        
|_________________


[_] [_] [_] [_] [t] [t] [_] [_] [t] [_] 

>> 
= RESTART: C:\Arunima\00 - projects\learning-python\programs\games\Hangman.py



 _    _                                                  __        ___  
| |  | |                                                /_ |      / _ \ 
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __     __   _| |     | | | |
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \    \ \ / / |     | | | |
| |  | | (_| | | | | (_| | | | | | | (_| | | | |    \ V /| |  _  | |_| |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|     \_/ |_| (_)  \___/ 
                     __/ |                                              
                    |___/                                               


Welcome to Hangman v1.0!                                            
* Enter exit to abandon round and new to start a new round.             
Enter a difficulty level ( 1/[2]/3 ) : 