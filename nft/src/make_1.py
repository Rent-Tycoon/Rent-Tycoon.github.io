# lottery-bronze.json - 25
# lottery-silver.json - 15
# lottery-gold.json - 9
# lottery-golden_ticket.json - 1

import json

def replace_and_save(template_file, placeholder, count, start):
    with open(f"../meta/tmpl/{template_file}", 'r', encoding='utf-8') as file:
        template = json.load(file)

    for i in range(start, start + count):
        output_file = f"nft_{i}.json"
        
        modified_template = json.loads(json.dumps(template).replace(placeholder, str(i - start + 1)))

        output_file = f"../meta/{output_file}"
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(modified_template, file, ensure_ascii=False, indent=4)

        print(f"file saved: {output_file} and type {template_file} - {i - start + 1}")

# Rounde 1
# replace_and_save('lottery-bronze.json', '{#?}', 25, 0)
# replace_and_save('lottery-silver.json', '{#?}', 15, 25)
# replace_and_save('lottery-gold.json', '{#?}', 9, 25 + 15)
# replace_and_save('lottery-golden_ticket.json', '{#?}', 1, 25 + 15 + 9)

# Rounde 2 ( 50+ )
replace_and_save('lottery-silver_r2.json', '{#?}', 15, 50 + 25)
replace_and_save('lottery-gold_r2.json', '{#?}', 9, 50 + 25 + 15)
replace_and_save('lottery-golden_r2_ticket.json', '{#?}', 1, 50 + 25 + 15 + 9)
