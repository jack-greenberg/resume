import click
from jinja2 import Template, Environment, PackageLoader
from pathlib import Path
import yaml

DATA_PATH = Path("data/")


def get_resume(file):
    file = DATA_PATH / file
    return open(file, "r").read()


def parse_yaml(y):
    return yaml.safe_load(y)


@click.command()
def main():
    env = Environment(loader=PackageLoader("resume", "templates"))
    template = env.get_template("universal-resume.j2")
    resume_file = get_resume("resume.yaml")
    rendered = template.render(r=parse_yaml(resume_file))
    print(rendered)


if __name__ == "__main__":
    main()
