#Intro

Troubleshooting is fixing problems in the system running the applications.
Debugging is fixing a problem in the code of the application.

1. Getting information
2. Finding the root causes
3. Performing the necessary remediation

ab - apache benchmark (example: ab -n 500 emap.conselldemallorca.net/)
strace - print all the system calls
iotop
iostat
vmstat
ionice
iftop
rsync -bwlimit #limit bandwith
tickle #program to limit band width
time ./script.py - give you time of user, real and sys of a command or program
pidof- list of pid of name
ps ax | less
memcached
kcachegrind -
rsync
netstat
ulimit - creates a core file that stores information related to a crash
gdb -c core example - help debug the print
backtrace - show a summary of the function calls that were used to the point where the failure occurs
pdb3 program.py param.csv - profiler python
lsof | grep deleted - files can be created and marked as deleted right after but deleted when process finishes

--python3
psutil.cpu_percent()
psutil.disk_io_counters()
psutil.net_io_counters()



#Monitoring Tools

Check out the following links for more information:

    https://docs.microsoft.com/en-us/sysinternals/downloads/procmon 

    http://www.brendangregg.com/linuxperf.html

    http://brendangregg.com/usemethod.html

    Activity Monitor in Mac:

    Performance Monitor on Windows

    https://www.digitalcitizen.life/how-use-resource-monitor-windows-7

    https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer

    https://en.wikipedia.org/wiki/Cache_(computing)

    https://www.reddit.com/r/linux/comments/d7hx2c/why_nice_levels_are_a_placebo_and_have_been_for_a/

#More About Improving Our Code

Check out the following links for more information:

https://en.wikipedia.org/wiki/Profiling_(computer_programming)


#More About Complex Slow Systems

We only touched briefly on the ways we can use concurrency to improve our programs. If you're interested in learning more, this article from Real Python has a lot of details on the different ways to use concurrency in Python.

Check out the following links for more information:

https://realpython.com/python-concurrency/

https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32

#Resources for Understanding Crashes

There's a ton of different reasons why a computer might crash. This Scientific American article discusses many of the possible reasons, including hardware problems and issues with the overall operating system or the applications on top. 

On Linux or MacOS, the worst kind of crash is called a Kernel Panic. On Windows, it's known as the Blue Screen of Death. These are situations where the computer completely stops responding and only a reboot can make it work again. They don't happen often, but it's good to understand what they mean: the whole OS encountered an error and it can't recover.

We called out that reading logs is super important. You should know how to read logs on the operating system that you're using. Here are some resources for this:

    How to find logs on Windows 10 (Digital Masters Magazine) https://www.digitalmastersmag.com/magazine/tip-of-the-day-how-to-find-crash-logs-on-windows-10/

    How to view the System Log on a Mac (How-to Geek) https://www.howtogeek.com/356942/how-to-view-the-system-log-on-a-mac/

    How to check system logs on Linux (FOSS Linux) https://www.fosslinux.com/8984/how-to-check-system-logs-on-linux-complete-usage-guide.htm

You also need to be familiar with the tools available in your OS to diagnose problems. These are the tools we called out, but you don't need to limit yourself to them:

    Process Monitor for Windows (Microsoft) https://docs.microsoft.com/en-us/sysinternals/downloads/procmon

    Linux strace command tutorial for beginners (HowtoForge)  https://www.howtoforge.com/linux-strace-command/

    How to trace your system calls on Mac OS (/etc/notes) https://etcnotes.com/posts/system-call/
 
#Resources for Debugging Crashes

Check out the following links for more information:

    https://realpython.com/python-concurrency/

    https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32

    https://stackoverflow.com/questions/33047452/definitive-list-of-common-reasons-for-segmentation-faults

    https://sites.google.com/a/case.edu/hpcc/home/important-notes-for-new-users/debugging-segmentation-faults

Readable Python code on GitHub:
Resources for Debugging Crashes

Check out the following links for more information:

    https://realpython.com/python-concurrency/

    https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32

    https://stackoverflow.com/questions/33047452/definitive-list-of-common-reasons-for-segmentation-faults

    https://sites.google.com/a/case.edu/hpcc/home/important-notes-for-new-users/debugging-segmentation-faults

Readable Python code on GitHub:

    https://github.com/fogleman/Minecraft

    https://github.com/cherrypy/cherrypy

    https://github.com/pallets/flask

    https://github.com/tornadoweb/tornado

    https://github.com/gleitz/howdoi

    https://github.com/bottlepy/bottle/blob/master/bottle.py

    https://github.com/sqlalchemy/sqlalchemy
    https://github.com/fogleman/Minecraft

    https://github.com/cherrypy/cherrypy

    https://github.com/pallets/flask

    https://github.com/tornadoweb/tornado

    https://github.com/gleitz/howdoi

    https://github.com/bottlepy/bottle/blob/master/bottle.py

    https://github.com/sqlalchemy/sqlalchemy

