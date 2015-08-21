# clock

## Installation

```
$ mkvirtualenv clock
$ pip install -r requirements.txt

```

## Usage

When you arrive at work:

    ./clock.py enter

When you leave for lunch:

    ./clock.py lunch

When you come back from lunch:

    ./clock.py back

When you leave for the day:

    ./clock.py leave

To check the current status and how many hours you have left:

    ./clock.py

Example output:


    $ ./clock.py 
    enter: 2015-08-21 13:02:25.004021
    lunch: 2015-08-21 14:20:40.823168
    back:  2015-08-21 14:58:30.823168
    leave: 
    
    worked hours: 4:34:25.297379
    time left: 3:25:34.702621
