# ベースイメージ
FROM python:3.11-slim

# ENV PYTHONUNBUFFERED=1
# ENV PYTHONDONTWRITEBYTECODE=1
# 作業ディレクトリ
WORKDIR /app

# 依存関係をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# コンテナ内DB用ディレクトリ（開発用）
# RUN mkdir -p /app/db && chmod 777 /app/db

# アプリケーションをコピー
COPY . .

# PYTHONPATH を指定して sql_db を認識させる
ENV PYTHONPATH=/app

# デフォルトは bash
CMD ["bash"]
