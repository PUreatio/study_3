# ubuntuイメージをベースに作成する。
FROM ubuntu
# メンテナンス者
MAINTAINER h.shigemoto <h.shigemoto@pureatio.com>
# Pythonインストール
RUN apt-get update && apt-get install -y python2.7 \
&& apt-get install -y python2.7-dbg \
&& apt-get install -y python2.7-dev \
&& apt-get install -y python-pip