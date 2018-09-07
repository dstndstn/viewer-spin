#! /bin/bash

# unset PYTHONPATH
# export PATH=~/miniconda3b/bin:${PATH}
# source activate viewer-conda-2
# export PYTHONPATH=${PYTHONPATH}:${CONDA_PREFIX}
# export LD_LIBRARY_PATH=${CONDA_PREFIX}/lib

export PYTHONPATH=${PYTHONPATH}:.

python -c "import sys; print(sys.path)"

python -c "from astrometry.util.util import Tan"

#['', '/usr/local/lib/python37.zip', '/usr/local/lib/python3.7', '/usr/local/lib/python3.7/lib-dynload', '/usr/local/lib/python3.7/site-packages', '/app/src/tractor', '/app/src/legacypipe/build/lib', '/app/viewer/src/astrometry']

uwsgi -s :5000 --wsgi-file wsgi.py --touch-reload wsgi.py --processes 8

#--reload-on-rss 768
#--logto /tmp/uwsgi.log -d /tmp/uwsgi2.log


