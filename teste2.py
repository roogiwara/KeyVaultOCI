import oci
import base64
import sys

# Documentation :

# Usage : python secret_examples.py secret_id OCI_PROFILE
# OCI_PROFILE is the name of profile that you want to use from OCI config file.


def read_secret_value(secret_client, secret_id):
    print("Reading vaule of secret_id {}.".format(secret_id))

    response = secret_client.get_secret_bundle(secret_id)

    base64_Secret_content = response.data.secret_bundle_content.content
    base64_secret_bytes = base64_Secret_content.encode('ascii')
    base64_message_bytes = base64.b64decode(base64_secret_bytes)
    secret_content = base64_message_bytes.decode('ascii')

    return secret_content


if len(sys.argv) != 3:
    raise RuntimeError(
        'This example expects an ocid for the secret to read.')

secret_id = sys.argv[1]
oci_profile = sys.argv[2]

config = config = oci.config.from_file(
    "~/.oci/config",
    oci_profile)

secret_client = oci.secrets.SecretsClient(config)
secret_content = read_secret_value(secret_client, secret_id)
print("Decoded content of the secret is: {}.".format(secret_content))