#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Sam Wu on 2019-04-06

import pytest
import allure
import sys


class TestFoo:

    # FUNCTION FOR SKIPED
    @allure.feature("FOO FUNCTIONS FOR SKIP")
    @allure.story("function for demo only")
    @pytest.mark.skipif(sys.version_info > (3, 6), reason="requires python3.6 or higher")
    def test_python_version(self):
        assert 1 == 1

    # FUNCTION FOR PASSED
    @allure.feature("FOO FUNCTIONS FOR PASSED")
    @allure.story("function for demo only")
    def test_equal(self):
        assert 1 == 1

    # FUNCTION FOR FAILED
    @allure.feature("FOO UNCTIONS FOR FAILURE")
    @allure.story("function for demo only")
    def test_situation(self):
        assert 1 == 2
