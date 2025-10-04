# Save this file in: frontend/Dockerfile

# Stage 1: Build the React application using Vite
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Serve the built application using NGINX
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
# NGINX listens on port 80 by default
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]