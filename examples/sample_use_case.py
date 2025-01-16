# Create sample_use_case.py in the /examples directory
cat <<EOL > ../examples/sample_use_case.py
"""
Sample Use Case for Cross-Chain Liquidity Optimizer

This script demonstrates a basic workflow for optimizing liquidity allocation across chains.
"""

from src.ai_agent.agent_core import AgentCore
from src.blockchain.ethereum import Ethereum
from src.game_sdk.sdk_integration import GameSDKIntegration

def main():
    # Initialize components
    memory = {}
    prompt = {"default": "Optimize liquidity allocation"}
    ai_agent = AgentCore(memory, prompt)
    
    ethereum = Ethereum("https://mainnet.infura.io/v3/example_project_id")
    game_sdk = GameSDKIntegration("https://api.examplegamesdk.com", "example_api_key")
    
    # Example market data and allocations
    market_data = [
        {"chain": "Ethereum", "price": 1200, "volume": 5000},
        {"chain": "BSC", "price": 350, "volume": 3000},
        {"chain": "Polygon", "price": 200, "volume": 2000},
    ]
    current_allocation = [5000, 3000, 2000]
    parameters = {"risk_tolerance": 0.5}
    
    # Process input with AI agent
    result = ai_agent.process_input(market_data, current_allocation, parameters)
    print("Optimized Allocation:", result["allocation"])
    print("Expected Return:", result["expected_return"])
    
    # Simulate a liquidity transfer on Ethereum
    if ethereum.connect():
        sender = "0xSenderAddress"
        private_key = "YourPrivateKey"
        recipient = "0xRecipientAddress"
        amount = 1000
        token_address = "0xTokenAddress"
        
        tx_hash = ethereum.transfer_liquidity(sender, private_key, recipient, amount, token_address)
        print("Transaction Hash:", tx_hash)
    else:
        print("Failed to connect to Ethereum network.")
    
    # Call a custom function via Game SDK
    sdk_response = game_sdk.call_function("optimize_liquidity", {"allocation": result["allocation"]})
    print("Game SDK Response:", sdk_response)

if __name__ == "__main__":
    main()
EOL
