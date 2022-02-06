# Interop Template

Interop-based application.

To get started:

- [PyEnv](https://github.com/pyenv/pyenv)
- [Poetry](https://python-poetry.org/)
- [RabbitMQ](https://www.rabbitmq.com/)

replace all occurrences of `interop_template` with your preferred app name and then scaffold a standalone app
```bash

make init

#: be sure to modify environment variables

#: scaffold publishers and modify  - optional
#: publishers would be created in the publisher sub-directory
interop publisher <publisher-name>

#: scaffold subscribers and modify  - optional
#: subscribers would be created in the subscriber sub-directory
interop subscriber <subscriber-name>

#: run the application
make start

```