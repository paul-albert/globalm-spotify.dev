# globalm-spotify.dev

## Prepare steps:

_(environment: Linux / Python 3.4+ / Flask 0.12.1)_

### Virtual host

* Ensure that you have `globalm-spotify.dev` value in your `/etc/hosts`
(Of course, you can use some other value for host)

### Back-end's part (Python/Flask)

* `cd /path/to/globalm-spotify.dev`

* Check version of Python:

`python3 -V` _(outputs like as Python 3.4.2)_

* Check version of Python:

`virtualenv --version` _(outputs like as 15.1.0)_

* Create new virtual environment:

`virtualenv -p python3 env`

* Activate the created virtual environment:

`source env/bin/activate`

* Check again version of Python:

`python -V` _(outputs like as Python 3.4.2)_

* Install all dependencies:

`pip install -r requirements.txt`

* Check and edit [configuration file](app/config.py) if needing

* Run the server:

`python app/main.py` (here you can use "http://127.0.0.1:8421/"; CTRL+C - for break the server)

* `deactivate` _(optional step, for virtual environment's turn off only)_

## Running:

* Open in browser link "http://globalm-spotify.dev:8421/"

* Select necessary filter and enter search query

* Click to search icon (in right side from search query field)
