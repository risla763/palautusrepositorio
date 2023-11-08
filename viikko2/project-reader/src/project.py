class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license,authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        authors_str = "\n".join([f"-{i}" for i in self.authors])
        dependencies_list = "\n".join([f"-{i}" for i in self.dependencies])
        development_list = "\n".join([f"-{i}" for i in self.dev_dependencies])
        return (
            f"\nName: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicence: {self.license}"
            f"\n"
            f"\nAuthors:" 
            f"\n{authors_str}"
            f"\n"
            f"\nDependencies:"
            f"\n{dependencies_list}"
            f"\n"
            f"\nDevelopment dependencies:"
            f"\n{development_list}"
        )
