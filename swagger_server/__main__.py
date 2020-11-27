#!/usr/bin/env python3
import os

import connexion

from swagger_server import encoder

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Account Management API'}, pythonic_params=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(threaded=True, port=port)
