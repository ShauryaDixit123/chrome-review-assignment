Problem statement - There are times when a user 
writes Good, Nice App or any other positive text, 
in the review and gives 1-star rating. 
Your goal is to identify the reviews where the semantics of review text does not match rating. 

Solution :

Virtual  env was created for the project ie. assignment_jds

In main.py file I wrote the code to find semantics of the uploaded file, it was used for 
local machine and the libraries used were pandas to read csv data and for dataframe manupulation
nltk for finding sementics of the text, removing stop words and tokenising it.

In temp.py file functions were created out of process used of main.py and more simplificed 
and compact. We use these functions to be called when necessory in app.py file that is  
out flask app python file. 

In later stages, in app.py ie. flask app file, various imports were performed from flask module
of necessory modules. These modules include : Flask, render_template, 
request, redirect, url_for, abort, jsonify,from werkzeug.utils , secure_filename was imported.
Going forward in process, basic pages were created in html,bootstrap and css. These pages 
were later called in render_template function. Basic pages includes index.html, base.html,
login.html,program.html. Base.html worked as a layout for the other html pages and was called.

Functions created in temp.py were called when data was uploaded in program.html to process the data through 
the functions and create output.

Later, output was returned in form of json, the places where the sementics matched were
labeled as "matched" and were it wasn't was named as "not_matched" in the output.