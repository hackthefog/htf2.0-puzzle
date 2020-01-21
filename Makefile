init:
	pip3 install -r requirements.txt

clean:
	pystarter clean

update:
	pip install --upgrade Click Flask gunicorn itsdangerous Jinja2 markupsafe pip pystarter setuptools werkzeug wheel

run: clean
	gunicorn run:app --preload --timeout 10 --max-requests 300