import logging
import pytest
import psutil
import platform
import pytest_html

@pytest.fixture
def setup():
    logger = logging.getLogger()
    return logger
def sys_os():
    p = platform.system()               #using paltform.system to know the os of system
    return p

def test_os(setup):
    os_type = sys_os()                 #calling the sys_os function to check the system is windows are not
    setup.info("testing os type ")
    if os_type == "Windows":
        res = True
    else:
        res = False
    assert res == True
    setup.info("testing os completed")


def memory():
    me = psutil.virtual_memory()
    mem = me.total/(1024*1024*1024)     #converting total bits to GB
    return mem

def test_memory(setup):
    total_mem = memory()
    setup.info("testing memory")
    if total_mem > 4:
        res = True
    else:
        res = False
    assert res == True
    setup.info("testing memory completed")


def dsk_usage():
    du = psutil.disk_usage("C:/").total
    return du/(1024*1024*1024)


def test_disk(setup):
    dsk = dsk_usage()
    setup.info("testing the disk usage")
    if dsk > 200:
        res = True
    else :
        res = False
    assert res == True
    setup.info("testing diskusage completed")

def cpu_use():
    return psutil.cpu_percent(2)

def test_cpupercent(setup):
    cp = cpu_use()
    setup.info("testing cpu percentage")
    if cp > 15:
        res = True
    else:
        res = False
    assert res == True
    setup.info("cpu usage testing completed")

def pytest_html_report_title(report):
    report.title = "question1 report"