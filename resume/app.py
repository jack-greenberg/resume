import click
from jinja2 import Template, Environment, PackageLoader
from pathlib import Path
import yaml
import pdfkit

DATA_PATH = Path("data/")
BUILD_PATH = Path("build/")

PDF_OPTIONS = {
    'margin-top': '0',
    'margin-right': '0',
    'margin-bottom': '0',
    'margin-left': '0',
}

env = Environment(loader=PackageLoader("resume", "templates"))


def read_file(file):
    file = DATA_PATH / file
    return open(file, "r").read()


def save_file(file, text):
    with open(file, "w+") as f:
        f.write(text)


def convert_to_pdf(file):
    pdfkit.from_file(str(file), str(BUILD_PATH / "build.pdf"), options=PDF_OPTIONS)


def parse_yaml(y):
    return yaml.safe_load(y)


@click.command()
def main():
    template = env.get_template("universal-resume.j2")

    resume_file = read_file("resume.yaml")
    rendered = template.render(
        r=parse_yaml(resume_file), template_name="universal-resume"
    )

    save_file(BUILD_PATH / "build.html", rendered)
    convert_to_pdf(BUILD_PATH / "build.html")


if __name__ == "__main__":
    main()
