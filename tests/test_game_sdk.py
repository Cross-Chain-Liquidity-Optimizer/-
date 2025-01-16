# Create test_game_sdk.py in the /tests directory
cat <<EOL > ../tests/test_game_sdk.py
"""
Unit Tests for Game SDK Integration

This module contains tests for the Game SDK integration logic.
"""

import pytest
from unittest.mock import patch, MagicMock
from src.game_sdk.sdk_integration import GameSDKIntegration

@pytest.fixture
def setup_game_sdk():
    """
    Setup fixture for initializing the Game SDK Integration module.
    :return: Initialized GameSDKIntegration instance.
    """
    sdk_base_url = "https://api.gamesdk.com"
    api_key = "test_api_key"
    return GameSDKIntegration(sdk_base_url, api_key)

@patch("src.game_sdk.sdk_integration.requests.post")
def test_call_function(mock_post, setup_game_sdk):
    """
    Test the call_function method for a successful custom function call.
    """
    sdk = setup_game_sdk
    mock_post.return_value.status_code = 200
    mock_post.return_value.json = MagicMock(return_value={"result": "success"})

    function_name = "optimize_liquidity"
    arguments = {"param1": "value1"}
    
    response = sdk.call_function(function_name, arguments)
    
    assert response == {"result": "success"}
    mock_post.assert_called_once_with(
        f"{sdk.sdk_base_url}/functions/{function_name}",
        json=arguments,
        headers={"Authorization": f"Bearer {sdk.api_key}"}
    )

@patch("src.game_sdk.sdk_integration.requests.get")
def test_get_function_list(mock_get, setup_game_sdk):
    """
    Test the get_function_list method for retrieving available functions.
    """
    sdk = setup_game_sdk
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = MagicMock(return_value={"functions": ["func1", "func2"]})

    response = sdk.get_function_list()
    
    assert response == {"functions": ["func1", "func2"]}
    mock_get.assert_called_once_with(
        f"{sdk.sdk_base_url}/functions",
        headers={"Authorization": f"Bearer {sdk.api_key}"}
    )

@patch("src.game_sdk.sdk_integration.requests.post")
def test_call_function_error(mock_post, setup_game_sdk):
    """
    Test the call_function method to handle API errors.
    """
    sdk = setup_game_sdk
    mock_post.return_value.status_code = 400

    function_name = "invalid_function"
    arguments = {"param1": "value1"}

    with 
