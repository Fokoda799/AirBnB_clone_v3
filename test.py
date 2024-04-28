from models import storage
from models.state import State

instance = State(name="Morocco")
storage.new(instance)
storage.save()
all = storage.get(State, '1071ad63-399a-44b6-8ebd-d59d8625afbf')
get_instance = storage.get(State, instance.id)
print(all)

