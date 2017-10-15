# chess-web

chess-web is the web client for the entire application. It takes cares of displaying the board and updating positions while the battle is occuring.

It relies on flask, including a celery job queuer to start the battle. A communication with a redis instance is required as updating positions relies on a publish–subscribe pattern.
