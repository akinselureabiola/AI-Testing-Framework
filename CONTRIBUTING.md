# Contributing

This document outlines the conventions and engineering practices used throughout the AI Testing Framework.

The primary goal of this project is to build a reusable testing framework that supports multiple AI applications within the AI Hub Platform, including the AI Resume Optimizer, the AI-powered IT Support Copilot, and future AI tools.

As the framework evolves, these guidelines help keep the project consistent, maintainable, and easy to extend.

---

## Code Style

This project follows standard Python conventions.

- Follow PEP 8.
- Prefer readability over cleverness.
- Keep functions, classes, and modules focused on a single responsibility.
- Use descriptive names for variables, functions, classes, and modules.
- Avoid unnecessary complexity. Start simple and improve only when there is a clear need.

---

## Documentation

Documentation should explain **why** something exists rather than repeating what the code already says.

- Every module should include a meaningful docstring.
- Keep comments concise and focused on engineering decisions.
- Update documentation whenever the behaviour of a component changes.

---

## Git Commit Convention

This project follows the Conventional Commits specification.

Examples:

```text
feat: add centralized configuration module
fix: resolve report directory path issue
docs: update framework architecture
refactor: simplify configuration loading
test: add regression tests for logger
chore: update project dependencies
```

---

## Project Structure

Each directory within the framework has a single responsibility.

```text
config/         Framework configuration
docs/           Project documentation
logs/           Generated log files
reports/        Test reports
screenshots/    Failure screenshots
tests/          Test suites
utilities/      Reusable helper modules
```

Reusable functionality belongs inside this framework.

Application-specific logic should remain inside the individual AI applications that consume the framework.

---

## Testing Philosophy

The purpose of this framework is to improve the quality and reliability of AI applications through reusable testing components.

As the framework grows, testing will include:

- Positive testing
- Negative testing
- Boundary testing
- Regression testing

The framework will evolve alongside the AI applications it supports, allowing testing capabilities to be shared rather than duplicated.

---

## Engineering Principles

Before introducing a new component, the following questions should be considered:

1. What problem does this solve?
2. Can it be reused by another AI application?
3. Does it improve the maintainability or simplicity of the framework?

These principles help ensure the framework grows intentionally rather than becoming unnecessarily complex.