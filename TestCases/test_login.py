#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Sam Wu on 2019-04-04

import pytest
import allure


class TestLogin:

    # SSH Login
    @allure.feature("SSH LOGIN")
    @allure.story("LOGIN SUCCESSFULLY")
    @pytest.mark.usefixtures("connect_dut")
    def test_login_success(self, connect_dut):
        with allure.step("ssh connection"):
            assert connect_dut is not None

    # SSH ifconfig
    @allure.feature("SSH IFCONFIG")
    @allure.story("execute 'ifconfig' on remote machine")
    @pytest.mark.usefixtures("connect_dut")
    def test_ifconfig(self, connect_dut):
        with allure.step("ifconfig"):
            assert connect_dut.run("ifconfig").communicate()[0] is not None




