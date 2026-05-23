class OutOfResourcesError(Exception):
    pass

def process_task(resource_a, resource_b):
    if resource_a == 0 or resource_b == 0:
        raise OutOfResourcesError("Missing required resources")
    print("Task is complete...")

try:
    process_task(0, 1)
except OutOfResourcesError as e:
    print(e)
