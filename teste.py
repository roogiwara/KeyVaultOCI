import oci
import sys
from datetime import datetime
from datetime import timedelta

# Set up config
config = oci.config.from_file("C:\Github\KeyVaultOCI\.oci\config", "DEFAULT")

# Create a service client
identity = oci.identity.IdentityClient(config)

# Get the current user
user = identity.get_user(config["user"]).data
print(user.name)
print(user.id)