How to start the app (all these commands were tested on windows 10)

commands(all these commands should be executed in the project folder(i personaly have used visual studio code terminal for it)):

1  run command-  pip install virtualenv
2  run command-  virtualenv myenv           //myenv is name given to virtual environment you can use any name of your choice
3  now to activate venv use command-   source ./myenv/Scripts/activate
4  now run command-   export PYTHONPATH=$PWD 
5  now when your virtual environment is activated install dependencies using command-    pip install -r requirements.txt
6  now start the server using command-      python app/main.py

your server should be running now on http://localhost:8000/

as i have used fastapi you can go to http://localhost:8000/docs to interact with routes.



breif summary on routes:

[POST]
/addaudio: in this route you first need to add type of audio and then fill the metadata details of that type,if you want to you 
            can remove other type's metadata fields whose type you didn't entered.

note: use audioType one of these three: song,podcast or audiobook.


audioType can be: song,podcast or audiobook
please enter correctly otherwise error will occur.
[GET]
/{audioType}: this route will give you all the audios stored on database of the type you entered.
/{audioType}/{id}: this route will give you audio with the given id and audioType.

[DELETE]
/{audioType}/{id}:this route will delete the specific audio with _id=id and the audioType.

[PUT
/{audioType}/{id}:this route will update the audio with specific id and audioType provided by user.

    


One more thing: this project is linked to my account of mongodb atlas if you want to connect it to your mongodb atlas account just insert 
your mongodb URI in database.py file (i have left comment above line where you need to insert your mongodb uri).


PS: You can also check my other github projects like ecommerce project in which i have used django REST FRAMEWORK and REACT.

