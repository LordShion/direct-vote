# direct-vote
A python Django project for a direct vote plateform.

### installation

git clone project

create a python 2.7 virtualenv outside project folder

activate virtualenv

pip install django==1.8


create a local_settings.py file  in the same folder as settings.py
with your database settings
for production prefer a postgresql database service 

in order to make modifications to javascript code and css code and compile after modification

you'll need to install nodeJS 

use npm to install needed packages

in the DirectVote/DirectVote folder
type

npm install

youl need sass

If you're using a distribution of Linux, you'll need to install Ruby first. You can install Ruby through the apt package manager, rbenv, or rvm.
sudo su -c "gem install sass"

to compile everything 
type

gulp       (this operation creates all needed static files if you modify them)






