# Python Dashboard for Lana PM

A documented example for python dashboards that can be used as a starting point
for any new dashboards. The example shows a multipage app with a rather simple
page 1 and a more complicated page 2. Page one can be seen as an example of how
to create simple dashboard pages with elements being mostly independent of each
other. Page 2 shows a complicated case where a table can be updated by the user,
which then calculates the cost and updates a KPI below. Additionally a graph
shows the occurences of the event selected in the table. For documentation of
how to create plots, we refer to the documentation of Ploty and Dash. For an
explanation of how to make api requests to the backend please see the Pylana
Documentation and the api specifications of Lana Process Mining.

## Getting started

### Install requirements

Create a new conda environment using:

`conda create env --env name`

Activate that environment using:

`conda activate <env-name>`

Install required packages:

`conda install requirements.txt`
`conda install lana_listener-0.0.1.tar.gz`

### Setting up configs and running the dashboard locally

It is possible to run the dashboard independent of LANA PM.
Simply fill in the API key and log_id into the `lana_listener` object and start
`index.py`.

### Uploading your first dashboard

Simply follow the steps in the jupyter-notebook to create a dashbaord and link
it to the log. Once you have the `dashboard_id` and it is connected to the
log, you will be able to upload source code either using the notebook, or using
the `upload.sh` script. For a detailed instruction of how to upload also
other types of dashboards, as well as a Bash and Python guide to upload, please
see `UploadTutorial.pdf`.

### Uploading (new) source-code

First stop tracking the `upload.sh` file so that you can change the file without
pushing the changes to git by accident.

`git update-index --assume-unchanged upload.sh`

After filling in the api_key, dashboard_id and url, open the terminal and run

`bash upload.sh`

Refresh the Advanced Dashboard page in LANA PM and the dashboard should appear.

## Add Graphs, Interactions and Pages

This repository follows a basic structure to allow for multiple pages. Each page
has its own URL with navigation enabled by the navbar at the top. The folder
structure is as follows:

```
- app.py
- index.py
- apps
   |-- __init__.py
   |-- app1.py
   |-- app2.py
- dashboard-components
   |-- indicator_objects.py
   |-- api_requests.py
```

Common functionality should be shared across pages using the
`dashboard-components` submodule. Elements that have the same formatting should
be defined as functions and not as copy pasted code. If API calls or data can be
used by other functions, they should also be implemented in an accessible way.
The more functions elements and functions are implemented, the fewer time it
will take to build new dashboards. On how to use submodules please see the Wiki
entry here:


https://github.com/lanalabs/python-dashboard/wiki/Working-with-submodules-in-VS-Code
