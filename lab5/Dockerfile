FROM debian
RUN apt-get update && apt-get install -y python3
COPY test_file.txt /data/test_file.txt
COPY md5_single.py /data/md5_single.py
COPY md5_multiple.py /data/md5_multiple.py
WORKDIR /data

CMD python3 md5_multiple.py .
