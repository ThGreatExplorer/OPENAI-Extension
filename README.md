# OPENAI EXTENSION
### Video Demo: https://www.youtube.com/watch?v=8Mdj1AIbnKA&t=4s
### Description:
This project was an attempt to use OPENAI's API tools to build your own version of the incredibly potent and popular chatgpt. I originally developed the idea after taking a look at OPENAI's playground and quickly got started using their starter tutorial.

https://beta.openai.com/playground https://beta.openai.com/docs/quickstart

My project has two parts, first a python component using flask that when ran, opens a localhost server with in templates/index.html. This is meant to simulate potential frontend program that a web development engineer could create using OPENAI's API, a proof of concept.The app.py handles the requests from the user to the API and then updates the html. Interesting features include being able to select from over a dozen openai models to generate prompts from. Each of those models have unique specialties and strengths. For example, text-davinci-03 which is the current model, is much more streamlined for nlp (natural language processing). However, another model like code-cushman-001 is far faster at generating code. The con being that it is far less efficient at processing non-code i.e. processing natural language input and converting that into code. <b>Make sure to have the required packages to run </b>. I recommend setting up a virtual environment.

Part Two is creating a chrome extension on top of the flask server, this way if a user wants to more easily access chatgpt, then can do so by simply clicking an icon on the top of the page. The downside is that the extension is much more limited in its offerings. It only provides three models: text-davinci-03, text-curie-001, text-babbage-001, from most capable but slowest to least capable but fastest. The html page is named popup.html and is a slightly modified version of index.html. The chrome extension must be run in developer mode, meaning that you have to toggle google developer mode on, and click load unpacked and select the folder it is downloaded in to run. <b> In order to run this application, you MUST start the flask server concurrently (an oversight I missed when originally thinking of this idea), this way the background.js makes the correct fetch request to the flask server. Additionally, when running flask, you MAY find flask automatically creating a __ pycache __ file. This file MUST be deleted before the program is ran as it causes a conflict because google chrome reads files starting with __ as reserved.</b> Just delete it and everything will run smoothly.

Both parts require you to set your own OPENAI_API_KEY which can be found by navigating to the links above, creating an account, and clicking create new key. The key will start with 18$ of free credits which ends up being quite a lot. Reset the key in the .env file to your API key, otherwise it create an error when accessing the OPEN AI API.

This has been a long and arduous journey filled with many bugs. But enjoy!

Also, don't try to use the API KEY provided, I've already revoked the key.
