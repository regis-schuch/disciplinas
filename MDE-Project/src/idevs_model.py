class IntegrationSolution:
    def __init__(self, name, infrastructure, services, keys, processes):
        self.name = name
        self.infrastructure = infrastructure
        self.services = services
        self.keys = keys
        self.processes = processes

class Infrastructure:
    def __init__(self, launcher, secureHardware, compartment, rootOfTrust, sourceCode):
        self.launcher = launcher
        self.secureHardware = secureHardware
        self.compartment = compartment
        self.rootOfTrust = rootOfTrust
        self.sourceCode = sourceCode

class Service:
    def __init__(self, type_, name, attributes):
        self.type = type_
        self.name = name
        self.attributes = attributes

class KeysExchange:
    def __init__(self, programKeys, serviceKeys):
        self.programKeys = programKeys
        self.serviceKeys = serviceKeys

class Process:
    def __init__(self, name, uses, steps):
        self.name = name
        self.uses = uses
        self.steps = steps

class Step:
    def __init__(self, name, actions):
        self.name = name
        self.actions = actions

class Action:
    def __init__(self, type_, **kwargs):
        self.type = type_
        self.params = kwargs
