import random
import sys

accuracy = random.uniform(0.7, 0.95)

print("Model accuracy:", accuracy)

if accuracy < 0.85:
    print("Accuracy below threshold")
    sys.exit(1)
else:
    print("Accuracy OK")
