#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Sam Wu on 2019-04-06
import pytest
import allure


class TestInstallation:

    # INSTALLATION
    @allure.feature("RPM INSTALLATION")
    @allure.story("install rpm package")
    @pytest.mark.usefixtures("dist_release_pkg")
    def test_installation(self, connect_dut, release_dir):
        with allure.step("ssh connection"):
            assert connect_dut is not None
        with allure.step("install rpm package"):
            connect_dut.run(f"chmod a+x {release_dir}/helloworld*.rpm")
            resp = connect_dut.run(f"rpm -ivh {release_dir}/helloworld*.rpm").communicate()[0]
            assert "#" in resp
        with allure.step("check installation"):
            resp = connect_dut.run(f"helloworld").communicate()[0]
            assert "HELLO WORLD!" in resp
        with allure.step("uninstall rpm package"):
            resp1 = connect_dut.run("rpm -e helloworld").communicate()[0]
            print(resp1)
            resp = connect_dut.run(f"rpm -qa |grep helloworld").communicate()[0]
            assert "" in resp









