git submodule update --init --recursive

# Python Dashboard for Lana PM

A documented example for python dashboards that can be used as a starting point
for any new dashboards. The example shows a multipage app with a rather simple
page-1 and a more complex page-2.

* Page-1 can be seen as an example of how to create simple dashboard page with
  elements being mostly independent of each other.

* Page 2 shows a more complex case where a table can be updated by the user,
  which then calculates the cost and updates a KPI below.

Additionally a graph shows the occurences of the event selected in the table.
For documentation of how to create plots, we refer to the documentation of Plotly
and Dash. For an explanation of how to make api requests to the backend please
see the Pylana documentation and the api specifications of Lana Process Mining.

## Getting started for a local setup without Process Mining front-end

TODO rephrase
### Preparing the local system

Create a new conda environment using:

`conda-shell`
`conda create -n <env-name>`

where _<env-name>_ is the name of the conda environment to be used.

Activate that environment using:

`conda activate <env-name>`

Install required packages:

`conda install -u`

`pip install pylana`
`pip install lana_listener-0.0.1.tar.gz`

Where _pylana_ is available in public repository;
_lana-listener_ component shall be sourced as a ready made package from lanalabs/github.

One may use a _requirements.txt_ to install generic dependencies into the
particular conda environment that is hosted natively on the local system in
order to develop the dashboard. Note that, these installed dependencies will not
be carried over into target system as installed ones!

A requirements file may be used from the mining repository which is also used
for production setup to look up and install dependencies.

TODO
### Setting up configs and running the dashboard locally

It is possible to run the dashboard independent of LANA PM.
Simply fill in the API key and log_id into the `lana_listener` object and start
`index.py`.

TODO where is it uploaded? local/production/cloud?
TODO Call it deployment instead of uploading.
### Uploading your first dashboard

Simply follow the steps in the jupyter-notebook to create a dashboard and link
it to the log. Once you have the `dashboard_id` and it is connected to the
log, you will be able to upload source code either using the notebook, or using
the `upload.sh` script. For a detailed instruction of how to upload also
other types of dashboards, as well as a Bash and Python guide to upload, please
see `UploadTutorial.pdf`.

TODO This is called replacing source code of an existing dashboard.
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
