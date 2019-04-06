#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Sam Wu on 2019-04-04

import yaml
import time
import random
from coupling.net.ssh import SSHClient
import paramiko



import logging.config
logger = logging.getLogger(__name__)


class DutBase:

    def __init__(self):
        self._dut_list = self.dut_list()
        self.available_dut_list = list(set(self._dut_list))
        self.undertesting_dut_list = []

    def dut_info(self, dut):
        with open("./Duts/duts.yaml", encoding="utf-8") as fs:
            dut_list = yaml.load(fs, Loader=yaml.FullLoader)
            for _ in dut_list:
                if dut == _["dut_name"]:
                    logger.info(f"the dut is {_}")
                    return _

    def dut_list(self):
        with open("./Duts/duts.yaml", encoding="utf-8") as fs:
            data = yaml.load(fs, Loader=yaml.FullLoader)
            dut_list = []
            for _ in data:
                sshc = SSHClient()
                sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                try:
                    sshc.connect(_["dut_ip"], _["dut_ssh_port"], _["ssh_user"], _["ssh_passwd"], timeout=10)
                    dut_list.append(_["dut_name"])
                except Exception as e:
                    pass
                finally:
                    sshc.close()
            dut_num = len(dut_list)
            logger.info(f"We have {dut_num} to be tested.")
            return dut_list

    def request_dut(self):
        while not self.available_dut_list:
            time.sleep(1)
            logger.info("!!!All dut are busy, waiting for available!!!")
        tmp = list(range(len(self.available_dut_list)))
        dut = self.available_dut_list.pop(random.sample(tmp, 1)[0])
        self.undertesting_dut_list.append(dut)
        return dut

    def release_dut(self, dut):
        self.available_dut_list.append(dut)
        self.undertesting_dut_list.remove(dut)

    def skip_dead_dut(self, dut):
        try:
            self.available_dut_list.remove(dut)
        except ValueError:
            pass
        finally:
            try:
                self.undertesting_dut_list.remove(dut)
            except ValueError:
                pass

