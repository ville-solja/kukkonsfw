FROM python
ADD kukkonsfw.py /
ADD requirements.txt /
RUN pip install -r requirements.txt
CMD ["python", "-u", "./kukkonsfw.py"]