import json

def replace_and_save(template_file, placeholder, count, start, start_internal = 0, meta_folder = 'meta'):
    with open(f"../{meta_folder}/tmpl/{template_file}", 'r', encoding='utf-8') as file:
        template = json.load(file)

    for i in range(start, start + count):
        output_file = f"nft_{i}.json"
        
        modified_template = json.loads(json.dumps(template).replace(placeholder, str(i - start + 1 + start_internal)))

        output_file = f"../{meta_folder}/{output_file}"
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(modified_template, file, ensure_ascii=False, indent=4)

        print(f"file saved: {output_file} and type {template_file} - {i - start + 1}")