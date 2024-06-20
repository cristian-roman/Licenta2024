class Injector:
    instances = {}
    configuration = None

    @staticmethod
    def register_instance(instance_key, instance):
        Injector.instances[instance_key] = instance
        return Injector

    @staticmethod
    def get_instance(instance_key):
        if Injector.instances.get(instance_key):
            return Injector.instances[instance_key]
