FROM python:3.6

ADD . /bluepi      
WORKDIR /bluepi    

RUN pip install --upgrade pip           
RUN pip install -r requirements.txt    
RUN apt-get update ##[edited]
RUN apt-get install 'ffmpeg'\
    'libsm6'\ 
    'libxext6'  -y 

EXPOSE 8000  
CMD ["python","main.py"]

