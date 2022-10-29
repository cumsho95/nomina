from threading import Lock, Thread
class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
class Singleton(metaclass=SingletonMeta):
    value: str = None
    def __init__(self, value: str) -> None:
        self.value = value
    def some_business_logic(self):
        ''
def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)
if __name__ == "__main__":
    print("If the same value appears on the printout, singleton was used.\n"
          "But if the values are different, 2 singletons were created.\n"
          "PRINT:\n")
    process1 = Thread(target=test_singleton, args=("A",))
    process2 = Thread(target=test_singleton, args=("B",))
    process1.start()
    process2.start()