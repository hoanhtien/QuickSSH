APP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH="$PYTHONPATH:$APP_DIR"
cd $APP_DIR
python2.7 bin/quick-ssh.py $1 
