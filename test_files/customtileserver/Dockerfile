dockerfile
FROM slechev/openwebrxplus-softmbe:latest

# this is for testing owrx+ with patched files from this repo

RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*


COPY entrypoint.sh /entrypoint.sh
COPY syncfiles.py /syncfiles.py
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]