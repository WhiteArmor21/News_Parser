FROM python:3.8.3

RUN mkdir /News_Parser

WORKDIR /News_Parser

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERRED=1

# install dependencies
COPY requirements.txt /News_Parser
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /News_Parser

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/News_Parser/entrypoint.sh"]