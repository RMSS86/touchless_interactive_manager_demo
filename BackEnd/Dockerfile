# # Stage 1: Build Stage
# FROM node:18 AS builder

# WORKDIR /app

# # Copy package.json and package-lock.json first to leverage Docker cache
# COPY package.json package-lock.json ./

# # Install all dependencies, including dev dependencies
# RUN npm install

# # Copy the rest of the application source code
# COPY . .

# # If you have a build step (e.g., for a frontend framework like React, Vue, Angular)
# # RUN npm run build

# # Stage 2: Production Image
# FROM node:18-alpine

# WORKDIR /app

# # Copy only the necessary files from the builder stage
# # This includes node_modules (production dependencies) and the application code
# COPY --from=builder /app/node_modules ./node_modules
# COPY --from=builder /app/package.json ./package.json
# COPY --from=builder /app/index.js ./index.js
# # If you had a build step, copy the build output instead
# # COPY --from=builder /app/dist ./dist

# # Install only production dependencies (if not copied from builder or if some are missing)
# # RUN npm install --only=production

# EXPOSE 80

# CMD ["npm", "start"]



FROM node:18-alpine

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 80

CMD ["npm", "start"]