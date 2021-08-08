FROM amazonlinux:latest
RUN yum update -y
RUN yum install python3 -y
RUN yum install nano -y
RUN yum install zip -y
RUN yum install unzip -y


#create working directory
ADD . .
RUN mkdir -p lambda/python

#install dependencies
RUN pip3 install boto3
# -t lambda/python
RUN pip3 install praw 
RUN pip3 install boto3
