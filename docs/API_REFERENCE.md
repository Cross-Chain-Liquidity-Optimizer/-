# Create API_REFERENCE.md in the /docs directory
cat <<EOL > API_REFERENCE.md
# API Reference

This document provides a detailed description of the APIs used in the Cross-Chain Liquidity Optimizer project.

## AI Agent APIs
### Endpoint: `/ai_agent/decision`
- **Method**: POST
- **Description**: Processes input data and returns the optimal liquidity allocation decision.
- **Request Body**:
  ```json
  {
    "input_data": {
      "market_data": [...],
      "current_allocation": [...],
      "parameters": { ... }
    }
  }
