FROM postgres:13.2

# Set the working directory
WORKDIR /app

# Expose the port
EXPOSE 8090

# Run the application
CMD ["postgres"] 