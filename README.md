# ormar-postgres-extensions

[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors) [![Maturity badge - level 1](https://img.shields.io/badge/Maturity-Level%201%20--%20New%20Project-yellow.svg)](https://github.com/tophat/getting-started/blob/master/scorecard.md) [![Stage](https://img.shields.io/pypi/status/ormar-postgres-extensions)](https://pypi.org/project/ormar-postgres-extensions/) [![Discord](https://img.shields.io/discord/809577721751142410?label=community%20chat)](https://discord.gg/YhK3GFcZrk)

[![Pypi](https://img.shields.io/pypi/v/ormar-postgres-extensions)](https://pypi.org/project/ormar-postgres-extensions/) [![Wheel](https://img.shields.io/pypi/wheel/ormar-postgres-extensions)](https://pypi.org/project/ormar-postgres-extensions/) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ormar-postgres-extensions) [![PyPI - Downloads](https://img.shields.io/pypi/dm/ormar-postgres-extensions)](https://pypi.org/project/ormar-postgres-extensions/) [![PyPI - License](https://img.shields.io/pypi/l/ormar-postgres-extensions)](./LICENSE)

![Build Status](https://github.com/tophat/ormar-postgres-extensions/workflows/Ormar%20Postgres%20Extensions%20CICD/badge.svg) [![codecov](https://codecov.io/gh/tophat/ormar-postgres-extensions/branch/master/graph/badge.svg)](https://codecov.io/gh/tophat/ormar-postgres-extensions)

## Overview

ormar-postgres-extensions is a an extension to the[Ormar](https://github.com/collerek/ormar) ORM. It enables developers to write models that map to native PostgreSQL types.

## Motivation

[Ormar](https://github.com/collerek/ormar) is an amazing async ORM that works with [FastAPI](https://github.com/tiangolo/fastapi). However, it is agnostic to the underlying database used meaning that we cannot use native PostgreSQL types such as UUID or JSONB columns. The aim of this library is to provide Ormar fields that can be used to generate database columns with native PG types.

## Installation

```shell
python -m pip install ormar-postgres-extensions
```

## Usage

### Fields

Two native PG fields are provided. The `PostgresJSONB` and `PostgresUUID` types map to native `JSONB` and `UUID` data types respectively. Using these in an Ormar model is as simple as importing the fields and using them in the model.

```python
from uuid import UUID

import ormar
from ormar_postgres_extensions import PostgresUUID


class MyModel(ormar.Model):
    uid: UUID = PostgresUUID(unique=True, nullable=False)
```

## Uninstalling

```python
pip uninstall ormar-postgres-extensions
```

## Contributing

Feel free to open a PR or GitHub issue. Contributions welcome!

To develop locally, clone this repository and run `. script/bootstrap` to install test dependencies. You can then use `invoke --list` to see available commands.
To run the tests locally, PostgreSQL needs to be running. This can be easily started via `inv database`.

### See contributing [guide](https://github.com/tophat/ormar-postgres-extensions/tree/master/CONTRIBUTING.md)
## Contributors

_You don't really have to add this section yourself! Simply use [all-contributors](https://allcontributors.org/) by adding comments in your PRs like so:_

```
@all-contributors please add <username> for <contribution type>
```

_Find out more about All-Contributors on their website!_


## License

`ormar-postgres-extensions` is licensed under [Apache License Version 2.0](https://github.com/tophat/ormar-postgres-extensions/tree/master/LICENSE).
