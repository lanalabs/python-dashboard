develop.sh
emphaise what partial results and where can be accessed

# Python Dashboard for Lana PM

A documented example for python dashboards that can be used as a starting point
for any new dashboards. An example project _dashboards_ shows a multipage app
with a rather simple page-1 and a more complex page-2.

* Page-1 can be seen as an example of how to create simple dashboard page with
  elements being mostly independent of each other.

* Page 2 shows a more complex case where a table can be updated by the user,
  which then calculates the cost and updates a KPI below.

Additionally a graph shows the occurences of the event selected in the table.
For documentation of how to create plots, we refer to the documentation of Plotly
and Dash. For an explanation of how to make api requests to the backend please
see the Pylana documentation and the api specifications of Lana Process Mining.

Additionally, a rather minimalistic dashboard is also provided by the project
_minimalistic\_dashboard_, which is potentially the simplest example that
involves the smallest set of external dependencies.

## Getting started for a local setup without Process Mining front-end

There are two potential ways to choose from for developing any dashboard, in
order to run the desired code:
 - Running the entire system via docker-compose on a local computer. This
   involves to be able to run _Process Mining_ as a whole.
 - Developing the dashboard code independently and uploading the code
   incrementally over and over again until ready to some remotely available
   setup. (not recommended)

### Preparing a (your) local system
 for using Python

Make sure the submodules are pulled and up-to-date on the example project of
your interest, execute in the root of this repository:

`git submodule update --init --recursive`

Create a new conda environment using in one of the example project folder:

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
be carried over onto the target system as installed ones!

When the setup of the local system and the remote system diverges, e.g.
supported python versions, available dependencies, etc; that may result in
failure.

A __requirements.txt_ file may be used, that is defined in the mining repository's
container setup that is actually used for production setup.

### Setting up configs and running the dashboard locally

It is possible to run the dashboard independent of LANA PM.
Simply fill in the API key and log_id into the `lana_listener` object and start
`index.py` in your own python (potentially _conda_) environment.

### Deploying your dashboard

Simply follow the steps in the jupyter-notebook to create a dashboard and link
it to the log. Once you have the `dashboard_id` and it is connected to the
log, you will be able to upload source code either using the notebook, or using
the `upload.sh` script. For a detailed instruction of how to upload also
other types of dashboards, as well as a Bash and Python guide to upload, please
see `UploadTutorial.pdf`.

### Uploading/replacing source-code of an existing Advanced dashboard

First, stop tracking the `upload.sh` file by git on your local machine, so that
you can modify its content without making actual changes to the original version
in the repository, by accident.

`git update-index --assume-unchanged upload.sh`

After assigning value to the `API_KEY`, `DASHBOARD_ID` and `URL` variables
respectively in the `upload.sh` scipt, open a terminal and execute it:

`bash upload.sh`

Refresh the Advanced Dashboard page in LANA PM and the dashboard should appear.

## Add Graphs, Interactions and Pages

The provided _dashboards_ project example follows a basic structure to allow for multiple pages. Each page
has its own URL with navigation enabled by the navigation-bar at the top. The folder
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

Common functionalities should be shared across pages using the
`dashboard-components` git-submodule. Elements that have the same formatting
should be defined as functions and not as copy pasted code. In case API calls or
data needs to be used by any other function, those should also be implemented in
an accessible way. The more function elements and functions are implemented,
the fewer time it will take to build new dashboards. On how to use submodules
please see the Wiki entry here:

https://github.com/lanalabs/python-dashboard/wiki/Working-with-submodules-in-VS-Code
.
