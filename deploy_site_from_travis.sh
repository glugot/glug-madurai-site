#!/bin/bash


SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
SSH_USER="lguruprasad,glug-madurai"
SSH_HOST="web.sourceforge.net"

LOCAL_PATH="./"
REMOTE_PATH="/home/project-web/glug-madurai/htdocs/"

set -e
set -x

echo "Publishing to GitHub pages\n"
make publish github

echo "Publishing to sf.net"
git checkout gh-pages
rsync -avz -e "$SSH_COMMAND" --progress --delete $LOCAL_PATH $SSH_USER@$SSH_HOST:$REMOTE_PATH

