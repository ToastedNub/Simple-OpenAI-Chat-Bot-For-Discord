# Simple-OpenAI-Chat-Bot-For-Discord
A simple single script bot that uses OpenAI for its responses.


 - THIS IS A SIMPLE PYTHON SCRIPT TO RUN YOUR OWN BOT SIMILAR TO MINE, EXCEPT YOU DONT NEED TO HAVE YOUR OWN DATABANK FOR THIS ONE, THIS ONE IS ALL FROM OPENAI, DATABANKS TAKE YEARS TO CREATE!

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

THIS TELLS YOU HOW TO SET UP YOUR SCRIPT TO RUN YOUR BOT, AS IT IS NOT SET UP TO RUN ANYTHING RIGHT NOW, YOU NEED AN OPENAI API_KEY AND A BOT_TOKEN

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

!GETTING YOUR API_KEY!

Go here to get your API_KEY (THIS IS NOT FREE, BUT IT IS VERY CHEAP)

Link: https://platform.openai.com/playground/chat

Once you create an account or log in, click on your profile at the top right from the link above, then click on "Your profile" this is where you can get your own API key 

(KEEP YOUR API KEY A SECRET, DO NOT SHARE IT WITH ANYBODY)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

!CREATING YOUR BOT AND GETTING YOUR BOT_TOKEN!

Go here, log in with your discord account and create an Application in the Applications tab at the top left.

After the bot is created, inside the bot you need to go to the Bot tab, and click "Reset Token" this is where you can go for all bot account creation for Discord.

Link: https://discord.com/developers/docs/intro

You need to make sure your application in the Bot tab has PRESENCE INTENT, SERVER MEMBERS INTENT, and MESSAGE CONTENT INTENT enabled or the bot will not work properly.

(KEEP YOUR API KEY A SECRET, DO NOT SHARE IT WITH ANYBODY)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

!EDITING THE SCRIPT TO WORK WITH YOUR BOT_TOKEN AND API_KEY!

At the top of the script, where it says API_KEY, replace API_KEY with your actual api key, it should be a big string of random letters and numbers.

At the bottom of the script, where it says BOT_TOKEN, replace BOT_TOKEN with your actual bot token, it should also be a big string of random letters and numbers.

At the top where it says ADD YOUR PERSONALITY HERE, you can add your own personality, the reason there are 3 lines there, are so that you know how to lay out the lines if you decide to add more than 3, it is not a good idea to have too much in each line, it can mess with how the responses get layed out.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

!INSTALLING DEPENDENCIES!

Open the script after you have Python installed, is easy do this and edit the script with Visual Studio Code.

Link: https://code.visualstudio.com

Once you open the script, you need to click Terminal at the top left, then click New Terminal.

Inside the terminal (the new box at the bottom of the screen) enter this command.

Command: pip install discord.py openai python-dotenv

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

!RUNNING YOUR BOT!

Once you have everything above finished, you can now run your bot by opening the "start" file!

If you close the command prompt that it opens, your bot will go offline, unless you host it on a server

THIS IS SET UP TO BE RUN AS A LOCAL HOST (you need to keep the script open to have the bot stay online) BUT YOU CAN SET IT UP TO RUN CONTINOUSLY

Here is the link for a cheap script hosting service!

Link: https://dashboard.render.com
