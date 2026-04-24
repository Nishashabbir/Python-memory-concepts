1. Plugin System (Real-world: apps, games, tools)

Imagine you’re building an app where new features (plugins) can be added dynamically.

✅ Idea:

Classes register themselves automatically.

plugins = []

def register(cls):
    plugins.append(cls)
    return cls

@register
class LoginPlugin:
    def run(self):
        print("Login system")

@register
class PaymentPlugin:
    def run(self):
        print("Payment system")

# Run all plugins
for plugin in plugins:
    plugin().run()

👉 Why this works:

Classes are objects → you pass them into register
You store them → and use them later

💡 This is how many frameworks handle extensions.

🏭 2. Dynamic Object Factory (Real-world: APIs, file handlers)

Instead of messy if-else, let classes handle creation.

class JSONParser:
    def parse(self):
        print("Parsing JSON")

class XMLParser:
    def parse(self):
        print("Parsing XML")

def get_parser(format_type):
    parsers = {
        "json": JSONParser,
        "xml": XMLParser
    }
    return parsers.get(format_type)

parser_class = get_parser("json")
parser = parser_class()
parser.parse()

👉 Clean, scalable, and flexible.

🎮 3. Game Character System

Different character types, same interface.

class Warrior:
    def attack(self):
        print("Sword attack")

class Mage:
    def attack(self):
        print("Magic attack")

def battle(character_class):
    character = character_class()
    character.attack()

battle(Warrior)
battle(Mage)

👉 You’re passing behavior (class), not just data.

🧪 4. Auto Method Injection (Power move)

Modify a class dynamically.

def add_greet(cls):
    def greet(self):
        print(f"Hello from {cls.__name__}")
    
    cls.greet = greet
    return cls

@add_greet
class User:
    pass

u = User()
u.greet()

👉 You just edited a class from outside.

This is how decorators for classes work internally.

📦 5. Simple ORM-like Behavior (like Django models)
class Model:
    def save(self):
        print(f"Saving {self.__class__.__name__}")

class User(Model):
    pass

class Product(Model):
    pass

objects = [User(), Product()]

for obj in objects:
    obj.save()

👉 Real frameworks rely heavily on classes being objects.