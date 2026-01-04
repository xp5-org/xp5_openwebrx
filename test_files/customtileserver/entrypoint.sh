entrypoint.sh

#!/bin/sh
python3 /copyfiles.py
exec /init "$@"
