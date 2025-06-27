#!/usr/bin/env python3
"""
Simple MCP Client for Instagram DM tools
"""

import json
import subprocess
import sys
from typing import Dict, Any

class MCPClient:
    def __init__(self, server_script: str = "src/mcp_server.py"):
        self.server_script = server_script
        self.server_process = None
    
    def start_server(self):
        """Start the MCP server as a subprocess"""
        try:
            self.server_process = subprocess.Popen(
                [sys.executable, self.server_script],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            print("🚀 MCP Server started")
        except Exception as e:
            print(f"❌ Failed to start MCP server: {e}")
    
    def stop_server(self):
        """Stop the MCP server"""
        if self.server_process:
            self.server_process.terminate()
            print("🛑 MCP Server stopped")
    
    def send_message(self, username: str, message: str) -> Dict[str, Any]:
        """Send Instagram DM via MCP server"""
        try:
            # For now, we'll use a simple approach
            # In a real implementation, you'd use the MCP protocol
            print(f"📱 Sending DM to @{username}: {message}")
            
            # This is where you'd make the actual MCP call
            # For now, return success
            return {
                "success": True, 
                "message": "Message sent successfully!",
                "username": username,
                "sent_message": message
            }
            
        except Exception as e:
            return {"success": False, "message": str(e)}
    
    def __enter__(self):
        self.start_server()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_server()

# Simple test function
def test_mcp_client():
    """Test the MCP client"""
    client = MCPClient()
    
    # Test sending a message
    result = client.send_message("test_user", "Hey there! 😊")
    print(f"Test result: {result}")

if __name__ == "__main__":
    test_mcp_client() 