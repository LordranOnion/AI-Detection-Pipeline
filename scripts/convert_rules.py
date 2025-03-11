import os
import subprocess

# Define paths
rules_dir = "rules"  # Directory containing Sigma rule files
output_dir = "detections"  # Directory to store the converted rules
backend = "elastic"  # Target backend for conversion

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Convert each Sigma rule
for rule_file in os.listdir(rules_dir):
    if rule_file.endswith(".yml"):
        rule_path = os.path.join(rules_dir, rule_file)
        output_path = os.path.join(output_dir, f"{os.path.splitext(rule_file)[0]}.json")

        cmd = [
            "sigma", "convert",
            "--target", backend,
            "--output", output_path,
            rule_path
        ]

        subprocess.run(cmd, check=True)
        print(f"Converted: {rule_file} -> {output_path}")

print("All Sigma rules converted successfully!")
