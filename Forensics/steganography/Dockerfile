FROM ubuntu:latest

WORKDIR /app

COPY amogus.jpg /app
RUN apt-get update && apt-get install -y steghide

EXPOSE 5002
CMD ["bash"]
