import nacos
from datetime import datetime
from threading import Timer
import time

import requests

import random


DEFAULT_GROUP = 'DEFAULT_GROUP'
SERVICE_INFO_SPLITER = '@@'


class NacosClient:
    def __init__(self, server_addresses, service_name, instance_ip, instance_port, namespace=None):
        self.server_addresses = server_addresses
        self.service_name = DEFAULT_GROUP + SERVICE_INFO_SPLITER + service_name
        self.namespace = namespace
        self.instance_ip = instance_ip
        self.instance_port = instance_port

        self.connect()

    def connect(self):
        self.client = nacos.NacosClient(
            self.server_addresses, namespace=self.namespace)
        self.client.add_naming_instance(
            self.service_name, self.instance_ip, self.instance_port, None, 1.0, metadata={})
        self.beat()

    def beat(self):
        self.client.send_heartbeat(self.service_name, self.instance_ip,
                                   "5000", None, 1.0, "{}")
        Timer(4, self.beat, ()).start()

    def getNacosClient(self):
        return self.client

    def getOneHealthyInstance(self, serviceName):
        instance = self.client.list_naming_instance(
            serviceName, None, True)

        totalWeight = 0
        for host in instance.get("hosts"):
            totalWeight += host.get("weight")

        pos = random.randint(0, 100) * totalWeight / 100

        for host in instance.get("hosts"):
            pos -= host.get("weight")
            if pos <= 0:
                return host

        raise Exception("Not found healthy service " + serviceName)

    def remoteCall(self, serviceName, url):
        host = self.getOneHealthyInstance(serviceName)
        response = requests.get(
            "http://" + host.get("ip") + ":" + str(host.get("port")) + url)
        return response.text
