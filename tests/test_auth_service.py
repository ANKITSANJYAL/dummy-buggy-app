"""
Tests for Authentication Service

These tests verify the multi-tenant token hashing functionality
"""

import pytest
import hashlib
from services.auth_service import _security_hash_id, validate_user_session


def test_security_hash_id_without_org():
    """
    Test that security hash works without org_id (backward compatibility).
    """
    token = "test-token-123"
    result = _security_hash_id(token)
    
    # Should return SHA256 hash (64 characters)
    assert len(result) == 64, f"Expected SHA256 hash length 64, got {len(result)}"
    assert isinstance(result, str)


def test_security_hash_id_with_org_prefix():
    """
    Test that security hash correctly includes org prefix per AD-305.
    
    Expected: Hash should include organization context when org_id provided
    """
    token = "test-token-123"
    org_id = "ORG-ABC"
    
    # Should work with org_id parameter
    result_with_org = _security_hash_id(token, org_id)
    result_without_org = _security_hash_id(token)
    
    # Hashes should be different when org is included
    assert result_with_org != result_without_org, \
        "Hash with org_id should differ from hash without org_id"
    
    # Both should be valid SHA256 hashes
    assert len(result_with_org) == 64
    assert len(result_without_org) == 64


def test_validate_user_session():
    """
    Test user session validation.
    """
    # Valid token
    valid_result = validate_user_session("valid-session-token")
    assert valid_result['authenticated'] is True
    assert 'user_id' in valid_result
    
    # Invalid token
    invalid_result = validate_user_session("invalid-token")
    assert invalid_result['authenticated'] is False


def test_multi_tenant_token_hashing():
    """
    Test multi-tenant token hashing functionality.
    
    This verifies that different organizations get different hashes
    for the same user token (security isolation).
    """
    token = "user-token-456"
    org1 = "ORG-123"
    org2 = "ORG-456"
    
    hash1 = _security_hash_id(token, org1)
    hash2 = _security_hash_id(token, org2)
    hash_no_org = _security_hash_id(token)
    
    # All three should be different
    assert hash1 != hash2, "Different orgs should produce different hashes"
    assert hash1 != hash_no_org, "Org hash should differ from no-org hash"
    assert hash2 != hash_no_org, "Org hash should differ from no-org hash"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
