# Take initial input
timeout = int(input("Enter timeout value: "))
status = input("Enter server status: ")

server_config = {"timeout": timeout, "status": status}

# --- Read & Inspect ---
print("Status:", server_config["status"])
print("Admin Email:", server_config.get("admin_email", "Not Set"))
print("Total settings:", len(server_config))
print("Keys:", list(server_config.keys()))
print("Values:", list(server_config.values()))

# --- Modify ---
server_config["timeout"] = -server_config["timeout"]
server_config["max_connections"] = int(input("Enter max connections: "))

print("\nAfter modification:", server_config)

# --- Clean Up ---
server_config.pop("timeout", None)

print("After cleanup:", server_config)

# --- Sort ---
print("Sorted Keys:", sorted(server_config.keys()))
