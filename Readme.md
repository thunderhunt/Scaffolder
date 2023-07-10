# Scaffolder

Scaffolder is a project scaffolding tool that helps you generate a predefined folder structure for your projects based on the yaml configuration which holds the project structure.

## Getting Started

These instructions will guide you on how to use the scaffolding tool to set up your project.

### Prerequisites

Before using the scaffolder, make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the project repository:

   ```shell
   git clone https://github.com/Thunderhunt/Scaffolder.git
   ```

2. Change into the project directory:

   ```shell
   cd scaffolder
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

### Usage

To generate the project structure using the provided configuration file, follow these steps:

1. Create a YAML configuration file specifying the desired folder structure. Refer to the `scaffolding.yml` file in this project as an example.

2. Run the following command:

   ```shell
   python scaffold.py -p <path> -n <project-name> -c <config-file>
   ```

   Replace `<path>` with the desired path where the project structure should be generated. If no path is specified, the structure will be created in the current directory.

   Replace `<project-name>` with the desired name for your project.

   Replace `<config-file>` with the path to your YAML configuration file.

3. The project structure will be generated according to the configuration file.

### Folder Structure

The generated project structure will follow the following layout:

```
- .gitignore
- .buf.gen.yaml
- buf.work.yaml
- README.md
- .golangci.yaml
- mockery.yaml
- Dockerfile
- .dockerignore
- tools.go
- Makefile
- api/
  - handlers/
    - routes.go
- cmd/
- docs/
- config/
- deploy/
- internal/
- pkg/
- tests/
- proto/
- local/
- assets/
- mocks/
- .github/
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please submit a pull request or open an issue in the project repository.

## License

This project is licensed under the MIT License