Resources for Debugging Crashes

Check out the following links for more information:

    https://realpython.com/python-concurrency/

    https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32

    https://stackoverflow.com/questions/33047452/definitive-list-of-common-reasons-for-segmentation-faults

    https://sites.google.com/a/case.edu/hpcc/home/important-notes-for-new-users/debugging-segmentation-faults

Readable Python code on GitHub:

    https://github.com/fogleman/Minecraft

    https://github.com/cherrypy/cherrypy

    https://github.com/pallets/flask

    https://github.com/tornadoweb/tornado

    https://github.com/gleitz/howdoi

    https://github.com/bottlepy/bottle/blob/master/bottle.py

    https://github.com/sqlalchemy/sqlalchemy

#More About Managing Resources

Check out the following links for more information:

    https://realpython.com/python-concurrency/

    https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32

    https://www.pluralsight.com/blog/tutorials/how-to-profile-memory-usage-in-python

    https://www.linuxjournal.com/content/troubleshooting-network-problems

#More About Making the Best Use of Our Time

Check out the following link for more information:

    https://blog.rescuetime.com/how-to-prioritize/

#More About Preventing Future Breakage

Preventing future breakage is a bit of a dynamic subject. Probably the most useful techniques here are identifying, isolating, and managing problem domains and failure domains. 

Problem Domains just describe the complexity of a given problem that one is trying to solve. Let’s look at an example below:

For example: counting the number of occurrences of a specific word in one of Shakespeare’s plays, like Hamlet. This is an indexing problem. And its problem domain is fairly limited in scope. It’s a single word, and a single play. A bit of BASH could easily solve this problem. So the problem domain is small, and the technical solution is fairly simple.

However, if the scope is widened slightly to include all of Shakespeare’s plays, the problem domain becomes larger. Any software solution used to try and solve this indexing problem has to now handle various logic that it did not have to handle before, like consolidating word occurrences in various plays. I.e. the word ‘Brevity’ may occur at least once in Hamlet, and N number of times in various other plays. Managing N occurrences of ‘Brevity’ over M works of Shakespeare is an order of magnitude more complex in terms of describing the problem domain. A bit of BASH could solve this problem, but it might be difficult.

If the problem becomes slightly more complex, such as finding the occurrences of various synonyms to a given word, then the problem domain becomes equally large. Managing original words, their synonyms, and their hit-count across multiple works of Shakespeare is even MORE complex.

So why is any of this useful? Well, if one can easily describe and reason about a problem in a lot of detail, they understand the Problem Domain fairly well. Producing a software solution for a given problem becomes easier when the Software Engineer understands the problem domain fairly well. Of course, building a good understanding of the Problem Domain often requires a lot of experimentation, and iteration. This is why it’s good to make a few initial attempts at testing a design before building an entire Production system to solve a problem like indexing Shakespeare.
Failure Domains

Like problem domains, failure domains just describe the complexity of a system. Except, instead of describing the various problems a system tries to solve, failure domains describe various sub-systems which may fail. Using the Shakespeare example again, if one of your systems is responsible for managing the full text of the works of Shakespeare (a content server), that might be a single failure domain. If another system is responsible for actually searching that content and counting the words (an indexer), that is a separate failure domain. Some failure domains can be within other failure domains. For example, if an indexer fails, the content server may not fail. But if a content server fails, the indexer will probably also fail.

So why do we care about any of this? Well, Problem Domains drive system complexity. Complex systems often have many failure domains. The key to preventing future breakage is to identify, and manage the scope and severity of a failure domain. This may mean redesigning the system in a way that has many smaller failure domains, instead of few large ones. 

As another example It’s better to have a video streaming service slow down instead of failing entirely. This kind of graceful degradation can be attributed to isolated failure domains.

This topic can be a bit complex, but there are several community articles on the idea of identifying and managing failure domains. Consolidating and completely eliminating possible failure domains is the key to preventing future breakage. If anything, managing failure domains should keep the scope of a break as small as possible.

Check out some more info here:

    https://simpleprogrammer.com/understanding-the-problem-domain-is-the-hardest-part-of-programming/

    https://blog.turbonomic.com/blog/on-technology/thinking-like-an-architect-understanding-failure-domains

    https://landing.google.com/sre/sre-book/chapters/effective-troubleshooting/


#More About Making the Best Use of Our Time

Check out the following link for more information:

    https://blog.rescuetime.com/how-to-prioritize/

#More About Making the Best Use of Our Time

Check out the following link for more information:

    https://blog.rescuetime.com/how-to-prioritize/

