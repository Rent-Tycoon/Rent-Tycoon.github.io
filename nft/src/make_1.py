# lottery-bronze.json - 25
# lottery-silver.json - 15
# lottery-gold.json - 9
# lottery-golden_ticket.json - 1

from lib import meta_generate

# Rounde 1
# meta_generate.replace_and_save('lottery-bronze.json', '{#?}', 25, 0)
# meta_generate.replace_and_save('lottery-silver.json', '{#?}', 15, 25)
# meta_generate.replace_and_save('lottery-gold.json', '{#?}', 9, 25 + 15)
# meta_generate.replace_and_save('lottery-golden_ticket.json', '{#?}', 1, 25 + 15 + 9)

# Rounde 2 ( 50+ )
meta_generate.replace_and_save('lottery-gold_r2.json', '{#?}', 9, 50)
meta_generate.replace_and_save('lottery-bronze_r2.json', '{#?}', 65, 50 + 9)
meta_generate.replace_and_save('lottery-silver_r2.json', '{#?}', 25, 50 + 9 + 65)
meta_generate.replace_and_save('lottery-golden_ticket.json', '{#?}', 1, 50 + 9 + 65 + 25, 1)
