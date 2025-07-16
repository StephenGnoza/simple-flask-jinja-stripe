import json

def load_products(products_path):
    with open(products_path) as f:
        products_list = json.load(f)
        return {item["id"]: item for item in products_list}

def parse_custom_options(product, form_data):
    custom_options = {}
    if "options" in product:
        for option in product["options"]:
            label = option[0]
            field_name = f"option_{label.replace(' ', '_')}"
            value = form_data.get(field_name)
            if value:
                custom_options[label] = value
    return custom_options

def create_metadata(product_id, custom_options):
    metadata = {'product_id': product_id}
    for k, v in custom_options.items():
        metadata[f"option_{k}"] = v
    return metadata
