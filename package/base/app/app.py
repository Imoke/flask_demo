from package.base.nacos import NacosClient
from package.base.apollo import ApolloClient
import re
from datetime import datetime


from flask import Flask, Blueprint

webapp = Flask(__name__)

commonBp = Blueprint('kpi', __name__)

NACOS_SERVER_ADDRESSES = "ofm-nacos-0.discovery-nacos.app.svc.cluster.local:8848"
NACOS_NAMESPACE = "public"
NACOS_SERVICE_NAME = "ofm-py-kpi-service"
NACOS_INSTANCE_IP = "127.0.0.1"
NACOS_INSTANCE_PORT = "5000"


APOLLO_APP_ID = "113"
APOLLO_SERVER_URL = "http://10.192.30.217:38080"

# nacosClient = NacosClient(NACOS_SERVER_ADDRESSES, NACOS_SERVICE_NAME,
#                           NACOS_INSTANCE_IP, NACOS_INSTANCE_PORT, NACOS_NAMESPACE)
apolloClient = ApolloClient(
    app_id=APOLLO_APP_ID, config_server_url=APOLLO_SERVER_URL)

# 暂时不需要start
# apolloClient.start()
