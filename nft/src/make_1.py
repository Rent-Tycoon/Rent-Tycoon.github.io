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
# meta_generate.replace_and_save('lottery-gold_r2.json', '{#?}', 9, 50)
# meta_generate.replace_and_save('lottery-bronze_r2.json', '{#?}', 65, 50 + 9)
# meta_generate.replace_and_save('lottery-silver_r2.json', '{#?}', 25, 50 + 9 + 65)
# meta_generate.replace_and_save('lottery-golden_ticket.json', '{#?}', 1, 50 + 9 + 65 + 25, 1)


round2_end = 50 + 9 + 65 + 25 + 1
print(f'round2_end: {round2_end}')

# Rounde 3 ( 50+ )
meta_generate.replace_and_save('lottery-golden_ticket.json', '{#?}', 1, round2_end, 2)
meta_generate.replace_and_save('lottery-gold_r3.json', '{#?}', 9, round2_end + 1)
meta_generate.replace_and_save('lottery-silver_r3.json', '{#?}', 25, round2_end + 1 + 9)
meta_generate.replace_and_save('lottery-bronze_r3.json', '{#?}', 65, round2_end + 1 + 9 + 25) 

