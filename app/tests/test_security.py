from app.core.security import hash_password, verify_password, create_access_token, decode_access_token

def test_hash_password():
    password = "mysecretpassword"
    hashed_password = hash_password(password)
    assert hashed_password != password  # Ensure the password is hashed
    assert verify_password(password, hashed_password)  # Verify the password against the hash


def test_verify_password():
    password = "mysecretpassword"
    hashed_password = hash_password(password)
    assert verify_password(password, hashed_password)  # Verify the password against the hash
    assert not verify_password("wrongpassword", hashed_password)  # Ensure wrong password fails verification

def test_create_access_token():
    user_id = 1
    token = create_access_token(user_id)
    assert token is not None



def test_hash_password():
    password = "mysecretpassword"
    hashed_password = hash_password(password)
    assert hashed_password != password
    # Check that it looks like a valid hash (e.g., bcrypt/argon2 hashes are usually long strings)
    assert len(hashed_password) > 20 




def test_create_access_token():
    user_id = 1
    token = create_access_token(user_id)
    assert isinstance(token, str)
    assert len(token.split(".")) == 3  




def test_decode_expired_or_invalid_token():
    with pytest.raises(Exception):  
     decode_access_token("invalid.token.structure")
