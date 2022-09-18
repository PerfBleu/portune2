import configparser
import os

def getAllPackages():
    config=configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "config.ini"))
    pkgstxt = config.get('BASE','packages')
    return(pkgstxt.split(',')[0:-1])

allPkgs = getAllPackages()
config=configparser.RawConfigParser()

def getEnabledPackage(gid) -> list[str]:
    #config=configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "config.ini"))
    enabledtxt = config.get(str(gid),'enabled')
    return(enabledtxt.split(',')[0:-1])

# def getDisabledPackage(gid):
#     config=configparser.ConfigParser()
#     config.read(os.path.join(os.path.dirname(__file__), "config.ini"))
#     disabledtxt = config.get(str(gid),'disabled')
#     return(disabledtxt.split(',')[0:-1])

def checkIfGroupExists(gid) -> bool:
    #config=configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "config.ini"))
    if config.has_section(str(gid)):
        return(True)
    else:
        return(False)

def addGroupSection(gid):
    #config=configparser.RawConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "config.ini"))
    config.add_section(str(gid))
    config.set(str(gid),'enabled','pcr,')
    config.write(open(os.path.join(os.path.dirname(__file__), "config.ini"), "w"))