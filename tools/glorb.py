def main():
    print("Here is a list of all available tools:\n")

    tools = [
        ("aglorb", "ADB (Android Debug Bridge tools)"),
        ("awglorb", "AWS cloud tools"),
        ("azglorb", "Azure cloud tools"),
        ("doglorb", "Docker tools"),
        ("docoglorb", "Docker Compose tools"),
        ("gcglorb", "Google Cloud tools"),
        ("gglorb", "Git version control tools"),
        ("ghglorb", "GitHub CLI tools"),
        ("glorb", "Tool listing / registry viewer"),
        ("kuglorb", "Kubernetes tools"),
        ("npglorb", "NPM (Node.js package manager) tools"),
    ]

    for name, desc in tools:
        print(f"- {name} - {desc}")

if __name__ == "__main__":
    main()