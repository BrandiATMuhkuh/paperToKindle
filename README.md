paperToKindle
=============

This is a python script which used k2pdfopt to convert 2 column pdf papers to a kindle readable format and sends it then to your kindle as email.

# Why
I don't know who came up with this super idea of creating 2 column pdf especially for papers. Really annoying. That is why I made this simple converter script. 

# How to install

* Download this script by clicking this link https://github.com/BrandiATMuhkuh/paperToKindle/archive/master.zip
* Unzip the "paperToKindle-master.zip" file where ever you want
* Download K2pdfopt for your platform from this page http://www.willus.com/k2pdfopt/download/
* Copy the "k2pdfopt" file into the folder "paperToKindle-master" folder
* Rename the file "example.cfg" to "config.cfg"
* Open config.cfg with any text editor
* Replace each variable with the proper smtp data (you can find them in you email client (thunderbird/outlook) or google for smtp server and your email service)
* Make sure Amazon can receive email from your email address
* go to https://www.amazon.de/gp/digital/fiona/manage?ie=UTF8&*Version*=1&*entries*=0#pdocSettings
* Add you email address to the Allowed email addresses
* Copy the kindle email address to your config.cfg and use it for the variable "kindleEmail"
* Now we are done

# How to run

* Open the command line and go to the the folder called "paperToKindle-master"
* python ./paperToKindle.py -p "pdfFileName"

