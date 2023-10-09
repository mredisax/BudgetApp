# Use the official Python image as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY ./backend/requirements.txt .

# Install app dependencies
RUN pip install -r requirements.txt

# Copy the rest of the Django project code to the container
COPY ./backend .

# Expose port 8000 for the Django application
EXPOSE 8000

# Start the Django application when the container runs
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

