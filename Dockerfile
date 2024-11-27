# Use Nginx as the base image
FROM nginx:alpine

# Set the working directory to Nginx's default web root
WORKDIR /usr/share/nginx/html

# Copy all static files to the container's web root
COPY . .

# Expose port 80 to allow access to the web server
EXPOSE 80

# Start the Nginx server
CMD ["nginx", "-g", "daemon off;"]

# ---------------- This is the content of my Dockerfile ---------------------------------------
#----------------------------------------------------------------------------------------------