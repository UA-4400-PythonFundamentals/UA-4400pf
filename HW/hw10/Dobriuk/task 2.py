class Human:
    species = "homosapiens"

    def __init__(self, name: str):
        self.name = name
    
    def welcome(self) -> None:
        print(f"Hello, {self.name}!")

    @classmethod
    def species_info(cls) -> str:
        return f"Species {cls.species}"

    @staticmethod
    def random_message() -> str:
        return "Have a great day!"