FROM python:2
MAINTAINER joe@devcorr.com

#copy source files to run the test framework
COPY scripts /usr/local/scripts/

# install default test browser phantomjs
RUN sh /usr/local/scripts/install_phantomjs.sh

# install behave and selenium packages
RUN pip install -U behave && pip install -U selenium && pip install -U page_objects

WORKDIR /usr/local/test/src

CMD ["behave"]