import data_fetcher


TEMPLATE_FILE = "animals_template.html"
OUTPUT_FILE = "animals.html"
PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def serialize_animal(animal):
    """Converts a single animal object into HTML"""

    output = ['<li class="cards__item">\n']

    if "name" in animal:
        output.append(f'  <div class="card__title">{animal["name"]}</div>\n')

    output.append('  <p class="card__text">\n')

    characteristics = animal.get("characteristics", {})

    if "diet" in characteristics:
        output.append(
            f'    <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'
        )

    if "locations" in animal and len(animal["locations"]) > 0:
        output.append(
            f'    <strong>Location:</strong> {animal["locations"][0]}<br/>\n'
        )

    if "type" in characteristics:
        output.append(
            f'    <strong>Type:</strong> {characteristics["type"]}<br/>\n'
        )

    output.append('  </p>\n')
    output.append('</li>\n')

    return "".join(output)


def serialize_animals(animals_data, animal_name):
    """Converts a list of animal objects into HTML"""

    if len(animals_data) == 0:
        return (
            f'<h2>Sorry, the animal "{animal_name}" '
            f'does not exist in this world.</h2>'
        )

    output = []

    for animal in animals_data:
        output.append(serialize_animal(animal))

    return "".join(output)


def write_html_to_file(template_file, output_file, placeholder, replacement):
    """Replaces placeholder in template and writes final HTML"""

    with open(template_file, "r", encoding="utf-8") as file:
        template = file.read()

    final_html = template.replace(placeholder, replacement)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(final_html)


def main():
    animal_name = input("Please enter an animal: ")

    animals_data = data_fetcher.fetch_data(animal_name)
    animals_html = serialize_animals(animals_data, animal_name)

    write_html_to_file(
        TEMPLATE_FILE,
        OUTPUT_FILE,
        PLACEHOLDER,
        animals_html
    )

    print(f"Website was successfully generated to the file {OUTPUT_FILE}.")


if __name__ == "__main__":
    main()