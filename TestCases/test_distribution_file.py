#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Sam Wu on 2019-04-05

import pytest
import allure


class TestDistribution:

    # DIST FILE
    @allure.feature("DIST FILE TO DUT")
    @allure.story("distribution file to dut test")
    @pytest.mark.usefixtures("connect_dut")
    def test_dist_pkg(self, connect_dut, release_dir):
        with allure.step("ssh connection"):
            assert connect_dut is not None
        with allure.step("open sftp"):
            sftp = connect_dut.open_sftp()
        with allure.step("remove pre-release"):
            if sftp.exists(release_dir):
                sftp.rmtree(release_dir)
            else:
                pass
        with allure.step("copy the release folder to dut"):
            sftp.putdir(release_dir, release_dir, None)
