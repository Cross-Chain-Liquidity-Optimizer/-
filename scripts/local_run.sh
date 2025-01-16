# Create local_run.sh in the /scripts directory
cat <<EOL > ../scripts/local_run.sh
#!/bin/bash

# Local Run Script for Cross-Chain Liquidity Optimizer

echo "Starting local environment setup..."

# Step 1: Set environment variables for local testing
export CONFIG_FILE="../config/config.yaml"
export ENVIRONMENT="development"

# Step 2: Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 3: Run the application locally
echo "Starting the application in local mode..."
python src/main.py --config \$CONFIG_FILE --env \$ENVIRONMENT

echo "Local run complete!"
EOL

# Make the script executable
chmod +x ../scripts/local_run.sh
