#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Sam Wu on 2019-04-04

import pytest
import time
from Common.conf_dir import htmlreports_dir
import os


import logging.config
logger = logging.getLogger(__name__)


def run_test():
    logger.info(f"#####DUT:start testing####")
    cur_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_data = htmlreports_dir + f"/{cur_time}"
    report = report_data + "/final_report"
    pytest.main(["./TestCases",
                 "-s", "-q",
                 f"--alluredir={report_data}"])
    os.system(f"allure generate {report_data} -o {report}")


if __name__ == '__main__':
    run_test()
