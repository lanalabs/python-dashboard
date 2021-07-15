# Python Dashboard for Lana PM
A documented example for python dashboards that can be used as a starting point for any new dashboards.

## Getting started
### Install requirements
Create a new conda environment using:  
`conda create env --env name`

Activate that environment using:  
`conda activate <env-name>`

Install required packages:  
`conda install requirements.txt`  
`conda install lana_listener-0.0.1.tar.gz`

### Setting up config.yml and running the dashboard locally
Depending on if you upload the dashboard to a local instance or the cloud version, fill in the fields for `config.yml`. 
Is is also possible to run the dashboard independend of LANA PM.  
Simply fill in the API key and log_id into the `lana_listener` object and start `index.py`.

### Uploading your first dashboard
Simply follow the steps in the jupyter-notebook to create a dashbaord and link it to the log. Once you have the ```dashboard_id``` and it is connected to the log, you will be able to upload source code either using the notebook, or using the ```upload.sh``` script.

### Uploading (new) source-code
First stop tracking the ```upload.sh``` file so that you can change the file without pushing the changes to git by accident.  
```git update-index --assume-unchanged upload.sh```  
After filling in the api_key, dashboard_id and url, open the terminal and run  
```bash upload.sh```  
Refresh the Advanced Dashboard page in LANA PM and the dashboard should appear.

## Add Graphs, Interactions and Pages
This repository follows a basic structure to allow for multiple pages. Each page has its own URL with navigation enabled by the navbar at the top. The folder structure is as follows:

```
- app.py
- index.py
- apps
   |-- __init__.py
   |-- app1.py
   |-- app2.py
- graph_objects.py
```
Common functionality should be shared across pages. Elements that have the same formatting should be defined as functions and not as copy pasted code. If API calls or data can be used by other functions, they should also be implemented in an accessible way. The more functions elements and functions are implemented, the fewer time it will take to build new dashboards. An example of this can be seen in `graph_objects.py`




