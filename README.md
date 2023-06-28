- First is to install the framework with 
 "pip3 install flask"


 when installing template:

 mkdir static

 brew install wget

 wget https://github.com/StartBootstrap/startbootstrap-clean-blog/archive/refs/tags/v5.0.10.zip

 {{ used_for_expression }}
 {% Used_for_statements %} this is called Logic control

 ------- Readin from a JSON file

 I created a json file and then bound it to my run.py file, specifically the about page with the code:
     data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)

and then I added company=data to the render_template command below.
Then in the about.html I added the following line:
   {{ company[1]["name"] }}
Telling what part of the object in the json file that I would like to have displayed in the about page

---
To secure data
---

- touch .gitignore
- touch env.py (this is where we hide sensitive data)


- npm install -g heroku (the -g means it is installed globally)

after it is insntalled

- heroku login -i

when asked for password I need to enter the api key generated on the Heroku webpage.

Heroku commands:

heroku apps (to see the apps available)

heroku apps: rename new_name_of_app --app current_name_of_app
