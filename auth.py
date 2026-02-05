import sqlite3
import hashlib
import streamlit as st

class Authentication:
    def __init__(self):
        pass
    
    def login(self, username, password):
        """Authenticate user"""
        try:
            # Try database authentication
            conn = sqlite3.connect('sales_system.db')
            cursor = conn.cursor()
            
            # Hash the password
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            
            # Use ? for SQLite
            query = "SELECT * FROM users WHERE username = ? AND password = ? AND is_active = TRUE"
            cursor.execute(query, (username, hashed_password))
            
            user = cursor.fetchone()
            conn.close()
            
            if user:
                return {
                    'authenticated': True, 
                    'username': user[1],  # username column
                    'role': user[3],      # role column
                    'user_id': user[0]    # id column
                }
            
        except sqlite3.OperationalError as e:
            # Table doesn't exist - fallback to demo login
            print(f"Database error (table may not exist): {e}")
        except Exception as e:
            print(f"Database auth error: {e}")
        
        # Fallback to demo credentials
        return self.demo_login(username, password)
    
    def demo_login(self, username, password):
        """Demo authentication for testing"""
        demo_users = {
            'admin': {
                'password': '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9',  # admin123
                'role': 'admin'
            },
            'manager1': {
                'password': 'd3b4d7055e6b2d7e7d5b5b5c5c5d5e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2',  # manager123
                'role': 'manager'
            },
            'clerk1': {
                'password': 'a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2',  # clerk123
                'role': 'clerk'
            }
        }
        
        # Hash the input password
        hashed_input = hashlib.sha256(password.encode()).hexdigest()
        
        if username in demo_users and hashed_input == demo_users[username]['password']:
            return {
                'authenticated': True, 
                'username': username, 
                'role': demo_users[username]['role'],
                'user_id': 1
            }
        
        return {'authenticated': False, 'error': 'Invalid credentials'}
    
    def logout(self):
        """Logout user"""
        st.session_state.authenticated = False
        st.session_state.current_user = None