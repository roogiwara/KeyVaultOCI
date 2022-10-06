import oci
from flask import Flask, request, Response
import teste2
app = Flask(__name__)

@app.route('/senha/', methods=['GET'])
def simpleapi():
    parametros = request.args.to_dict()
    secret_id = parametros['chave']

    #http://127.0.0.1:5000/senha/?chave=ocid1.vaultsecret.oc1.sa-saopaulo-1.amaaaaaarnobwxyazyt5a3d6twwbmnf4qcsmq6xbce3s7yg5xj3ury623naq
    #http://127.0.0.1:5000/senha/?chave=ocid1.vaultsecret.oc1.sa-saopaulo-1.amaaaaaarnobwxyapmlqfyz52antcf76imj6f5ta52kugsazp36hq3frpqoa
    
    oci_profile = "DEFAULT"

    config = oci.config.from_file(
        "C:\Github\KeyVaultOCI\.oci\config",
        oci_profile)

    secret_client = oci.secrets.SecretsClient(config)
    secret_content = teste2.read_secret_value(secret_client, secret_id)
    resposta = format(secret_content)   
    return Response(response=resposta,status=200,mimetype="application/json")

if __name__ == '__main__':   
    app.run(host='0.0.0.0')