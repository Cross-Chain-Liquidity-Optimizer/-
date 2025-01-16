# Create deploy.sh in the /scripts directory
mkdir -p ../scripts
cat <<EOL > ../scripts/deploy.sh
#!/bin/bash

# Deployment Script for Cross-Chain Liquidity Optimizer

echo "Starting deployment..."

# Step 1: Set environment variables
export CONFIG_FILE="../config/config.yaml"
export ENVIRONMENT="production"

# Step 2: Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 3: Run database migrations (if applicable)
echo "Running database migrations..."
# Add your database migration commands here, e.g., alembic upgrade head

# Step 4: Start the application
echo "Starting the application..."
python src/main.py --config \$CONFIG_FILE --env \$ENVIRONMENT

echo "Deployment complete!"
EOL

# Make the script executable
chmod +x ../scripts/deploy.sh
