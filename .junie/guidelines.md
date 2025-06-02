# Kafka Mirror Kit Development Guidelines

This document provides essential information for developers working on the Kafka Mirror Kit project.

## Build/Configuration Instructions

### Environment Setup

1. **Dependencies**:
    - Python 3.8+ is required
    - Docker and Docker Compose are required for running Kafka clusters
   - Install the package in development mode with: `pip install -e .`
   - This enables an "editable install" where changes to the source code are immediately reflected without reinstalling

2. **Project Structure**:
    - `src/`: Contains the source code
        - `src/core/`: Contains the core module that exposes Python API to execute operations
        - `src/cli/`: Contains the command line interface for core
    - `tests/`: Contains unit tests
        - `tests/core/`: Contains tests for the core module
        - `tests/cli/`: Contains tests for the CLI module
    - `.junie/`: Contains development guidelines

3. **Development Environment**:
    - Use a virtual environment:
      ```bash
      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate
      ```

### Configuration

1. **Kafka Cluster Configuration**:
    - Configurations for Kafka clusters should be defined in a YAML or JSON format
    - Default configurations should be stored in a `config/` directory (to be created)
    - Custom configurations can be passed to the `KafkaCluster` class during initialization

2. **MirrorMaker 2 Configuration**:
    - MirrorMaker 2 configurations should follow the standard Kafka Connect format
    - Connector configurations should be generated dynamically based on the source and target clusters

## Testing Information

### Running Tests

1. **Unit Tests**:
    - Run all tests: `python -m unittest discover tests`
    - Run a specific test file: `python -m unittest tests/test_file.py`
    - Run a specific test case: `python -m unittest tests.test_file.TestClass.test_method`

2. **Integration Tests**:
    - Integration tests that require Docker should be marked with appropriate decorators
    - Run integration tests: `python -m unittest discover tests/integration`

### Adding New Tests

1. **Test Structure**:
    - Place unit tests in the `tests/` directory
    - Name test files with the prefix `test_`
    - Use the `unittest` framework for writing tests
    - Follow the pattern in existing tests (e.g., `test_kafka_mirror.py`)

2. **Test Example**:
   ```python
   import unittest
   from unittest.mock import patch
   from kafka_mirror_kit.core.your_module import YourClass

   class TestYourClass(unittest.TestCase):
       def setUp(self):
           self.instance = YourClass()

       def test_your_method(self):
           result = self.instance.your_method()
           self.assertEqual(result, expected_value)

       @patch('kafka_mirror_kit.core.module_to_mock')
       def test_with_mock(self, mock_obj):
           mock_obj.return_value = 'mocked_value'
           result = self.instance.method_using_mock()
           self.assertEqual(result, 'mocked_value')
   ```

3. **Mocking External Services**:
    - Use `unittest.mock` for mocking external services like Kafka
    - For Docker-based tests, consider using test containers or Docker Compose files specific for testing

## Additional Development Information

### Coding Standards

1. **Type Hints**:
    - Always use type hints for function parameters and return values
    - Example:
      ```python
      def function_name(param1: str, param2: int) -> bool:
          return True
      ```

2. **Documentation**:
    - Use docstrings for all classes, methods, and functions
    - Follow Google style docstrings format
    - Example:
      ```python
      def function_name(param1, param2):
          """
          Short description of the function.

          Args:
              param1: Description of param1
              param2: Description of param2

          Returns:
              Description of return value

          Raises:
              ExceptionType: When and why this exception is raised
          """
      ```

3. **Code Organization**:
    - Follow the single responsibility principle
    - Keep classes and functions focused on a single task
    - Use meaningful names for variables, functions, and classes

### Best Practices

1. **Error Handling**:
    - Use specific exceptions rather than generic ones
    - Handle exceptions at the appropriate level
    - Log exceptions with meaningful messages

2. **Logging**:
    - Use the Python `logging` module instead of print statements
    - Configure logging levels appropriately
    - Include contextual information in log messages

3. **Configuration Management**:
    - Use environment variables for sensitive information
    - Store configuration in dedicated files (YAML/JSON)
    - Provide sensible defaults but allow for overrides

4. **Testing**:
    - Write tests for all new functionality
    - Aim for high test coverage
    - Use mocks to isolate unit tests from external dependencies

### Docker and Kafka

1. **Docker Compose**:
    - Use Docker Compose for managing multi-container applications
    - Define services, networks, and volumes in the docker-compose.yml file
    - Use environment variables for configuration

2. **Kafka Configuration**:
    - Follow Kafka best practices for topic configuration
    - Consider partitioning strategy based on use case
    - Set appropriate retention policies

3. **MirrorMaker 2**:
    - Use the recommended configurations for MirrorMaker 2
    - Consider topic renaming strategies
    - Monitor replication lag
