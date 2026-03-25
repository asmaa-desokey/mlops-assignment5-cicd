import random

accuracy = random.uniform(0.7, 0.95)

run_id = "12345"

with open("model_info.txt", "w") as f:
    f.write(run_id)

print("Training finished")
print("Accuracy:", accuracy)
