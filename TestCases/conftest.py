#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Sam Wu on 2019-04-04

import pytest


from Common.Dut import DutBase
from coupling.net.ssh import SSHClient
import paramiko

import logging.config
logger = logging.getLogger(__name__)

DUTBASE = DutBase()
RELEASE_DIR = "/opt/release"




@pytest.fixture(scope="module")
def dut_obj():
    dut = DUTBASE.request_dut()
    return dut

@pytest.fixture(scope="module")
def dut_info(dut_obj):
    info = DUTBASE.dut_info(dut_obj)
    return info


@pytest.fixture(scope="module")
def release_dir():
    return RELEASE_DIR


@pytest.fixture(scope="module")
def connect_dut(dut_obj, dut_info):
    ip = dut_info["dut_ip"]
    port = dut_info["dut_ssh_port"]
    user = dut_info["ssh_user"]
    pw = dut_info["ssh_passwd"]
    sshc = SSHClient()
    sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        sshc.connect(ip, port, user, pw)
        yield sshc
        sshc.close()
        DUTBASE.release_dut(dut_obj)
    except Exception as e:
        DUTBASE.skip_dead_dut(dut_obj)


@pytest.fixture(scope="module")
def dist_release_pkg(connect_dut, release_dir):
    sftp = connect_dut.open_sftp()
    if sftp.exists(release_dir):
        sftp.rmtree(release_dir)
    sftp.putdir(release_dir, release_dir, None)































