FROM python:3

ADD python_exercise.py /

CMD [ "python", "python_exercise.py" ,"--list","111233 112233 121133 111131 223341"]