# show version python
FROM python:3.12
# show what and where we need to save
COPY . /code
#    ^what ^where
#show our workspace (where is storage all files for start)
WORKDIR /code
# show what we should do before start project(what do start)
RUN pip install -r requirements.txt
# command for docker
CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0"]


