# Learn Django Modular (Web App with Python)

## How to create Django Module and Project
to be...

## How to generate CSS Tailwind & DaisyUI
to be...

## How to make Django Migration

```sh
pdm run src/manage.py makemigrations <module_name> --empty -n <migration_name>
```

execution:
```sh
pdm run src/manage migrate
```

show migration:
```sh
pdm run src/manage showmigrations
```

revert:
```sh
pdm run src/manage migrate <module_name> <number>
```