# Save this file in: gateway/Dockerfile

# Use the official lightweight NGINX image as a base
FROM nginx:alpine

# Remove the default nginx configuration file to avoid conflicts
RUN rm /etc/nginx/conf.d/default.conf

# Copy our custom nginx.conf to the container's configuration location
COPY nginx.conf /etc/nginx/conf.d/