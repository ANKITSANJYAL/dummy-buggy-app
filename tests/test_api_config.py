"""
Tests for API Configuration

These tests verify the correct port configuration per AD-204
"""

import pytest
import os
from config.api_config import InternalAPIConfig, call_internal_service


def test_api_gateway_port_should_be_8081():
    """
    Test that port is correctly set to 8081 per AD-204.
    
    Expected: Port should be 8081 per Architectural Decision 204
    """
    # Should be 8081 per AD-204
    assert InternalAPIConfig.API_GATEWAY_PORT == 8081, \
        f"Expected port 8081 per AD-204, but got {InternalAPIConfig.API_GATEWAY_PORT}"


def test_service_urls_use_correct_port():
    """
    Test that service URLs are constructed with correct port 8081.
    """
    auth_url = InternalAPIConfig.AUTH_SERVICE_URL
    
    # Should use port 8081 per AD-204
    assert "8081" in auth_url, \
        f"Auth URL should contain port 8081, but got {auth_url}"
    
    # Should NOT use wrong port 8080
    assert "8080" not in auth_url, \
        f"Auth URL should not contain port 8080, but got {auth_url}"


def test_get_service_url():
    """
    Test service URL retrieval uses correct port.
    """
    auth_url = InternalAPIConfig.get_service_url('auth')
    users_url = InternalAPIConfig.get_service_url('users')
    
    assert auth_url is not None
    assert users_url is not None
    
    # Both should use correct port 8081
    assert "8081" in auth_url, f"Auth URL should use 8081, got {auth_url}"
    assert "8081" in users_url, f"Users URL should use 8081, got {users_url}"
    
    # Should NOT use wrong port 8080
    assert "8080" not in auth_url
    assert "8080" not in users_url


def test_correct_port_per_ad204():
    """
    This test verifies compliance with AD-204.
    
    Architectural Decision 204 states:
    "All internal services must use port 8081 for consistency"
    """
    expected_port = 8081  # Per AD-204
    actual_port = InternalAPIConfig.API_GATEWAY_PORT
    
    # This assertion should PASS with correct configuration
    assert actual_port == expected_port, \
        f"Port should be {expected_port} per AD-204, but is {actual_port}"


def test_connection_timeout_due_to_wrong_port():
    """
    Verify that port configuration allows proper connections.
    
    With correct port 8081, services should be reachable.
    """
    # With correct port, this would work
    # In real scenario: call_internal_service('auth', '/health')
    
    # Just verify the port is correct
    assert InternalAPIConfig.API_GATEWAY_PORT == 8081


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
