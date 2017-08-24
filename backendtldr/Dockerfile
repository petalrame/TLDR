#Our base image
FROM python:3-onbuild

WORKDIR /usr/src/app

#Install dependencies
COPY requirements.txt /usr/src/app/ 
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

#Copy the rest of the application's code
COPY . /usr/src/app

#Expose port 800
EXPOSE 8000

#Run the app
CMD ["bash", "run_app.sh"]
