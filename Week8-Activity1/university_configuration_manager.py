class UniversityConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

# Settings
        cls._instance.name = "Yoobee"
        cls._instance.year = "2026"
        cls._instance.semester = "1st semester"
        return cls._instance

# Create two settings objects
settings1 = UniversityConfig()
settings2 = UniversityConfig()

 
 #  Change settings using settings1
settings1.name = "Auckland University"
settings1.year = "2027"
settings1.semester = "2nd semester"

 # Access using settings2
print(settings2.name)
print(settings2.year)
print(settings2.semester)

 # Check if they are the same object
print(settings1 is settings2)
    