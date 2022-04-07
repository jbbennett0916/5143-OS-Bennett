So or this you will make it so that 
It automaticaly passes the time slice 
Number to the cpu you will have it saved as a variable 
that can be adjusted I'll just give it like 5 or something to start with maybe move up if it starts to suck because I fee like that is too short but it is a good one 
To test with 

For this you don't need to do anything with the Queue it will be sorted just like FCFS
The only thing you have to modify for this is you may have to overwrite your
Run function inside the CPU that then calls either NonRR() or RRrun()
You will always pass the time slice but it will only ever be passed into the 
RRrun() function it will either be saved as a variable or entered in by the user 

Will also have to add in a function that returns the job to the readyQueue if it is not complete 
This will Only ever be a thing for RRrun()


After this you just have to get your program to run with multiple CPU's which will
just require you adjusting your driver function 

ACTUALLY IT SEEMS SO MUCH EASIER TO JUST CREATE THE CPU WITH THE ALGO AND 
TIME SLICE i MAY JUST DO THAT AND YOU WILL ALSO HAVE TO DO THIS WITH READY
sINCE THESE ARE THE TWO CLASSES THAT ARE EFECED BY THE SCHEDULING ALGOS AND 
IT MAKES SENSE THAT THEY WOULD CONTAIN THAT IN THEIR CLASS INSTEAD OF THE DRIVER


THIS MEANS YOU WILL HAVE TO CHANGE THE READY QUEUE AND THE WAY IT SORTS BY BEING 
PASSED THE ALGO EXTERNALLY IN THE DRIVER FUNCTION

OKAY NEVER MIND I DECIDED TO MAKE IT EASIER ON MYSELF AND JUST PASS IT THROUGH THE DRIVER FUNCTION AS I COULD ALWAYS CHANGE IT AND THIS WOULD BE AN EASY FIX TO DO WHAT I
WAS DESCRIBING ABOVE 

THE ONLY THING THAT MAY GIVE YOU TROUBLE WITH THIS PROGRAM IS MAKING SURE THAT WHEN IT FINISES IN THE CPU IT DOESN'T GO TO READY ON THE SAME CLOCK TICK BUT I IMMAGINE 
I HAVE ALREADY SOLVED THIS BY MAKING SURE IT DOESN'T GO TO WAITING IN THE SAME CLOCK
TICK SO IT WILL PROBABLY BE FINE AS LONG AS I PLACE IT IN THE SAME STAGE AS THE PASS
TO THE WAITING QUEUEU ALTHOUGH MAYBE NOT 

