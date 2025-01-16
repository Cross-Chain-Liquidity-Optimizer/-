# Create test_ai_agent.py in the /tests directory
mkdir -p ../tests
cat <<EOL > ../tests/test_ai_agent.py
"""
Unit Tests for AI Agent

This module contains unit tests for the core logic of the AI agent.
"""

import pytest
from src.ai_agent.agent_core import AgentCore

@pytest.fixture
def setup_agent():
    """
    Setup fixture for initializing the AI agent.
    :return: Initialized AgentCore instance.
    """
    memory = {}
    prompt = {"default": "Optimize liquidity"}
    return AgentCore(memory, prompt)

def test_process_input(setup_agent):
    """
    Test the process_input method of the AI agent.
    """
    agent = setup_agent
    market_data = [{"price": 100, "volume": 200}, {"price": 150, "volume": 300}]
    current_allocation = [500, 500]
    parameters = {"risk_tolerance": 0.5}
    
    result = agent.process_input(market_data, current_allocation, parameters)
    
    assert "allocation" in result
    assert "expected_return" in result
    assert len(result["allocation"]) == len(current_allocation)
    assert result["expected_return"] > 0

def test_optimize_allocation(setup_agent):
    """
    Test the private method _optimize_allocation.
    """
    agent = setup_agent
    market_data = [{"price": 100, "volume": 200}]
    current_allocation = [1000]
    parameters = {"risk_tolerance": 0.7}
    
    result = agent._optimize_allocation(market_data, current_allocation, parameters)
    
    assert isinstance(result, list)
    assert len(result) == len(current_allocation)
    assert all(isinstance(val, float) for val in result)

def test_calculate_expected_return(setup_agent):
    """
    Test the private method _calculate_expect
